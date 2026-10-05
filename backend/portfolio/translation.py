from modeltranslation.translator import register, TranslationOptions
from .models import Category, Project

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'problem_statement', 'solution', 'result', 'client_quote')
