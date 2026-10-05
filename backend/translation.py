"""
Django Modeltranslation Konfiqurasiyasi
----------------------------------------
Qeyd: django-modeltranslation arxitekturasina esasen, her bir tetbiqin (app)
ozune aid 	ranslation.py fayli movcuddur ve modeltranslation terefinden avtomatik oxunur:

1. home/translation.py:
   - HeroContent: ('title', 'gradient_text', 'subtitle', 'button1_text', 'button2_text')
   - Service: ('title', 'description')
   - PricingPlan: ('name', 'description', 'features')
   - Stat: ('label',)
   - ShowcaseItem: ('title', 'description')
   - SiteSettings: ('address',)

2. about/translation.py:
   - TeamMember: ('name', 'role', 'bio', 'skills', 'projects')
   - Value: ('title', 'description')

3. portfolio/translation.py:
   - Category: ('name',)
   - Project: ('title', 'description', 'problem_statement', 'solution', 'result', 'client_quote')

4. blog/translation.py:
   - PostCategory: ('name',)
   - Tag: ('name',)
   - Post: ('title', 'excerpt', 'content')

Butun modeller ucun 'az', 'ru', 'en' dillerinde saheler yaradilmisdir ve TabbedTranslationAdmin vasitesile admin panelde tablar seklinde gosterilir.
"""
