from modeltranslation.translator import register, TranslationOptions
from .models import AboutSection, TeamMember, Value

@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('heading', 'subheading', 'description', 'mission')

@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role', 'bio', 'skills', 'projects')

@register(Value)
class ValueTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
