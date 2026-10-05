from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactMessage(models.Model):
    name = models.CharField("Ad və Soyad", max_length=150, help_text="Müraciət edən şəxsin tam adı")
    email = models.EmailField("E-poçt Ünvanı", help_text="Müraciət edənin əlaqə e-poçtu")
    phone = models.CharField("Telefon Nömrəsi", max_length=50, blank=True, null=True, help_text="Əlaqə telefon nömrəsi")
    subject = models.CharField("Müraciət Mövzusu", max_length=200, help_text="Müraciətin qısa mövzusu")
    message = models.TextField("Mesaj Mətni", help_text="Müraciət edən şəxsin göndərdiyi ətraflı mesaj mətni")
    is_read = models.BooleanField("Oxundu", default=False, help_text="Mesaj oxunubsa işarələyin")
    created_at = models.DateTimeField("Göndərilmə Tarixi", auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Gələn Mesaj")
        verbose_name_plural = _("Gələn Mesajlar (Əlaqə Formu)")

class LiveChatMessage(models.Model):
    name = models.CharField("Ad", max_length=150)
    message = models.TextField("Mesaj")
    is_read = models.BooleanField("Oxundu", default=False)
    created_at = models.DateTimeField("Tarix", auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Canlı Çat Mesajı")
        verbose_name_plural = _("Canlı Çat Mesajları")

from home.models import SiteSettings

class ContactSettings(SiteSettings):
    class Meta:
        proxy = True
        verbose_name = _("Əlaqə Tənzimləmələri")
        verbose_name_plural = _("Əlaqə Tənzimləmələri (Xəritə, Nömrə)")

