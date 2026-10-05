import os
import django
import sys

sys.path.append('c:/Users/Terlan/OneDrive/Desktop/sayt2/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from home.models import CtaBanner
cta = CtaBanner.objects.first()
with open('db_output.txt', 'w', encoding='utf-8') as f:
    if cta:
        f.write(f"Title AZ: '{cta.title_az}'\n")
        f.write(f"Title EN: '{cta.title_en}'\n")
        f.write(f"Subtitle AZ: '{cta.subtitle_az}'\n")
    else:
        f.write("No CTA object found.\n")
