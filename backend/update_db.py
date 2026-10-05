import os
import django
import sys

sys.path.append('c:/Users/Terlan/OneDrive/Desktop/sayt2/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from home.models import CtaBanner
cta = CtaBanner.objects.first()
if cta:
    # Update English translations
    cta.title_en = "Let's Launch Your Project Today"
    cta.subtitle_en = "Elevate your brand to the digital summit with our expert team."
    cta.button_text_en = "Contact Us"
    
    # Update Russian translations
    cta.title_ru = "Давайте Запустим Ваш Проект Сегодня"
    cta.subtitle_ru = "Поднимите свой бизнес на цифровую вершину вместе с нашей профессиональной командой."
    cta.button_text_ru = "Связаться с нами"
    
    cta.save()
    print("Database updated successfully.")
