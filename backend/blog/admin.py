from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin as TranslationAdmin
from .models import PostCategory, Tag, Post

@admin.register(PostCategory)
class PostCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'author', 'reading_time', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured',)

