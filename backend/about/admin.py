from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin as TranslationAdmin
from .models import AboutSection, TeamMember, Value

@admin.register(AboutSection)
class AboutSectionAdmin(TranslationAdmin):
    pass

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('name', 'role', 'experience_years', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role', 'skills')

@admin.register(Value)
class ValueAdmin(TranslationAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
