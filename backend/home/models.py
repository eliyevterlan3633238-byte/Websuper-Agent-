from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

def validate_image_size(image):
    limit_mb = 5
    if image.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Maksimum fayl ölçüsü {limit_mb} MB ola bilər.")
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

class HeroContent(SingletonModel):
    title = models.CharField(max_length=200, default="Rəqəmsal Dünyada")
    gradient_text = models.CharField(max_length=200, default="İz Buraxın", help_text="Başlığın qradiyent rəngli ikinci sətri")
    subtitle = models.TextField(default="Müasir texnologiyalar və innovativ dizaynla biznesinizi inkişaf etdiririk. Sizin uğurunuz, bizim prioritetimizdir.")
    button1_text = models.CharField(max_length=50, default="Layihəyə Başla")
    button1_link = models.CharField(max_length=200, default="/contact/")
    button2_text = models.CharField(max_length=50, default="Portfolioya Bax")
    button2_link = models.CharField(max_length=200, default="/portfolio/")
    
    class Meta:
        verbose_name = _("Əsas Hero Başlığı")
        verbose_name_plural = _("Ana Səhifə Hero Bölməsi")

    def __str__(self):
        return "Home Hero Bölməsi"


class Service(models.Model):
    title = models.CharField("Xidmətin Adı", max_length=100, help_text="Xidmətin adı (məs: Veb İnkişaf, Mobil Tətbiq, UI/UX Dizayn)")
    description = models.TextField("Xidmətin İzahı", help_text="Xidmət haqqında qısa izah mətni")
    icon_class = models.CharField("İkon Kodu (FontAwesome)", max_length=50, default="fas fa-laptop-code", help_text="FontAwesome ikonu (məs: fas fa-laptop-code, fas fa-mobile-alt, fas fa-paint-brush)")
    order = models.IntegerField("Sıralama", default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField("Aktivdir", default=True, help_text="Saytda aktiv olaraq görünsün?")

    class Meta:
        ordering = ['order']
        verbose_name = _("Xidmət")
        verbose_name_plural = _("Xidmətlərimiz Bölməsi (3 Əsas Kart)")

    def __str__(self):
        return self.title


class ProcessStep(models.Model):
    step_number = models.CharField("Mərhələ Nömrəsi", max_length=10, default="1", help_text="Mərhələnin nömrəsi (məs: 1, 2, 3, 4)")
    title = models.CharField("Mərhələ Başlığı", max_length=100, help_text="Mərhələnin adı (məs: Kəşfiyyat, Dizayn, Development, Təhvil & Dəstək)")
    description = models.TextField("Mərhələ İzahı", help_text="Mərhələ haqqında qısa izah mətni")
    order = models.IntegerField("Sıralama", default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField("Aktivdir", default=True, help_text="Saytda aktiv görünsün?")

    class Meta:
        ordering = ['order', 'step_number']
        verbose_name = _("İş Prosesi Mərhələsi")
        verbose_name_plural = _("İş Prosesimiz Mərhələləri (1, 2, 3, 4)")

    def __str__(self):
        return f"{self.step_number}. {self.title}"


class CtaBanner(SingletonModel):
    title = models.CharField("Bölmə Başlığı", max_length=200, default="Layihənizi Bu Gün Başladaq", help_text="Böyük əsas başlıq (məs: Layihənizi Bu Gün Başladaq)")
    subtitle = models.TextField("Alt İzah Mətni", default="Peşəkar komandamızla birlikdə biznesinizi rəqəmsal zirvəyə qaldırın.", help_text="Başlığın altındakı izah mətni")
    button_text = models.CharField("Düymə Mətni", max_length=50, default="Bizimlə Əlaqə", help_text="Düymə üzərində görünən yazı")
    button_url = models.CharField("Düymə Linki (URL)", max_length=200, default="/contact/", help_text="Düyməyə klik edildikdə açılacaq link (məs: /contact/)")
    background_image = models.ImageField("Arxa Fon Şəkili", upload_to='cta/', blank=True, null=True, help_text="İstəyə bağlı: Xüsusi arxa fon şəkili (boş qalarsa əllər olan yaşıl şablon qalır)")

    class Meta:
        verbose_name = _("Son CTA Bölməsi")
        verbose_name_plural = _("Son CTA Bölməsi (Layihənizi Başladaq)")

    def __str__(self):
        return "Son CTA Bölməsi (Layihənizi Başladaq)"


class PricingPlan(models.Model):
    name = models.CharField(max_length=100, help_text="Paketin adı (məs: Başlanğıc, Standart, Premium)")
    price = models.CharField(max_length=50, help_text="Qiymət (məs: 500 AZN-dən, 1200 AZN-dən)")
    description = models.TextField(help_text="Paketin qısa izahı")
    features = models.TextField(help_text="Hər xüsusiyyəti yeni sətirdə yazın (Enter-lə ayırın).")
    is_popular = models.BooleanField(default=False, help_text="'Ən Populyar' etiketi göstərilsin?")
    order = models.IntegerField(default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField(default=True, help_text="Saytda aktiv görünsün?")

    class Meta:
        ordering = ['order']
        verbose_name = _("Qiymət Paketi")
        verbose_name_plural = _("Qiymət Paketləri (Tariflər)")

    def __str__(self):
        return self.name
        
    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class Stat(models.Model):
    number = models.CharField(max_length=50, help_text="Statistika rəqəmi (məs: 150+, 50+, 5+, 24/7)")
    label = models.CharField(max_length=100, help_text="Statistikanın izahı (məs: Layihə, Müştəri, İl Təcrübə, Dəstək)")
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="İstəyə bağlı FontAwesome ikonu (məs: fa-solid fa-users)")
    order = models.IntegerField(default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField(default=True, help_text="Saytda aktiv görünsün?")

    class Meta:
        ordering = ['order']
        verbose_name = _("Statistika Rəqəmi")
        verbose_name_plural = _("Statistika Bloku (150+, 50+ və s.)")

    def __str__(self):
        return f"{self.number} - {self.label}"


class ShowcaseItem(models.Model):
    title = models.CharField(max_length=150, help_text="Slaydın əsas başlığı (məs: Veb Tətbiqlər, Mobil Tətbiqlər, Kreativ Brendinq)")
    subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Qısa alt başlıq və ya istiqamətlər (məs: iOS və Android, Nativ Həllər)")
    description = models.TextField(help_text="Kartın üzərində görünən izah mətni")
    image = models.ImageField(upload_to='showcase/', help_text="Slaydın arxa fon şəkili")
    button_text = models.CharField(max_length=50, default="Ətraflı Bax", help_text="Düymə mətni")
    button_url = models.CharField(max_length=200, default="/portfolio/", help_text="Düyməyə klik edildikdə açılacaq link")
    order = models.IntegerField(default=0, help_text="Görünmə ardıcıllığı")
    is_active = models.BooleanField(default=True, help_text="Saytda aktiv görünsün?")

    class Meta:
        ordering = ['order']
        verbose_name = _("Ana Səhifə Slaydı")
        verbose_name_plural = _("Ana Səhifə Slayderi")

    def __str__(self):
        return self.title

    @property
    def link(self):
        return self.button_url


class SiteSettings(SingletonModel):
    address = models.CharField(max_length=200, default="Baku, Azerbaijan", help_text="Ünvan mətni")
    map_embed_url = models.TextField(
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d194473.42999433604!2d49.71487679318182!3d40.394508493134114!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40307d6bd6211cf9%3A0x343f6b5e7ae56c6b!2sBaku%2C%20Azerbaijan!5e0!3m2!1sen!2s!4v1690000000000!5m2!1sen!2s",
        help_text="Google Maps 'Embed' (Yerləşdirmə) linki. Xəritədə Share -> Embed a map hissəsindən 'src' daxilindəki linki kopyalayın."
    )
    phone = models.CharField(max_length=50, default="+994 50 000 00 00", help_text="Əlaqə nömrəsi")
    email = models.EmailField(default="info@websuper.az", help_text="Əlaqə e-poçt ünvanı") 
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn profil linki")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram profil linki")
    whatsapp = models.URLField(blank=True, null=True, help_text="WhatsApp nömrəsi və ya linki (məsələn: https://wa.me/994501234567)")

    # Hero Background Images
    about_hero_image = models.ImageField(upload_to='hero_images/', blank=True, null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Haqqımızda səhifəsinin arxa fon şəkli (Max 5MB. Format: jpg, png, webp)")
    portfolio_hero_image = models.ImageField(upload_to='hero_images/', blank=True, null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Portfolio səhifəsinin arxa fon şəkli (Max 5MB. Format: jpg, png, webp)")
    blog_hero_image = models.ImageField(upload_to='hero_images/', blank=True, null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Blog səhifəsinin arxa fon şəkli (Max 5MB. Format: jpg, png, webp)")
    contact_hero_image = models.ImageField(upload_to='hero_images/', blank=True, null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Əlaqə səhifəsinin arxa fon şəkli (Max 5MB. Format: jpg, png, webp)")

    # Home Page Background Images
    stats_section_bg_image = models.ImageField(upload_to='hero_images/', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Ana səhifə - Statistika bölməsinin fon şəkli (Max 5MB. Format: jpg, png, webp)")
    process_section_bg_image = models.ImageField(upload_to='hero_images/', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Ana səhifə - İş Prosesimiz bölməsinin fon şəkli (Max 5MB. Format: jpg, png, webp)")
    cta_section_bg_image = models.ImageField(upload_to='hero_images/', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']), validate_image_size],
        help_text="Ana səhifə - CTA (Layihənizi Başladaq) bölməsinin fon şəkli (Max 5MB. Format: jpg, png, webp)")

    class Meta:
        verbose_name = _("Sayt Əlaqə & Sosial Media Tənzimləmələri")
        verbose_name_plural = _("Sayt Ümumi Tənzimləmələri")

    def __str__(self):
        return "Sayt Ümumi Məlumatları"

    def save(self, *args, **kwargs):
        if self.map_embed_url and '<iframe' in self.map_embed_url:
            import re
            match = re.search(r'src="([^"]+)"', self.map_embed_url)
            if match:
                self.map_embed_url = match.group(1)
        super().save(*args, **kwargs)
