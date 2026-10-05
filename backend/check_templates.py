import os
import django
from django.template import Template, Engine
from django.conf import settings
from django.template.utils import get_app_template_dirs

# Ensure settings are configured (minimal for template checking)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

errors = []
engine = Engine.get_default()

template_dirs = []
for engine in django.template.engines.all():
    template_dirs.extend(engine.template_dirs)
    # Add app template dirs
    try:
        from django.template.utils import get_app_template_dirs
        template_dirs.extend(get_app_template_dirs('templates'))
    except Exception:
        pass

# Deduplicate
template_dirs = list(set(template_dirs))

for t_dir in template_dirs:
    for root, dirs, files in os.walk(t_dir):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        source = f.read()
                    # Try to create a Template object, which parses it
                    Template(source)
                except Exception as e:
                    errors.append(f"{path}: {e}")

if errors:
    print("Found template errors:")
    for err in errors:
        print(err)
    exit(1)
else:
    print("All templates compiled successfully.")
    exit(0)
