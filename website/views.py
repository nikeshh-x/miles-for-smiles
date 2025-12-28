from django.shortcuts import render
from .models import Partner, GalleryMedia, TeamMember

# Create your views here.

def home(request):
    # Get all partners to display on the home page
    partners = Partner.objects.all()

    # Get all gallery media to display on the home page
    gallery_items = GalleryMedia.objects.all()[:6]
    
    # Get all team members to display on the home page
    teams = TeamMember.objects.all()
    
    context = {
        'partners':partners,
        'gallery_items':gallery_items,
        'teams':teams,
    }
    return render(request, 'website/home.html', context)


def gallery(request):
    # Get all gallery media
    gallery_items = GalleryMedia.objects.all()
    context = {
        'gallery_items': gallery_items,
    }
    return render(request, 'website/galleryPage.html', context)
