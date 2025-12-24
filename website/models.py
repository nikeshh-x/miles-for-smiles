from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/logos/')
    website = models.URLField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def  __str__(self):
        return self.name
    
class GalleryMedia(models.Model):

    # MEDIA_TYPE_CHOICCES = [
    #     ('image', 'Image'),
    #     ('video', 'Video'),
    # ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    #media_type = models.CharField(max_length=10) choices=MEDIA_TYPE_CHOICCES, default='image'
    image = models.ImageField(upload_to='gallery/images/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Gallery Media'
        verbose_name_plural = 'Gallery Media'
    
    def __str__(self):
        return self.title
    
    
    