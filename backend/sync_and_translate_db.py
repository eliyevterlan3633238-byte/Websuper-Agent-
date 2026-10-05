import os
import sys
import django

# Set up Django environment
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from portfolio.models import Category, Project
from blog.models import PostCategory, Post
from home.models import HeroContent, SiteSettings

print("=== 1. Syncing & Translating Categories ===")
for cat in Category.objects.all():
    name = cat.name or 'Web Development'
    cat.name_az = 'Veb İnkişaf' if 'Web' in name else name
    cat.name_en = 'Web Development'
    cat.name_ru = 'Веб-разработка'
    cat.save()
    print(f"Category: AZ={cat.name_az}, EN={cat.name_en}, RU={cat.name_ru}")

print("\n=== 2. Syncing & Translating Projects ===")
for p in Project.objects.all():
    # Use existing title or fallback
    orig_title = p.title or f"Layihə {p.id}"
    num = p.id
    
    p.title_az = f"Layihə {num}"
    p.title_en = f"Project {num}"
    p.title_ru = f"Проект {num}"
    
    p.description_az = (
        "Bu layihə müasir veb texnologiyaları əsasında hazırlanmışdır. "
        "Yüksək performans, zərif dizayn və istifadəçi rahatlığı təmin edir."
    )
    p.description_en = (
        "This project is developed using cutting-edge web technologies. "
        "It provides high performance, elegant design, and seamless user experience."
    )
    p.description_ru = (
        "Этот проект разработан на основе современных веб-технологий. "
        "Он обеспечивает высокую производительность, элегантный дизайн и удобство использования."
    )
    
    p.problem_statement_az = "Müştərinin köhnəlmiş veb platforması yüksək trafikə tab gətirə bilmirdi və mobildə zəif işləyirdi."
    p.problem_statement_en = "The client's legacy web platform could not handle high traffic and performed poorly on mobile."
    p.problem_statement_ru = "Устаревшая веб-платформа клиента не справлялась с высоким трафиком и плохо работала на мобильных устройствах."
    
    p.solution_az = "Müasir arxitektura və responsiv dizaynla tam yenidən quruldu."
    p.solution_en = "Completely rebuilt with modern architecture and fully responsive design."
    p.solution_ru = "Полностью перестроен с использованием современной архитектуры и адаптивного дизайна."
    
    p.result_az = "Yüklənmə sürəti 3 dəfə artdı, müştəri məmnuniyyəti yüksəldi."
    p.result_en = "Load speed tripled and customer satisfaction significantly increased."
    p.result_ru = "Скорость загрузки выросла в 3 раза, а удовлетворенность клиентов значительно увеличилась."
    
    p.client_quote_az = "WebSuper komandası işimizi tamamilə dəyişdi. Nəticədən çox razıyıq!"
    p.client_quote_en = "The WebSuper team completely transformed our digital presence. Highly recommended!"
    p.client_quote_ru = "Команда WebSuper полностью преобразила наш бизнес в интернете. Очень довольны результатом!"
    
    p.save()
    print(f"Project #{p.id}: AZ='{p.title_az}', EN='{p.title_en}', RU='{p.title_ru}'")

print("\n=== 3. Syncing & Translating Blog Categories ===")
for bcat in PostCategory.objects.all():
    bcat.name_az = "Texnologiya"
    bcat.name_en = "Technology"
    bcat.name_ru = "Технологии"
    bcat.save()
    print(f"Blog Category: AZ={bcat.name_az}, EN={bcat.name_en}, RU={bcat.name_ru}")

print("\n=== 4. Syncing & Translating Blog Posts ===")
for post in Post.objects.all():
    num = post.id
    post.title_az = f"Müasir Veb Dizayn Trendləri {num}"
    post.title_en = f"Modern Web Design Trends {num}"
    post.title_ru = f"Современные тренды веб-дизайна {num}"
    
    post.excerpt_az = "İstifadəçilərin saytda qalma müddətini artırmaq üçün tətbiq olunan ən son dizayn qaydaları və prinsipləri."
    post.excerpt_en = "Latest design principles and best practices applied to boost user engagement and retention on your website."
    post.excerpt_ru = "Новейшие принципы и правила дизайна для увеличения времени взаимодействия пользователей с сайтом."
    
    content_az = (
        "<p>Blog məzmunu burada başlayır. Veb dizayn daim inkişaf edir və yeni trendlər yaranır. "
        "İstifadəçilərin diqqətini cəlb etmək üçün bu trendləri izləmək mütləqdir.</p>"
        "<p>Müasir interfeyslər təmizlik və minimalizm üzərində qurulur. Əlavə olaraq, süni intellektin dizayn prosesinə inteqrasiyası işimizi daha da asanlaşdırır.</p>"
    )
    content_en = (
        "<p>The blog content starts here. Web design is constantly evolving with emerging trends. "
        "Staying updated with these trends is vital to capture your audience's attention.</p>"
        "<p>Modern interfaces are built on simplicity, clarity, and minimalism. Integrating AI into design workflows enhances efficiency even further.</p>"
    )
    content_ru = (
        "<p>Содержание блога начинается здесь. Веб-дизайн постоянно развивается и появляются новые тренды. "
        "Следовать этим трендам необходимо для привлечения внимания пользователей.</p>"
        "<p>Современные интерфейсы строятся на принципах чистоты и минимализма. Интеграция искусственного интеллекта делает рабочий процесс еще эффективнее.</p>"
    )
    
    post.content_az = content_az
    post.content_en = content_en
    post.content_ru = content_ru
    post.save()
    print(f"Blog Post #{post.id}: AZ='{post.title_az}', EN='{post.title_en}', RU='{post.title_ru}'")

print("\n=== 5. Syncing & Translating HeroContent ===")
hero = HeroContent.load()
hero.title_az = "Rəqəmsal Dünyada"
hero.gradient_text_az = "İz Buraxın"
hero.subtitle_az = "Müasir texnologiyalar və innovativ dizaynla biznesinizi inkişaf etdiririk. Sizin uğurunuz, bizim prioritetimizdir."
hero.button1_text_az = "Layihəyə Başla"
hero.button2_text_az = "Portfolioya Bax"

hero.title_en = "In the Digital World"
hero.gradient_text_en = "Leave Your Mark"
hero.subtitle_en = "We grow your business with modern technologies and innovative design. Your success is our top priority."
hero.button1_text_en = "Start a Project"
hero.button2_text_en = "View Portfolio"

hero.title_ru = "В цифровом мире"
hero.gradient_text_ru = "Оставьте свой след"
hero.subtitle_ru = "Мы развиваем ваш бизнес с помощью передовых технологий и инновационного дизайна. Ваш успех — наш приоритет."
hero.button1_text_ru = "Начать проект"
hero.button2_text_ru = "Смотреть портфолио"
hero.save()
print("HeroContent updated with distinct AZ, EN, and RU texts.")

print("\n=== 6. Syncing & Translating SiteSettings ===")
settings_obj = SiteSettings.load()
settings_obj.address_az = "Bakı şəhəri, Azərbaycan"
settings_obj.address_en = "Baku city, Azerbaijan"
settings_obj.address_ru = "г. Баку, Азербайджан"
settings_obj.save()
print("SiteSettings updated.")

print("\n=== ALL TRANSLATION DATA SYNCED SUCCESSFULLY! ===")
