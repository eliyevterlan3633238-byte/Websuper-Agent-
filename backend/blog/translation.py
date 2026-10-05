from modeltranslation.translator import register, TranslationOptions
from .models import PostCategory, Tag, Post

@register(PostCategory)
class PostCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'content')
