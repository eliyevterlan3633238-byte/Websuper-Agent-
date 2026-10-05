from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from .models import ContactMessage, ContactSettings
from home.admin import SiteSettingsAdmin

@admin.register(ContactSettings)
class ContactSettingsAdmin(SiteSettingsAdmin):
    fieldsets = (
        (_('Əlaqə Məlumatları və Xəritə'), {
            'fields': ('address', 'map_embed_url', 'phone', 'email')
        }),
        (_('Sosial Şəbəkələr'), {
            'fields': ('linkedin', 'whatsapp', 'instagram'),
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone', 'status_indicator', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    list_editable = ()
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    
    fieldsets = (
        (_('Müştəri Məlumatları'), {
            'fields': ('name', 'email', 'phone'),
            'description': _('Müraciət göndərən şəxsin əlaqə vasitələri')
        }),
        (_('Mesajın Məzmunu'), {
            'fields': ('subject', 'message'),
            'description': _('Göndərilən müraciət mövzusu və ətraflı mətn')
        }),
        (_('Status və Tarix'), {
            'fields': ('is_read', 'created_at'),
            'description': _('Mesajın oxunma vəziyyəti və qəbul edilmə vaxtı')
        }),
    )

    def status_indicator(self, obj):
        if not obj.is_read:
            return mark_safe('<b><span style="color: #ef4444;">●</span> Oxunmayıb</b>')
        return mark_safe('<span style="color: #10b981;">●</span> Oxunub')
    status_indicator.short_description = _('Status')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Auto-mark as read when opened
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=['is_read'])
        return super().change_view(request, object_id, form_url, extra_context)

