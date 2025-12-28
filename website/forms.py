from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border-2 border-gray-200 rounded-xl px-4 py-3 focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition-all outline-none',
                'placeholder': 'John Doe'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border-2 border-gray-200 rounded-xl px-4 py-3 focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition-all outline-none',
                'placeholder': 'john@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full border-2 border-gray-200 rounded-xl px-4 py-3 focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition-all outline-none',
                'placeholder': '+977-98xxxxxxxx'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full border-2 border-gray-200 rounded-xl px-4 py-3 focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition-all outline-none resize-none',
                'placeholder': 'How can we help you?',
                'rows': 5
            }),
        }