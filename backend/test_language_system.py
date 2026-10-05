import os
import sys
import django

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from django.test import Client
from django.utils import translation
from portfolio.models import Project, Category
from blog.models import Post, PostCategory
from home.models import HeroContent

client = Client(SERVER_NAME='localhost')

print("="*60)
print("1. TESTING DYNAMIC MODEL TRANSLATIONS")
print("="*60)

for lang in ['az', 'en', 'ru']:
    translation.activate(lang)
    h = HeroContent.load()
    p = Project.objects.first()
    post = Post.objects.first()
    print(f"\n[Language: {lang.upper()}]")
    print(f"  Hero Title: '{h.title}' | Gradient: '{h.gradient_text}'")
    print(f"  Project Title: '{p.title}' | Category: '{p.category.name}'")
    print(f"  Post Title: '{post.title}' | Category: '{post.category.name}'")
    
    assert p.title, f"Project title must not be empty for {lang}"
    assert post.title, f"Post title must not be empty for {lang}"
    assert h.title, f"Hero title must not be empty for {lang}"

print("\nAll dynamic model translation checks PASSED!")

print("\n" + "="*60)
print("2. TESTING STATIC TRANSLATIONS & RENDERED PAGES")
print("="*60)

# Check Home Page in all 3 languages
home_checks = {
    'az': ["Ana Səhifə", "Xidmətlərimiz", "İş Prosesimiz", "Qiymətlərimiz"],
    'en': ["Home", "Our Services", "Our Process", "Pricing Plans"],
    'ru': ["Главная", "Наши услуги", "Наш процесс", "Тарифные планы"]
}

for lang, phrases in home_checks.items():
    res = client.get(f'/{lang}/')
    assert res.status_code == 200, f"Failed GET /{lang}/"
    content = res.content.decode('utf-8')
    print(f"\n[GET /{lang}/ (Home)]")
    for phrase in phrases:
        found = phrase in content
        print(f"  Check '{phrase}': {'FOUND' if found else 'MISSING'}")
        assert found, f"Phrase '{phrase}' not found in /{lang}/"

# Check About Page
about_checks = {
    'az': ["Haqqımızda", "Hekayəmiz", "Dəyərlərimiz", "Komandamız"],
    'en': ["About Us", "Story", "Our Values", "Team"],
    'ru': ["О нас", "история", "Наши ценности", "Команда"]
}

for lang, phrases in about_checks.items():
    res = client.get(f'/{lang}/about/')
    assert res.status_code == 200, f"Failed GET /{lang}/about/"
    content = res.content.decode('utf-8')
    print(f"\n[GET /{lang}/about/]")
    for phrase in phrases:
        found = phrase in content
        print(f"  Check '{phrase}': {'FOUND' if found else 'MISSING'}")
        assert found, f"Phrase '{phrase}' not found in /{lang}/about/"

# Check Portfolio Page
portfolio_checks = {
    'az': ["Hamısı", "İşlər"],
    'en': ["All", "Works"],
    'ru': ["Все", "Работы"]
}

for lang, phrases in portfolio_checks.items():
    res = client.get(f'/{lang}/portfolio/')
    assert res.status_code == 200, f"Failed GET /{lang}/portfolio/"
    content = res.content.decode('utf-8')
    print(f"\n[GET /{lang}/portfolio/]")
    for phrase in phrases:
        found = phrase in content
        print(f"  Check '{phrase}': {'FOUND' if found else 'MISSING'}")
        assert found, f"Phrase '{phrase}' not found in /{lang}/portfolio/"

# Check Blog Page
blog_checks = {
    'az': ["Blog", "Oxu"],
    'en': ["Blog", "Read"],
    'ru': ["Блог", "Читать"]
}

for lang, phrases in blog_checks.items():
    res = client.get(f'/{lang}/blog/')
    assert res.status_code == 200, f"Failed GET /{lang}/blog/"
    content = res.content.decode('utf-8')
    print(f"\n[GET /{lang}/blog/]")
    for phrase in phrases:
        found = phrase in content
        print(f"  Check '{phrase}': {'FOUND' if found else 'MISSING'}")
        assert found, f"Phrase '{phrase}' not found in /{lang}/blog/"

# Check Contact Page & Form Placeholders
contact_checks = {
    'az': ["Bizimlə", "Əlaqə", "Mesaj Göndərin", 'placeholder="Adınız və Soyadınız"', 'placeholder="Email ünvanınız"'],
    'en': ["Get in", "Contact", "Send a Message", 'placeholder="Full Name"', 'placeholder="Email Address"'],
    'ru': ["Свяжитесь", "Контакты", "Отправьте сообщение", 'placeholder="Ваше имя и фамилия"', 'placeholder="Ваш адрес эл. почты"']
}

for lang, phrases in contact_checks.items():
    res = client.get(f'/{lang}/contact/')
    assert res.status_code == 200, f"Failed GET /{lang}/contact/"
    content = res.content.decode('utf-8')
    print(f"\n[GET /{lang}/contact/]")
    for phrase in phrases:
        found = phrase in content
        print(f"  Check '{phrase}': {'FOUND' if found else 'MISSING'}")
        assert found, f"Phrase '{phrase}' not found in /{lang}/contact/"

print("\n" + "="*60)
print("3. TESTING LANGUAGE SWITCHER REDIRECT (AZ -> EN -> RU -> AZ)")
print("="*60)

c_switch = Client(SERVER_NAME='localhost')
# Start on /az/about/
r1 = c_switch.get('/az/about/')
assert r1.status_code == 200

# Switch to EN
r2 = c_switch.post('/i18n/setlang/', {'language': 'en', 'next': '/az/about/'}, follow=True)
print(f"Switch AZ -> EN: Final URL = {r2.request['PATH_INFO']}")
assert r2.request['PATH_INFO'] == '/en/about/'

# Switch EN -> RU
r3 = c_switch.post('/i18n/setlang/', {'language': 'ru', 'next': '/en/about/'}, follow=True)
print(f"Switch EN -> RU: Final URL = {r3.request['PATH_INFO']}")
assert r3.request['PATH_INFO'] == '/ru/about/'

# Switch RU -> AZ
r4 = c_switch.post('/i18n/setlang/', {'language': 'az', 'next': '/ru/about/'}, follow=True)
print(f"Switch RU -> AZ: Final URL = {r4.request['PATH_INFO']}")
assert r4.request['PATH_INFO'] == '/az/about/'

print("Language switcher sequential redirects PASSED!")

print("\n" + "="*60)
print("ALL LANGUAGE & LOCALIZATION TESTS PASSED SUCCESSFULLY! 🚀")
print("="*60)

