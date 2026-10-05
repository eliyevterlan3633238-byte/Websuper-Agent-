import os

ru_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\ru\LC_MESSAGES\django.po'
en_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\en\LC_MESSAGES\django.po'

translations_ru = {
    'Tək Səhifəli (Landing) Dizayn': 'Одностраничный (Landing) Дизайн',
    'Mobil Responsivlik': 'Мобильная адаптивность',
    'Basic SEO Optimizasiyası': 'Базовая SEO-оптимизация',
    '1 Ay Ödənişsiz Dəstək': '1 месяц бесплатной поддержки',
    'Çoxsəhifəli Korporativ Sayt': 'Многостраничный корпоративный сайт',
    'CMS İnteqrasiyası (Admin Panel)': 'Интеграция CMS (Админ-панель)',
    'Sürət və SEO Optimizasiyası': 'Оптимизация скорости и SEO',
    '3 Ay Ödənişsiz Dəstək': '3 месяца бесплатной поддержки',
    'Xüsusi Animasiyalar (Parallax)': 'Специальные анимации (Parallax)',
    'E-ticarət və Kompleks Sistem': 'Электронная коммерция и комплексная система',
    'Xüsusi UI/UX Dizayn Araşdırması': 'Специальное UI/UX исследование',
    'Yüksək Təhlükəsizlik və Ödəniş İnteqrasiyası': 'Высокая безопасность и интеграция платежей',
    '6 Ay Ödənişsiz Dəstək': '6 месяцев бесплатной поддержки',
    'Tam API Dəstəyi': 'Полная поддержка API'
}

translations_en = {
    'Tək Səhifəli (Landing) Dizayn': 'Single Page (Landing) Design',
    'Mobil Responsivlik': 'Mobile Responsiveness',
    'Basic SEO Optimizasiyası': 'Basic SEO Optimization',
    '1 Ay Ödənişsiz Dəstək': '1 Month Free Support',
    'Çoxsəhifəli Korporativ Sayt': 'Multi-page Corporate Website',
    'CMS İnteqrasiyası (Admin Panel)': 'CMS Integration (Admin Panel)',
    'Sürət və SEO Optimizasiyası': 'Speed and SEO Optimization',
    '3 Ay Ödənişsiz Dəstək': '3 Months Free Support',
    'Xüsusi Animasiyalar (Parallax)': 'Special Animations (Parallax)',
    'E-ticarət və Kompleks Sistem': 'E-commerce and Complex System',
    'Xüsusi UI/UX Dizayn Araşdırması': 'Custom UI/UX Design Research',
    'Yüksək Təhlükəsizlik və Ödəniş İnteqrasiyası': 'High Security and Payment Integration',
    '6 Ay Ödənişsiz Dəstək': '6 Months Free Support',
    'Tam API Dəstəyi': 'Full API Support'
}

def append_translations(path, trans_dict):
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(path, 'a', encoding='utf-8') as f:
        for k, v in trans_dict.items():
            if f'msgid "{k}"' not in content:
                f.write(f'\n\nmsgid "{k}"\nmsgstr "{v}"\n')

append_translations(ru_path, translations_ru)
append_translations(en_path, translations_en)
print("Translations appended.")
