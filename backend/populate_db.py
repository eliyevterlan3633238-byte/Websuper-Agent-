import os
import django
import random
from django.core.files.base import ContentFile
import urllib.request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from portfolio.models import Category, Project

# Create Category
cat, _ = Category.objects.get_or_create(name='Web Development', slug='web-development')

# Create 6 Projects
for i in range(1, 7):
    title = f'Layihə {i}'
    slug = f'layihe-{i}'
    
    if not Project.objects.filter(slug=slug).exists():
        p = Project(
            title=title,
            slug=slug,
            category=cat,
            client_name='Dummy Client',
            description='Bu kurs Front-End Web Proqramlaşdırmaya giriş üçün hazırlanmışdır və yeni başlayanlar üçün idealdır. Kurs tələbələrə müasir veb saytların və tətbiqlərin əsas strukturunu, dizayn prinsiplərini, interaktivlik və funksionallıq yaratmaq üçün lazım olan texnologiyaları öyrədir.\n\nTələbələr kurs boyunca HTML5, CSS3, SCSS, JavaScript, TypeScript və React ilə işləyərək tam funksional, estetik və responsive veb tətbiqlər yaratmağı öyrənəcəklər. Kurs praktiki yanaşmaya əsaslanır: hər dərs interaktiv tapşırıqlar, mini-layihələr və real dünya nümunələri ilə zənginləşdirilib.',
            technologies='HTML, CSS, JS, Django',
            problem_statement='',
            solution='',
            result=''
        )
        
        # Download a random dummy image
        url = "https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
        response = urllib.request.urlopen(url)
        p.cover_image.save(f'dummy_project_{i}.jpg', ContentFile(response.read()), save=False)
        p.save()
        print(f"Created {title}")
    else:
        print(f"Project {title} already exists")
