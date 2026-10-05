from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class PostCategory(models.Model):
    name = models.CharField("Kateqoriya Adı", max_length=100, help_text="Məqalə kateqoriyası (məs: Texnologiya, Dizayn, Proqramlaşdırma)")
    slug = models.SlugField("URL Keçid (Slug)", unique=True, help_text="Avtomatik doldurulur və ya unikal latın qısaltması")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Məqalə Kateqoriyası")
        verbose_name_plural = _("Məqalə Kateqoriyaları")

class Tag(models.Model):
    name = models.CharField("Teq Adı", max_length=50, help_text="Açar söz / teq (məs: web, ui, mobile)")
    slug = models.SlugField("URL Keçid (Slug)", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Teq")
        verbose_name_plural = _("Teqlər")

class Post(models.Model):
    title = models.CharField("Məqalə Başlığı", max_length=200, help_text="Məqalənin əsas başlığı (məs: Müasir Veb Dizayn Trendləri)")
    slug = models.SlugField("URL Keçid (Slug)", unique=True, help_text="Məqalə linki (məs: muasir-veb-dizayn-trendleri)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Müəllif", help_text="Məqaləni yazan istifadəçi")
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name="Kateqoriya", help_text="Aid olduğu mövzu/kateqoriya")
    cover_image = models.ImageField("Əsas Şəkil (Cover)", upload_to='blog/', help_text="Məqalə kartında və səhifəsində görünən əsas şəkil")
    excerpt = models.TextField("Qısa Məzmun (Excerpt)", max_length=300, help_text="Kartın üzərində görünən 1-2 cümləlik qısa xülasə")
    content = models.TextField("Məqalənin Tam Mətni", help_text="Məqalənin tam oxunan geniş mətni")
    reading_time = models.PositiveIntegerField("Oxuma Müddəti (dəqiqə)", default=5, help_text="Təxmini oxuma vaxtı")
    views_count = models.PositiveIntegerField("Baxış Sayı", default=0, editable=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name="Teqlər (Açar sözlər)")
    is_featured = models.BooleanField("Seçilmiş Məqalə", default=False, help_text="Xüsusi vurğulanmış/seçilmiş kimi göstərilsin?")
    created_at = models.DateTimeField("Dərc Tarixi", auto_now_add=True)
    updated_at = models.DateTimeField("Son Yenilənmə Tarixi", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Məqalə")
        verbose_name_plural = _("Blog Məqalələri")

