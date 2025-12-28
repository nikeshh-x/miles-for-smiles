from django.contrib import admin
from .models import Partner, GalleryMedia, TeamMember, ContactMessage

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

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'submitted_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['submitted_at']
    list_editable = ['is_read']

    def has_add_permission(self, request):
        return False