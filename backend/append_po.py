import codecs
import os

az_po_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\az\LC_MESSAGES\django.po'
ru_po_path = r'c:\Users\Terlan\OneDrive\Desktop\sayt2\backend\locale\ru\LC_MESSAGES\django.po'

az_content = """
msgid "Privacy Policy"
msgstr "Məxfilik Siyasəti"

msgid "Last updated"
msgstr "Son yenilənmə"

msgid "Introduction"
msgstr "Giriş"

msgid "Welcome to WebSuper Agency. We respect your privacy and are committed to protecting your personal data. This privacy policy will inform you as to how we look after your personal data when you visit our website."
msgstr "WebSuper Agency-yə xoş gəlmisiniz. Biz sizin məxfiliyinizə hörmət edirik və şəxsi məlumatlarınızı qorumağa sadiqik. Bu məxfilik siyasəti vebsaytımıza daxil olduğunuz zaman şəxsi məlumatlarınıza necə baxdığımız barədə sizə məlumat verəcəkdir."

msgid "The data we collect about you"
msgstr "Sizin haqqınızda topladığımız məlumatlar"

msgid "We may collect, use, store and transfer different kinds of personal data about you, including Identity Data (first name, last name), Contact Data (email address, telephone numbers), and Technical Data (IP address, browser type and version)."
msgstr "Biz sizin haqqınızda Şəxsiyyət Məlumatları (ad, soyad), Əlaqə Məlumatları (e-poçt ünvanı, telefon nömrələri) və Texniki Məlumatlar (IP ünvanı, brauzer növü və versiyası) daxil olmaqla müxtəlif növ şəxsi məlumatları toplaya, istifadə edə, saxlaya və ötürə bilərik."

msgid "How we use your personal data"
msgstr "Şəxsi məlumatlarınızı necə istifadə edirik"

msgid "We will only use your personal data when the law allows us to. Most commonly, we will use your personal data to provide our services, to manage our relationship with you, or to improve our website."
msgstr "Şəxsi məlumatlarınızdan yalnız qanun icazə verdiyi hallarda istifadə edəcəyik. Ən çox, biz şəxsi məlumatlarınızdan xidmətlərimizi təmin etmək, sizinlə əlaqələrimizi idarə etmək və ya vebsaytımızı inkişaf etdirmək üçün istifadə edəcəyik."

msgid "Contact us"
msgstr "Bizimlə əlaqə"

msgid "If you have any questions about this privacy policy or our privacy practices, please contact us."
msgstr "Bu məxfilik siyasəti və ya məxfilik təcrübəmizlə bağlı hər hansı sualınız varsa, lütfən bizimlə əlaqə saxlayın."

msgid "Müasir veb həllər və innovativ dizaynlar."
msgstr "Müasir veb həllər və innovativ dizaynlar."

msgid "Biznesinizi rəqəmsal dünyada inkişaf etdirmək üçün peşəkar komandamızla ən son texnologiyalara əsaslanan kreativ həllər təqdim edirik."
msgstr "Biznesinizi rəqəmsal dünyada inkişaf etdirmək üçün peşəkar komandamızla ən son texnologiyalara əsaslanan kreativ həllər təqdim edirik."

msgid "Naviqasiya"
msgstr "Naviqasiya"

msgid "Xidmətlər"
msgstr "Xidmətlər"

msgid "Veb Tətbiqlər"
msgstr "Veb Tətbiqlər"

msgid "Mobil Tətbiqlər (iOS/Android)"
msgstr "Mobil Tətbiqlər (iOS/Android)"

msgid "UI/UX Dizayn"
msgstr "UI/UX Dizayn"

msgid "Korporativ Kimlik/Brendinq"
msgstr "Korporativ Kimlik/Brendinq"

msgid "SaaS Həlləri"
msgstr "SaaS Həlləri"

msgid "Əlaqə"
msgstr "Əlaqə"

msgid "Bütün hüquqlar qorunur."
msgstr "Bütün hüquqlar qorunur."
"""

ru_content = """
msgid "Privacy Policy"
msgstr "Политика конфиденциальности"

msgid "Last updated"
msgstr "Последнее обновление"

msgid "Introduction"
msgstr "Введение"

msgid "Welcome to WebSuper Agency. We respect your privacy and are committed to protecting your personal data. This privacy policy will inform you as to how we look after your personal data when you visit our website."
msgstr "Добро пожаловать в WebSuper Agency. Мы уважаем вашу конфиденциальность и обязуемся защищать ваши личные данные. Эта политика конфиденциальности сообщит вам о том, как мы заботимся о ваших личных данных при посещении нашего сайта."

msgid "The data we collect about you"
msgstr "Данные, которые мы собираем о вас"

msgid "We may collect, use, store and transfer different kinds of personal data about you, including Identity Data (first name, last name), Contact Data (email address, telephone numbers), and Technical Data (IP address, browser type and version)."
msgstr "Мы можем собирать, использовать, хранить и передавать различные виды ваших личных данных, включая идентификационные данные (имя, фамилия), контактные данные (адрес электронной почты, номера телефонов) и технические данные (IP-адрес, тип и версия браузера)."

msgid "How we use your personal data"
msgstr "Как мы используем ваши личные данные"

msgid "We will only use your personal data when the law allows us to. Most commonly, we will use your personal data to provide our services, to manage our relationship with you, or to improve our website."
msgstr "Мы будем использовать ваши личные данные только в тех случаях, когда это разрешено законом. Чаще всего мы будем использовать ваши личные данные для предоставления наших услуг, управления нашими отношениями с вами или улучшения нашего сайта."

msgid "Contact us"
msgstr "Свяжитесь с нами"

msgid "If you have any questions about this privacy policy or our privacy practices, please contact us."
msgstr "Если у вас есть какие-либо вопросы относительно этой политики конфиденциальности или нашей практики конфиденциальности, пожалуйста, свяжитесь с нами."

msgid "Müasir veb həllər və innovativ dizaynlar."
msgstr "Современные веб-решения и инновационный дизайн."

msgid "Biznesinizi rəqəmsal dünyada inkişaf etdirmək üçün peşəkar komandamızla ən son texnologiyalara əsaslanan kreativ həllər təqdim edirik."
msgstr "Мы предлагаем креативные решения на основе новейших технологий с нашей профессиональной командой для развития вашего бизнеса в цифровом мире."

msgid "Naviqasiya"
msgstr "Навигация"

msgid "Xidmətlər"
msgstr "Услуги"

msgid "Veb Tətbiqlər"
msgstr "Веб-приложения"

msgid "Mobil Tətbiqlər (iOS/Android)"
msgstr "Мобильные приложения (iOS/Android)"

msgid "UI/UX Dizayn"
msgstr "UI/UX Дизайн"

msgid "Korporativ Kimlik/Brendinq"
msgstr "Корпоративный стиль/Брендинг"

msgid "SaaS Həlləri"
msgstr "SaaS решения"

msgid "Əlaqə"
msgstr "Контакты"

msgid "Bütün hüquqlar qorunur."
msgstr "Все права защищены."
"""

if os.path.exists(az_po_path):
    with codecs.open(az_po_path, 'a', 'utf-8') as f:
        f.write(az_content)

if os.path.exists(ru_po_path):
    with codecs.open(ru_po_path, 'a', 'utf-8') as f:
        f.write(ru_content)
