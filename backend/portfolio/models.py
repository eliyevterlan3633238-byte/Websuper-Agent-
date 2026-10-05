from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Kateqoriyanın adı (məs: Veb İnkişaf, Mobil Tətbiq, Brendinq)")
    slug = models.SlugField(unique=True, help_text="URL üçün unikal identifikator")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Layihə Kateqoriyası")
        verbose_name_plural = _("Layihə Kateqoriyaları")

class Project(models.Model):
    title = models.CharField(max_length=200, help_text="Layihənin adı")
    slug = models.SlugField(unique=True, help_text="URL üçün unikal identifikator")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', help_text="Aid olduğu kateqoriya")
    order = models.PositiveIntegerField(default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField(default=True, help_text="Saytda aktiv görünsün?")
    client_name = models.CharField(max_length=150, blank=True, null=True, help_text="Müştərinin adı / şirkət")
    project_url = models.URLField(blank=True, null=True, help_text="Layihənin canlı veb sayt / tətbiq linki")
    description = models.TextField(help_text="Layihə haqqında ümumi məlumat")
    problem_statement = models.TextField(blank=True, null=True, help_text="Qarşıya qoyulan problem")
    solution = models.TextField(blank=True, null=True, help_text="Təqdim etdiyimiz həll")
    result = models.TextField(blank=True, null=True, help_text="Əldə olunan nəticə")
    technologies = models.CharField(max_length=255, help_text="İstifadə olunan texnologiyalar (vergüllə ayrılmış, məs: Python, Django, React)")
    client_quote = models.TextField(blank=True, null=True, help_text="Müştərinin rəyi")
    cover_image = models.ImageField(upload_to='portfolio/', help_text="Layihənin əsas üzlük şəkili")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = _("Portfolio Layihəsi")
        verbose_name_plural = _("Portfolio Layihələri")

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio/gallery/', help_text="Əlavə qalereya şəkili")
    order = models.PositiveIntegerField(default=0, help_text="Şəkillərin qalereyadakı ardıcıllığı")

    class Meta:
        ordering = ['order']
        verbose_name = _("Layihə Qalereya Şəkili")
        verbose_name_plural = _("Layihə Qalereyası Şəkilləri")

    def __str__(self):
        return f"{self.project.title} Image"
