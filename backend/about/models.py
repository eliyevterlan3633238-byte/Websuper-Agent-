from django.db import models
from django.utils.translation import gettext_lazy as _

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class AboutSection(SingletonModel):
    heading = models.CharField(max_length=200, default="Bizim Hekayəmiz", help_text="Bölmənin əsas başlığı (məs: Bizim Hekayəmiz)")
    subheading = models.CharField(max_length=200, default="WebSuper Agency", blank=True, help_text="Qradiyent rəngli alt başlıq")
    description = models.TextField(help_text="Haqqımızda bölməsinin əsas hekayə mətni")
    mission = models.TextField(blank=True, null=True, help_text="Missiyamız mətni")
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Yan tərəfdə görünən komanda/ofis şəkili")

    class Meta:
        verbose_name = _("Haqqımızda Məzmunu")
        verbose_name_plural = _("Haqqımızda Bölməsi")

    def __str__(self):
        return "Haqqımızda Əsas Məzmunu"


class TeamMember(models.Model):
    name = models.CharField(max_length=100, help_text="Komanda üzvünün tam adı")
    role = models.CharField(max_length=100, help_text="Vəzifəsi (məs: CEO & Founder, Lead Designer, Senior Developer)")
    bio = models.TextField(blank=True, null=True, help_text="Qısa tərcümeyi-hal / haqqında məlumat")
    image = models.ImageField(upload_to='team/', help_text="Komanda üzvünün şəkili")
    experience_years = models.PositiveIntegerField(default=0, help_text="Neçə illik təcrübəsi var")
    skills = models.TextField(blank=True, null=True, help_text="Əsas bacarıqları (məs: UI/UX Dizayn, Figma, Python, Django)")
    projects = models.TextField(blank=True, null=True, help_text="Bitirdiyi əsas layihələr və ya nailiyyətlər")
    order = models.PositiveIntegerField(default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField(default=True, help_text="Saytda aktiv görünsün?")

    class Meta:
        ordering = ['order']
        verbose_name = _("Komanda Üzvü")
        verbose_name_plural = _("Komanda Üzvləri (Haqqımızda/Ana Səhifə)")

    def __str__(self):
        return self.name


class Value(models.Model):
    title = models.CharField(max_length=100, help_text="Dəyərin adı (məs: İnnovasiya, Etibarlılıq, Keyfiyyət)")
    description = models.TextField(help_text="Dəyərin qısa izahı")
    icon = models.CharField(max_length=50, help_text="FontAwesome ikonu (məs: fas fa-lightbulb, fas fa-handshake, fas fa-gem)")
    order = models.PositiveIntegerField(default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField(default=True, help_text="Saytda aktiv görünsün?")

    class Meta:
        ordering = ['order']
        verbose_name = _("Dəyər")
        verbose_name_plural = _("Dəyərlərimiz (Haqqımızda)")

    def __str__(self):
        return self.title
