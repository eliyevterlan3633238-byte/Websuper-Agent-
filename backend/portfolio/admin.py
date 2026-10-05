from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin as TranslationAdmin
from .models import Category, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'client_name')
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('project_url',)
    inlines = [ProjectImageInline]

admin.site.register(ProjectImage)
