from .models import ContactMessage

def unread_contacts_context(request):
    # Yalnız admin səhifələrində (və ya staff userlər üçün) badge hesablanması
    if request.user.is_authenticated and request.user.is_staff:
        # /admin/ urls should be covered
        if request.path.startswith('/admin/'):
            count = ContactMessage.objects.filter(is_read=False).count()
            return {'unread_contacts_count': count}
    return {}
