from django.contrib import admin
from .models import Partner, GalleryMedia, TeamMember

# Register your models here.

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('created_at',)

@admin.register(GalleryMedia)
class GalleryMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at', 'updated_at')
    ordering = ('-uploaded_at',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at', 'updated_at')
    search_fields = ('name', 'role')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)