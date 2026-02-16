from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('event/<int:id>/', views.eventDetails, name='event')
]
