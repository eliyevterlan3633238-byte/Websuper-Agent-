from modeltranslation.translator import register, TranslationOptions
from .models import HeroContent, Service, ProcessStep, CtaBanner, PricingPlan, Stat, ShowcaseItem, SiteSettings

@register(HeroContent)
class HeroContentTranslationOptions(TranslationOptions):
    fields = ('title', 'gradient_text', 'subtitle', 'button1_text', 'button2_text')

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ProcessStep)
class ProcessStepTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(CtaBanner)
class CtaBannerTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_text')

@register(PricingPlan)
class PricingPlanTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'features')

@register(Stat)
class StatTranslationOptions(TranslationOptions):
    fields = ('label',)

@register(ShowcaseItem)
class ShowcaseItemTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'button_text')

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('address',)

