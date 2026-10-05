from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.db import models
from modeltranslation.admin import TabbedTranslationAdmin as TranslationAdmin
from .models import HeroContent, Service, ProcessStep, CtaBanner, PricingPlan, Stat, ShowcaseItem, SiteSettings

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            output.append(f'<a href="{image_url}" target="_blank"><img src="{image_url}" alt="{name}" width="150" height="150" style="object-fit: cover; border-radius: 5px; margin-bottom: 10px;"/></a><br>')
        output.append(super().render(name, value, attrs, renderer))
        return mark_safe(''.join(output))

@admin.register(HeroContent)
class HeroContentAdmin(TranslationAdmin):
    pass

@admin.register(ShowcaseItem)
class ShowcaseItemAdmin(TranslationAdmin):
    list_display = ('title', 'button_text', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')

@admin.register(Stat)
class StatAdmin(TranslationAdmin):
    list_display = ('label', 'number', 'order', 'is_active')
    list_editable = ('number', 'order', 'is_active')
    search_fields = ('label', 'number')

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'icon_class', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')

@admin.register(ProcessStep)
class ProcessStepAdmin(TranslationAdmin):
    list_display = ('step_number', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')

@admin.register(PricingPlan)
class PricingPlanAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'is_popular', 'order', 'is_active')
    list_editable = ('is_popular', 'order', 'is_active')
    search_fields = ('name',)

@admin.register(CtaBanner)
class CtaBannerAdmin(TranslationAdmin):
    pass

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }
    
    fieldsets = (
        (_('Ümumi Əlaqə'), {
            'fields': ('address', 'map_embed_url', 'phone', 'email')
        }),
        (_('Sosial Şəbəkələr (Header & Footer)'), {
            'fields': ('linkedin', 'whatsapp', 'instagram'),
            'description': 'Bu 3 şəbəkə (LinkedIn, WhatsApp, Instagram) saytın Yuxarı (Header) hissəsində xüsusi olaraq göstərilir. Bütün linklər həmçinin Footer-də də istifadə oluna bilər.'
        }),
        (_('Arxa Fon Şəkilləri (Hero Bölməsi)'), {
            'fields': ('about_hero_image', 'portfolio_hero_image', 'blog_hero_image', 'contact_hero_image'),
            'description': 'Saytın müxtəlif səhifələrinin ən üst hissəsində (Hero bölməsində) görünəcək şəkilləri buradan idarə edə bilərsiniz. Şəkil yüklənməsə, standart (default) şəkillər görünəcək.'
        }),
        (_('Ana Səhifə Arxa Fon Şəkilləri'), {
            'fields': ('stats_section_bg_image', 'process_section_bg_image', 'cta_section_bg_image'),
            'description': 'Ana səhifədəki Statistika, İş Prosesimiz və CTA bölmələrinin arxa fon şəkillərini buradan idarə edə bilərsiniz.'
        }),
    )

