from modeltranslation.translator import register, TranslationOptions
from .models import ContactSettings

@register(ContactSettings)
class ContactSettingsTranslationOptions(TranslationOptions):
    fields = ('address',)
