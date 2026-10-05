import os
import django
import urllib.request
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from blog.models import Post, PostCategory, Tag
from django.contrib.auth import get_user_model

User = get_user_model()
author = User.objects.first()

if not author:
    print("No user found. Exiting.")
    exit()

# Create Category
cat, _ = PostCategory.objects.get_or_create(name='Texnologiya', slug='texnologiya')

# Create Tags
tag_ai, _ = Tag.objects.get_or_create(name='AI', slug='ai')
tag_web3, _ = Tag.objects.get_or_create(name='Web3', slug='web3')

for i in range(1, 4):
    title = f'Müasir Veb Dizayn Trendləri {i}'
    slug = f'muasir-veb-dizayn-trendleri-{i}'
    
    if not Post.objects.filter(slug=slug).exists():
        p = Post(
            title=title,
            slug=slug,
            author=author,
            category=cat,
            excerpt='İstifadəçilərin saytda qalma müddətini artırmaq üçün tətbiq olunan ən son dizayn qaydaları və prinsipləri.',
            content='Blog məzmunu burada olacaq. Daha ətraflı məlumat üçün paneldən redaktə edin.',
            reading_time=5,
            views_count=120
        )
        url = "https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-4.0.3&w=800&q=80"
        response = urllib.request.urlopen(url)
        p.cover_image.save(f'dummy_blog_{i}.jpg', ContentFile(response.read()), save=False)
        p.save()
        p.tags.add(tag_ai, tag_web3)
        print(f"Created post {i}")
