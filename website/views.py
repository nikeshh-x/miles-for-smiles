from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Partner, GalleryMedia, TeamMember, Events
from django.utils import timezone


# Create your views here.

def home(request):
    # Get all partners to display on the home page
    partners = Partner.objects.all()

    # Get all gallery media to display on the home page
    gallery_items = GalleryMedia.objects.all()[:6]
    
    # Get all team members to display on the home page
    teams = TeamMember.objects.all()

    # Get the events
    events = Events.objects.all()[:3]
    
    context = {
        'partners':partners,
        'gallery_items':gallery_items,
        'teams':teams,
        'events':events,
    }
    return render(request, 'website/home.html', context)


def gallery(request):
    # Get all gallery media
    gallery_items = GalleryMedia.objects.all()
    context = {
        'gallery_items': gallery_items,
    }
    return render(request, 'website/galleryPage.html', context)

def events(request):
    """Display all events with filters"""
    events = Events.objects.all()
    
    # Apply filters
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    
    
    if status_filter and status_filter != 'ALL':
        events = events.filter(status=status_filter)
    
    if search_query:
        events = events.filter(title__icontains=search_query) | \
                 events.filter(description__icontains=search_query) | \
                 events.filter(venue__icontains=search_query)
    
    # Get counts for stats
    total_events = events.count()
    upcoming_events = events.filter(start_date__gt=timezone.now()).count()
    
    context = {
        'events': events,
        'all_statuses': Events.STATUS_CHOICES,
        'current_status': status_filter,
        'search_query': search_query,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'website/eventPage.html', context)  # or 'events/events.html'

def eventDetails(request, id):
    return (request, 'website/eventDetail.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Try Sending Mail
            try:
                send_mail(
                    subject=f'New Contact Form Submission from {contact_message.name}',
                    message=f'''
                    New contact form submission:
                    
                    Name: {contact_message.name}
                    Email: {contact_message.email}
                    Phone: {contact_message.phone}
                    
                    Message:
                    {contact_message.message}
                    ''',
                    from_email=contact_message.DEFAULT_FROM_EMAIL,
                    recipient_list=['nikeshmanandhar16@gmail.com'],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email error:{e}")
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
        
    return render(request, 'website/contact.html',context)