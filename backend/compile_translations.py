import os
import sys
import polib

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')

TRANSLATIONS = {
    # Navbar & Common
    "Home": {
        "az": "Ana Səhifə",
        "en": "Home",
        "ru": "Главная"
    },
    "About": {
        "az": "Haqqımızda",
        "en": "About",
        "ru": "О нас"
    },
    "Portfolio": {
        "az": "Portfolio",
        "en": "Portfolio",
        "ru": "Портфолио"
    },
    "Blog": {
        "az": "Blog",
        "en": "Blog",
        "ru": "Блог"
    },
    "Contact": {
        "az": "Əlaqə",
        "en": "Contact",
        "ru": "Контакты"
    },
    "Müasir veb həllər və innovativ dizaynlar.": {
        "az": "Müasir veb həllər və innovativ dizaynlar.",
        "en": "Modern web solutions and innovative designs.",
        "ru": "Современные веб-решения и инновационный дизайн."
    },
    "Bütün hüquqlar qorunur.": {
        "az": "Bütün hüquqlar qorunur.",
        "en": "All rights reserved.",
        "ru": "Все права защищены."
    },
    "Dili dəyişdir": {
        "az": "Dili dəyişdir",
        "en": "Change Language",
        "ru": "Изменить язык"
    },

    # Titles & Headers
    "Ana Səhifə": {
        "az": "Ana Səhifə",
        "en": "Home",
        "ru": "Главная"
    },
    "Haqqımızda": {
        "az": "Haqqımızda",
        "en": "About Us",
        "ru": "О нас"
    },
    "Əlaqə": {
        "az": "Əlaqə",
        "en": "Contact",
        "ru": "Контакты"
    },
    "Bizimlə": {
        "az": "Bizimlə",
        "en": "Get in",
        "ru": "Свяжитесь"
    },
    "Bizi İfadə Edən": {
        "az": "Bizi İfadə Edən",
        "en": "Our Featured",
        "ru": "Наши"
    },
    "İşlər": {
        "az": "İşlər",
        "en": "Works",
        "ru": "Работы"
    },
    "Rəqəmsal": {
        "az": "Rəqəmsal",
        "en": "Digital",
        "ru": "Цифровой"
    },
    "Blog": {
        "az": "Blog",
        "en": "Blog",
        "ru": "Блог"
    },

    # Contact Page & Form
    "Telefon": {
        "az": "Telefon",
        "en": "Phone",
        "ru": "Телефон"
    },
    "Email": {
        "az": "Email",
        "en": "Email",
        "ru": "Эл. почта"
    },
    "Ünvan": {
        "az": "Ünvan",
        "en": "Address",
        "ru": "Адрес"
    },
    "Mesaj Göndərin": {
        "az": "Mesaj Göndərin",
        "en": "Send a Message",
        "ru": "Отправьте сообщение"
    },
    "Hər hansı bir sualınız və ya layihəniz varsa, bizə yazın.": {
        "az": "Hər hansı bir sualınız və ya layihəniz varsa, bizə yazın.",
        "en": "If you have any questions or projects, reach out to us.",
        "ru": "Если у вас есть вопросы или проект, напишите нам."
    },
    "Göndər": {
        "az": "Göndər",
        "en": "Send",
        "ru": "Отправить"
    },
    "Adınız və Soyadınız": {
        "az": "Adınız və Soyadınız",
        "en": "Full Name",
        "ru": "Ваше имя и фамилия"
    },
    "Email ünvanınız": {
        "az": "Email ünvanınız",
        "en": "Email Address",
        "ru": "Ваш адрес эл. почты"
    },
    "Telefon nömrəniz": {
        "az": "Telefon nömrəniz",
        "en": "Phone Number",
        "ru": "Номер телефона"
    },
    "Mövzu": {
        "az": "Mövzu",
        "en": "Subject",
        "ru": "Тема"
    },
    "Mesajınız": {
        "az": "Mesajınız",
        "en": "Your Message",
        "ru": "Ваше сообщение"
    },
    "Zəhmət olmasa, bütün mütləq sahələri doldurun.": {
        "az": "Zəhmət olmasa, bütün mütləq sahələri doldurun.",
        "en": "Please fill in all required fields.",
        "ru": "Пожалуйста, заполните все обязательные поля."
    },

    # About Page
    "Bizim": {
        "az": "Bizim",
        "en": "Our",
        "ru": "Наша"
    },
    "Hekayəmiz": {
        "az": "Hekayəmiz",
        "en": "Story",
        "ru": "История"
    },
    "WebSuper Agency olaraq biznesləri rəqəmsallaşdırmaq və onlara bazarda rəqabət üstünlüyü qazandırmaq məqsədilə fəaliyyətə başladıq. Biz sadəcə kod yazmırıq, istifadəçilərinizi heyran edəcək vizual təcrübələr və etibarlı həllər yaradırıq.": {
        "az": "WebSuper Agency olaraq biznesləri rəqəmsallaşdırmaq və onlara bazarda rəqabət üstünlüyü qazandırmaq məqsədilə fəaliyyətə başladıq. Biz sadəcə kod yazmırıq, istifadəçilərinizi heyran edəcək vizual təcrübələr və etibarlı həllər yaradırıq.",
        "en": "As WebSuper Agency, we started our mission to digitize businesses and give them a competitive market advantage. We craft immersive visual experiences and reliable software solutions that captivate your users.",
        "ru": "Как WebSuper Agency, мы начали свою деятельность с целью цифровизации бизнеса и предоставления конкурентных преимуществ. Мы не просто пишем код — мы создаем потрясающие визуальные впечатления и надежные решения."
    },
    "Missiyamız hər bir müştərinin brend dəyərini artırmaq və innovativ texnologiyalarla onlara dəstək olmaqdır.": {
        "az": "Missiyamız hər bir müştərinin brend dəyərini artırmaq və innovativ texnologiyalarla onlara dəstək olmaqdır.",
        "en": "Our mission is to enhance each client's brand value and empower them through cutting-edge technologies.",
        "ru": "Наша миссия — повышать ценность бренда каждого клиента и поддерживать его с помощью инновационных технологий."
    },
    "Dəyərlərimiz": {
        "az": "Dəyərlərimiz",
        "en": "Our Values",
        "ru": "Наши ценности"
    },
    "Bizi fərqləndirən əsas prinsiplər.": {
        "az": "Bizi fərqləndirən əsas prinsiplər.",
        "en": "Core principles that set us apart.",
        "ru": "Ключевые принципы, которые нас выделяют."
    },
    "İnnovasiya": {
        "az": "İnnovasiya",
        "en": "Innovation",
        "ru": "Инновации"
    },
    "Daim yeni texnologiyalar axtarır və tətbiq edirik.": {
        "az": "Daim yeni texnologiyalar axtarır və tətbiq edirik.",
        "en": "We continuously seek and implement modern technologies.",
        "ru": "Мы постоянно исследуем и внедряем новые технологии."
    },
    "Etibarlılıq": {
        "az": "Etibarlılıq",
        "en": "Reliability",
        "ru": "Надежность"
    },
    "Verdiyimiz sözlərin arxasında dayanırıq.": {
        "az": "Verdiyimiz sözlərin arxasında dayanırıq.",
        "en": "We firmly stand behind our commitments.",
        "ru": "Мы неизменно держим слово и выполняем обязательства."
    },
    "Keyfiyyət": {
        "az": "Keyfiyyət",
        "en": "Quality",
        "ru": "Качество"
    },
    "Hər detalda mükəmməlliyə can atırıq.": {
        "az": "Hər detalda mükəmməlliyə can atırıq.",
        "en": "We strive for excellence in every detail.",
        "ru": "Мы стремимся к совершенству в каждой детали."
    },
    "Peşəkar": {
        "az": "Peşəkar",
        "en": "Professional",
        "ru": "Профессиональная"
    },
    "Komandamız": {
        "az": "Komandamız",
        "en": "Team",
        "ru": "Команда"
    },
    "Layihələrinizi həyata keçirən istedadlı şəxslər.": {
        "az": "Layihələrinizi həyata keçirən istedadlı şəxslər.",
        "en": "Talented specialists turning your ideas into reality.",
        "ru": "Талантливые специалисты, воплощающие ваши проекты в жизнь."
    },
    "Təcrübə": {
        "az": "Təcrübə",
        "en": "Experience",
        "ru": "Опыт"
    },
    "Bacarıqlar": {
        "az": "Bacarıqlar",
        "en": "Skills",
        "ru": "Навыки"
    },
    "Layihələr": {
        "az": "Layihələr",
        "en": "Projects",
        "ru": "Проекты"
    },
    "il": {
        "az": "il",
        "en": "years",
        "ru": "лет"
    },
    "Məlumat yoxdur": {
        "az": "Məlumat yoxdur",
        "en": "No info",
        "ru": "Нет информации"
    },
    "Haqqında ətraflı məlumat yoxdur.": {
        "az": "Haqqında ətraflı məlumat yoxdur.",
        "en": "No detailed information available.",
        "ru": "Подробная информация отсутствует."
    },

    # Portfolio Page & Detail
    "Hamısı": {
        "az": "Hamısı",
        "en": "All",
        "ru": "Все"
    },
    "Bax": {
        "az": "Bax",
        "en": "View",
        "ru": "Смотреть"
    },
    "Ətraflı bax": {
        "az": "Ətraflı bax",
        "en": "View Details",
        "ru": "Подробнее"
    },
    "Layihə": {
        "az": "Layihə",
        "en": "Project",
        "ru": "Проект"
    },
    "Texnologiya": {
        "az": "Texnologiya",
        "en": "Technology",
        "ru": "Технологии"
    },
    "Tarix": {
        "az": "Tarix",
        "en": "Date",
        "ru": "Дата"
    },
    "Layihə Haqqında": {
        "az": "Layihə Haqqında",
        "en": "About Project",
        "ru": "О проекте"
    },
    "Layihə haqqında məlumat yoxdur.": {
        "az": "Layihə haqqında məlumat yoxdur.",
        "en": "No details available about this project.",
        "ru": "Информация о проекте отсутствует."
    },
    "Problem": {
        "az": "Problem",
        "en": "Problem",
        "ru": "Проблема"
    },
    "Həll Yolu": {
        "az": "Həll Yolu",
        "en": "Solution",
        "ru": "Решение"
    },

    # Blog Page & Detail
    "Oxu": {
        "az": "Oxu",
        "en": "Read",
        "ru": "Читать"
    },
    "Hələ heç bir blog əlavə olunmayıb": {
        "az": "Hələ heç bir blog əlavə olunmayıb",
        "en": "No blog posts yet",
        "ru": "Пока нет статей в блоге"
    },
    "Tezliklə yeni məqalələrimiz burada yer alacaq.": {
        "az": "Tezliklə yeni məqalələrimiz burada yer alacaq.",
        "en": "New articles will be published here soon.",
        "ru": "Скоро здесь появятся новые публикации."
    },
    "Əvvəlki": {
        "az": "Əvvəlki",
        "en": "Previous",
        "ru": "Предыдущая"
    },
    "Sonrakı": {
        "az": "Sonrakı",
        "en": "Next",
        "ru": "Следующая"
    },
    "Müəllif": {
        "az": "Müəllif",
        "en": "Author",
        "ru": "Автор"
    },
    "WebSuper Agency mütəxəssisi": {
        "az": "WebSuper Agency mütəxəssisi",
        "en": "WebSuper Agency Expert",
        "ru": "Специалист WebSuper Agency"
    },
    "Təsadüfi Bloglar": {
        "az": "Təsadüfi Bloglar",
        "en": "Recommended Posts",
        "ru": "Рекомендуемые статьи"
    },
    "Kateqoriyalar": {
        "az": "Kateqoriyalar",
        "en": "Categories",
        "ru": "Категории"
    },
    "Populyar Teqlər": {
        "az": "Populyar Teqlər",
        "en": "Popular Tags",
        "ru": "Популярные теги"
    },

    # Home Page
    "Hələ də veb saytınız yoxdur? Dayanmayın!": {
        "az": "Hələ də veb saytınız yoxdur? Dayanmayın!",
        "en": "Still don't have a website? Don't wait!",
        "ru": "Все еще нет веб-сайта? Не ждите!"
    },
    "Əlaqə Saxla": {
        "az": "Əlaqə Saxla",
        "en": "Get in Touch",
        "ru": "Связаться"
    },
    "Ətraflı Bax": {
        "az": "Ətraflı Bax",
        "en": "Learn More",
        "ru": "Подробнее"
    },
    "Müştəri": {
        "az": "Müştəri",
        "en": "Clients",
        "ru": "Клиентов"
    },
    "İl Təcrübə": {
        "az": "İl Təcrübə",
        "en": "Years Experience",
        "ru": "Лет опыта"
    },
    "Dəstək": {
        "az": "Dəstək",
        "en": "Support",
        "ru": "Поддержка"
    },
    "Xidmətlərimiz": {
        "az": "Xidmətlərimiz",
        "en": "Our Services",
        "ru": "Наши услуги"
    },
    "Biznesinizin inkişafı üçün tam əhatəli rəqəmsal həllər.": {
        "az": "Biznesinizin inkişafı üçün tam əhatəli rəqəmsal həllər.",
        "en": "Comprehensive digital solutions for your business growth.",
        "ru": "Комплексные цифровые решения для роста вашего бизнеса."
    },
    "Veb Development": {
        "az": "Veb Development",
        "en": "Web Development",
        "ru": "Веб-разработка"
    },
    "Müasir, sürətli və istifadəçi dostu veb saytların yaradılması.": {
        "az": "Müasir, sürətli və istifadəçi dostu veb saytların yaradılması.",
        "en": "Creation of modern, fast, and user-friendly websites.",
        "ru": "Создание современных, быстрых и удобных сайтов."
    },
    "Mobil Tətbiqlər": {
        "az": "Mobil Tətbiqlər",
        "en": "Mobile Applications",
        "ru": "Мобильные приложения"
    },
    "iOS və Android üçün nativ və çarpaz platformalı tətbiqlər.": {
        "az": "iOS və Android üçün nativ və çarpaz platformalı tətbiqlər.",
        "en": "Native and cross-platform mobile apps for iOS and Android.",
        "ru": "Нативные и кроссплатформенные приложения для iOS и Android."
    },
    "UI/UX Dizayn": {
        "az": "UI/UX Dizayn",
        "en": "UI/UX Design",
        "ru": "UI/UX Дизайн"
    },
    "Müştəriləri cəlb edən \"wow\" effektli, funksional dizaynlar.": {
        "az": "Müştəriləri cəlb edən \"wow\" effektli, funksional dizaynlar.",
        "en": "Stunning, functional designs with a 'wow' effect that attract customers.",
        "ru": "Функциональный дизайн с вау-эффектом, привлекающий клиентов."
    },
    "İş Prosesimiz": {
        "az": "İş Prosesimiz",
        "en": "Our Process",
        "ru": "Наш процесс"
    },
    "İdeyanızdan real məhsula gedən mükəmməl yol.": {
        "az": "İdeyanızdan real məhsula gedən mükəmməl yol.",
        "en": "A proven pathway from your concept to a tangible product.",
        "ru": "Идеальный путь от вашей идеи до реального продукта."
    },
    "Kəşfiyyat": {
        "az": "Kəşfiyyat",
        "en": "Discovery",
        "ru": "Исследование"
    },
    "Biznes ehtiyaclarınızı və hədəflərinizi öyrənirik.": {
        "az": "Biznes ehtiyaclarınızı və hədəflərinizi öyrənirik.",
        "en": "We analyze your business needs and objectives.",
        "ru": "Мы глубоко изучаем потребности и цели вашего бизнеса."
    },
    "Dizayn": {
        "az": "Dizayn",
        "en": "Design",
        "ru": "Дизайн"
    },
    "İstifadəçi təcrübəsini əsas alaraq interfeyslər yaradırıq.": {
        "az": "İstifadəçi təcrübəsini əsas alaraq interfeyslər yaradırıq.",
        "en": "We design intuitive interfaces centered on user experience.",
        "ru": "Создаем интуитивные интерфейсы с упором на опыт пользователей."
    },
    "Development": {
        "az": "Development",
        "en": "Development",
        "ru": "Разработка"
    },
    "Ən son texnologiyalarla kodlaşdırma prosesi aparılır.": {
        "az": "Ən son texnologiyalarla kodlaşdırma prosesi aparılır.",
        "en": "Clean and scalable coding using the latest technologies.",
        "ru": "Надежное программирование с использованием новейших технологий."
    },
    "Təhvil & Dəstək": {
        "az": "Təhvil & Dəstək",
        "en": "Delivery & Support",
        "ru": "Сдача и поддержка"
    },
    "Məhsulu təhvil verib daimi texniki dəstək göstəririk.": {
        "az": "Məhsulu təhvil verib daimi texniki dəstək göstəririk.",
        "en": "We launch the product and provide continuous technical support.",
        "ru": "Запускаем продукт и обеспечиваем круглосуточную поддержку."
    },
    "Son Yazılarımız": {
        "az": "Son Yazılarımız",
        "en": "Recent Articles",
        "ru": "Последние статьи"
    },
    "Blogumuzdan sənaye xəbərləri və faydalı məlumatlar.": {
        "az": "Blogumuzdan sənaye xəbərləri və faydalı məlumatlar.",
        "en": "Industry insights and valuable tips from our blog.",
        "ru": "Новости индустрии и полезные статьи из нашего блога."
    },
    "Veb saytlarda animasiyanın rolu": {
        "az": "Veb saytlarda animasiyanın rolu",
        "en": "The Role of Animation in Modern Websites",
        "ru": "Роль анимации в современных веб-сайтах"
    },
    "2026-cı ilin UI/UX trendləri": {
        "az": "2026-cı ilin UI/UX trendləri",
        "en": "Top UI/UX Trends for 2026",
        "ru": "Главные тренды UI/UX 2026 года"
    },
    "Django ilə təhlükəsizlik qaydaları": {
        "az": "Django ilə təhlükəsizlik qaydaları",
        "en": "Security Best Practices with Django",
        "ru": "Правила безопасности веб-приложений на Django"
    },
    "Qiymətlərimiz": {
        "az": "Qiymətlərimiz",
        "en": "Pricing Plans",
        "ru": "Тарифные планы"
    },
    "Ehtiyaclarınıza və büdcənizə uyğun ideal paketi seçin.": {
        "az": "Ehtiyaclarınıza və büdcənizə uyğun ideal paketi seçin.",
        "en": "Choose the optimal plan tailored to your needs and budget.",
        "ru": "Выберите идеальный пакет в соответствии с вашими потребностями."
    },
    "Ən Populyar": {
        "az": "Ən Populyar",
        "en": "Most Popular",
        "ru": "Самый популярный"
    },
    "Sifariş Ver": {
        "az": "Sifariş Ver",
        "en": "Order Now",
        "ru": "Заказать"
    },
    "Başlanğıc": {
        "az": "Başlanğıc",
        "en": "Starter",
        "ru": "Стартовый"
    },
    "AZN-dən": {
        "az": "AZN-dən",
        "en": "from AZN",
        "ru": "от AZN"
    },
    "Kiçik bizneslər və startaplar üçün ideal seçim.": {
        "az": "Kiçik bizneslər və startaplar üçün ideal seçim.",
        "en": "Ideal choice for small businesses and startups.",
        "ru": "Идеальный выбор для малого бизнеса и стартапов."
    },
    "Standart": {
        "az": "Standart",
        "en": "Standard",
        "ru": "Стандартный"
    },
    "Korporativ şirkətlər üçün tam funksional həll.": {
        "az": "Korporativ şirkətlər üçün tam funksional həll.",
        "en": "Fully functional solution for corporate companies.",
        "ru": "Полнофункциональное решение для корпоративных компаний."
    },
    "Premium": {
        "az": "Premium",
        "en": "Premium",
        "ru": "Премиум"
    },
    "Genişmiqyaslı və xüsusi e-ticarət/platforma həlləri.": {
        "az": "Genişmiqyaslı və xüsusi e-ticarət/platforma həlləri.",
        "en": "Large-scale e-commerce and custom digital platform solutions.",
        "ru": "Масштабные решения для электронной коммерции и сложных платформ."
    },
    "Layihənizi Bu Gün Başladaq": {
        "az": "Layihənizi Bu Gün Başladaq",
        "en": "Let's Launch Your Project Today",
        "ru": "Начнем ваш проект сегодня"
    },
    "Peşəkar komandamızla birlikdə biznesinizi rəqəmsal zirvəyə qaldırın.": {
        "az": "Peşəkar komandamızla birlikdə biznesinizi rəqəmsal zirvəyə qaldırın.",
        "en": "Elevate your brand to the digital summit with our expert team.",
        "ru": "Поднимите свой бизнес на цифровую вершину вместе с нашей командой."
    },
    "Bizimlə Əlaqə": {
        "az": "Bizimlə Əlaqə",
        "en": "Contact Us",
        "ru": "Связаться с нами"
    },

    # Privacy Policy Page
    "Privacy Policy": {
        "az": "Məxfilik Siyasəti",
        "en": "Privacy Policy",
        "ru": "Политика конфиденциальности"
    },
    "Last updated": {
        "az": "Son yenilənmə",
        "en": "Last updated",
        "ru": "Последнее обновление"
    },
    "Introduction": {
        "az": "Giriş",
        "en": "Introduction",
        "ru": "Введение"
    },
    "Welcome to WebSuper Agency. We respect your privacy and are committed to protecting your personal data. This privacy policy will inform you as to how we look after your personal data when you visit our website.": {
        "az": "WebSuper Agency-yə xoş gəlmisiniz. Biz sizin məxfiliyinizə hörmət edirik və şəxsi məlumatlarınızı qorumağa sadiqik. Bu məxfilik siyasəti vebsaytımıza daxil olduğunuz zaman şəxsi məlumatlarınıza necə baxdığımız barədə sizə məlumat verəcəkdir.",
        "en": "Welcome to WebSuper Agency. We respect your privacy and are committed to protecting your personal data. This privacy policy will inform you as to how we look after your personal data when you visit our website.",
        "ru": "Добро пожаловать в WebSuper Agency. Мы уважаем вашу конфиденциальность и обязуемся защищать ваши личные данные. Эта политика конфиденциальности сообщит вам о том, как мы заботимся о ваших личных данных при посещении нашего сайта."
    },
    "The data we collect about you": {
        "az": "Sizin haqqınızda topladığımız məlumatlar",
        "en": "The data we collect about you",
        "ru": "Данные, которые мы собираем о вас"
    },
    "We may collect, use, store and transfer different kinds of personal data about you, including Identity Data (first name, last name), Contact Data (email address, telephone numbers), and Technical Data (IP address, browser type and version).": {
        "az": "Biz sizin haqqınızda Şəxsiyyət Məlumatları (ad, soyad), Əlaqə Məlumatları (e-poçt ünvanı, telefon nömrələri) və Texniki Məlumatlar (IP ünvanı, brauzer növü və versiyası) daxil olmaqla müxtəlif növ şəxsi məlumatları toplaya, istifadə edə, saxlaya və ötürə bilərik.",
        "en": "We may collect, use, store and transfer different kinds of personal data about you, including Identity Data (first name, last name), Contact Data (email address, telephone numbers), and Technical Data (IP address, browser type and version).",
        "ru": "Мы можем собирать, использовать, хранить и передавать различные виды ваших личных данных, включая идентификационные данные (имя, фамилия), контактные данные (адрес электронной почты, номера телефонов) и технические данные (IP-адрес, тип и версия браузера)."
    },
    "How we use your personal data": {
        "az": "Şəxsi məlumatlarınızı necə istifadə edirik",
        "en": "How we use your personal data",
        "ru": "Как мы используем ваши личные данные"
    },
    "We will only use your personal data when the law allows us to. Most commonly, we will use your personal data to provide our services, to manage our relationship with you, or to improve our website.": {
        "az": "Şəxsi məlumatlarınızdan yalnız qanun icazə verdiyi hallarda istifadə edəcəyik. Ən çox, biz şəxsi məlumatlarınızdan xidmətlərimizi təmin etmək, sizinlə əlaqələrimizi idarə etmək və ya vebsaytımızı inkişaf etdirmək üçün istifadə edəcəyik.",
        "en": "We will only use your personal data when the law allows us to. Most commonly, we will use your personal data to provide our services, to manage our relationship with you, or to improve our website.",
        "ru": "Мы будем использовать ваши личные данные только в тех случаях, когда это разрешено законом. Чаще всего мы будем использовать ваши личные данные для предоставления наших услуг, управления нашими отношениями с вами или улучшения нашего сайта."
    },
    "Contact us": {
        "az": "Bizimlə əlaqə",
        "en": "Contact us",
        "ru": "Свяжитесь с нами"
    },
    "If you have any questions about this privacy policy or our privacy practices, please contact us.": {
        "az": "Bu məxfilik siyasəti və ya məxfilik təcrübəmizlə bağlı hər hansı sualınız varsa, lütfən bizimlə əlaqə saxlayın.",
        "en": "If you have any questions about this privacy policy or our privacy practices, please contact us.",
        "ru": "Если у вас есть какие-либо вопросы относительно этой политики конфиденциальности или нашей практики конфиденциальности, пожалуйста, свяжитесь с нами."
    },

    # Footer additions
    "Biznesinizi rəqəmsal dünyada inkişaf etdirmək üçün peşəkar komandamızla ən son texnologiyalara əsaslanan kreativ həllər təqdim edirik.": {
        "az": "Biznesinizi rəqəmsal dünyada inkişaf etdirmək üçün peşəkar komandamızla ən son texnologiyalara əsaslanan kreativ həllər təqdim edirik.",
        "en": "We offer creative solutions based on the latest technologies with our professional team to grow your business in the digital world.",
        "ru": "Мы предлагаем креативные решения на основе новейших технологий с нашей профессиональной командой для развития вашего бизнеса в цифровом мире."
    },
    "Naviqasiya": {
        "az": "Naviqasiya",
        "en": "Navigation",
        "ru": "Навигация"
    },
    "Xidmətlər": {
        "az": "Xidmətlər",
        "en": "Services",
        "ru": "Услуги"
    },
    "Veb Tətbiqlər": {
        "az": "Veb Tətbiqlər",
        "en": "Web Applications",
        "ru": "Веб-приложения"
    },
    "Mobil Tətbiqlər (iOS/Android)": {
        "az": "Mobil Tətbiqlər (iOS/Android)",
        "en": "Mobile Apps (iOS/Android)",
        "ru": "Мобильные приложения (iOS/Android)"
    },
    "UI/UX Dizayn": {
        "az": "UI/UX Dizayn",
        "en": "UI/UX Design",
        "ru": "UI/UX Дизайн"
    },
    "Korporativ Kimlik/Brendinq": {
        "az": "Korporativ Kimlik/Brendinq",
        "en": "Corporate Identity/Branding",
        "ru": "Корпоративный стиль/Брендинг"
    },
    "SaaS Həlləri": {
        "az": "SaaS Həlləri",
        "en": "SaaS Solutions",
        "ru": "SaaS решения"
    },

    # Django Admin Apps & Models Verbose Names
    "Əsas Hero Başlığı": {
        "az": "Əsas Hero Başlığı",
        "en": "Main Hero Header",
        "ru": "Главный заголовок Hero"
    },
    "Ana Səhifə Hero Bölməsi": {
        "az": "Ana Səhifə Hero Bölməsi",
        "en": "Home Hero Section",
        "ru": "Раздел Hero главной страницы"
    },
    "Xidmət": {
        "az": "Xidmət",
        "en": "Service",
        "ru": "Услуга"
    },
    "Xidmətlərimiz Bölməsi (3 Əsas Kart)": {
        "az": "Xidmətlərimiz Bölməsi (3 Əsas Kart)",
        "en": "Our Services Section (3 Main Cards)",
        "ru": "Раздел 'Наши услуги' (3 основные карточки)"
    },
    "İş Prosesi Mərhələsi": {
        "az": "İş Prosesi Mərhələsi",
        "en": "Work Process Step",
        "ru": "Этап рабочего процесса"
    },
    "İş Prosesimiz Mərhələləri (1, 2, 3, 4)": {
        "az": "İş Prosesimiz Mərhələləri (1, 2, 3, 4)",
        "en": "Our Work Process Steps (1, 2, 3, 4)",
        "ru": "Этапы рабочего процесса (1, 2, 3, 4)"
    },
    "Son CTA Bölməsi": {
        "az": "Son CTA Bölməsi",
        "en": "Final CTA Section",
        "ru": "Финальный раздел CTA"
    },
    "Son CTA Bölməsi (Layihənizi Başladaq)": {
        "az": "Son CTA Bölməsi (Layihənizi Başladaq)",
        "en": "Final CTA Section (Let's Start Your Project)",
        "ru": "Финальный раздел CTA (Начнем ваш проект)"
    },
    "Qiymət Paketi": {
        "az": "Qiymət Paketi",
        "en": "Pricing Plan",
        "ru": "Тарифный план"
    },
    "Qiymət Paketləri (Tariflər)": {
        "az": "Qiymət Paketləri (Tariflər)",
        "en": "Pricing Plans (Tariffs)",
        "ru": "Тарифные планы (Цены)"
    },
    "Statistika Rəqəmi": {
        "az": "Statistika Rəqəmi",
        "en": "Statistic Number",
        "ru": "Показатель статистики"
    },
    "Statistika Bloku (150+, 50+ və s.)": {
        "az": "Statistika Bloku (150+, 50+ və s.)",
        "en": "Statistics Block (150+, 50+, etc.)",
        "ru": "Блок статистики (150+, 50+ и др.)"
    },
    "Ana Səhifə Slaydı": {
        "az": "Ana Səhifə Slaydı",
        "en": "Home Page Slide",
        "ru": "Слайд главной страницы"
    },
    "Ana Səhifə Slayderi": {
        "az": "Ana Səhifə Slayderi",
        "en": "Home Page Slider",
        "ru": "Слайдер главной страницы"
    },
    "Sayt Əlaqə & Sosial Media Tənzimləmələri": {
        "az": "Sayt Əlaqə & Sosial Media Tənzimləmələri",
        "en": "Site Contact & Social Media Settings",
        "ru": "Настройки контактов и соцсетей сайта"
    },
    "Sayt Ümumi Tənzimləmələri": {
        "az": "Sayt Ümumi Tənzimləmələri",
        "en": "General Site Settings",
        "ru": "Общие настройки сайта"
    },
    "Haqqımızda Məzmunu": {
        "az": "Haqqımızda Məzmunu",
        "en": "About Us Content",
        "ru": "Содержимое 'О нас'"
    },
    "Haqqımızda Bölməsi": {
        "az": "Haqqımızda Bölməsi",
        "en": "About Us Section",
        "ru": "Раздел 'О нас'"
    },
    "Komanda Üzvü": {
        "az": "Komanda Üzvü",
        "en": "Team Member",
        "ru": "Член команды"
    },
    "Komanda Üzvləri (Haqqımızda/Ana Səhifə)": {
        "az": "Komanda Üzvləri (Haqqımızda/Ana Səhifə)",
        "en": "Team Members (About/Home)",
        "ru": "Члены команды (О нас/Главная)"
    },
    "Dəyər": {
        "az": "Dəyər",
        "en": "Value",
        "ru": "Ценность"
    },
    "Dəyərlərimiz (Haqqımızda)": {
        "az": "Dəyərlərimiz (Haqqımızda)",
        "en": "Our Values (About Us)",
        "ru": "Наши ценности (О нас)"
    },
    "Layihə Kateqoriyası": {
        "az": "Layihə Kateqoriyası",
        "en": "Project Category",
        "ru": "Категория проекта"
    },
    "Layihə Kateqoriyaları": {
        "az": "Layihə Kateqoriyaları",
        "en": "Project Categories",
        "ru": "Категории проектов"
    },
    "Portfolio Layihəsi": {
        "az": "Portfolio Layihəsi",
        "en": "Portfolio Project",
        "ru": "Проект портфолио"
    },
    "Portfolio Layihələri": {
        "az": "Portfolio Layihələri",
        "en": "Portfolio Projects",
        "ru": "Проекты портфолио"
    },
    "Layihə Qalereya Şəkili": {
        "az": "Layihə Qalereya Şəkili",
        "en": "Project Gallery Image",
        "ru": "Изображение галереи проекта"
    },
    "Layihə Qalereyası Şəkilləri": {
        "az": "Layihə Qalereyası Şəkilləri",
        "en": "Project Gallery Images",
        "ru": "Изображения галереи проекта"
    },
    "Məqalə Kateqoriyası": {
        "az": "Məqalə Kateqoriyası",
        "en": "Article Category",
        "ru": "Категория статьи"
    },
    "Məqalə Kateqoriyaları": {
        "az": "Məqalə Kateqoriyaları",
        "en": "Article Categories",
        "ru": "Категории статей"
    },
    "Teq": {
        "az": "Teq",
        "en": "Tag",
        "ru": "Тег"
    },
    "Teqlər": {
        "az": "Teqlər",
        "en": "Tags",
        "ru": "Теги"
    },
    "Məqalə": {
        "az": "Məqalə",
        "en": "Article",
        "ru": "Статья"
    },
    "Blog Məqalələri": {
        "az": "Blog Məqalələri",
        "en": "Blog Articles",
        "ru": "Статьи блога"
    },
    "Gələn Mesaj": {
        "az": "Gələn Mesaj",
        "en": "Incoming Message",
        "ru": "Входящее сообщение"
    },
    "Gələn Mesajlar (Əlaqə Formu)": {
        "az": "Gələn Mesajlar (Əlaqə Formu)",
        "en": "Incoming Messages (Contact Form)",
        "ru": "Входящие сообщения (Форма связи)"
    },
    "Ümumi Əlaqə": {
        "az": "Ümumi Əlaqə",
        "en": "General Contact",
        "ru": "Общие контакты"
    },
    "Sosial Şəbəkələr (Header & Footer)": {
        "az": "Sosial Şəbəkələr (Header & Footer)",
        "en": "Social Networks (Header & Footer)",
        "ru": "Социальные сети (Шапка и подвал)"
    },
    "Arxa Fon Şəkilləri (Hero Bölməsi)": {
        "az": "Arxa Fon Şəkilləri (Hero Bölməsi)",
        "en": "Background Images (Hero Section)",
        "ru": "Фоновые изображения (Раздел Hero)"
    },
    "Ana Səhifə Arxa Fon Şəkilləri": {
        "az": "Ana Səhifə Arxa Fon Şəkilləri",
        "en": "Home Page Background Images",
        "ru": "Фоновые изображения главной страницы"
    },
    "Müştəri Məlumatları": {
        "az": "Müştəri Məlumatları",
        "en": "Customer Information",
        "ru": "Информация о клиенте"
    },
    "Mesajın Məzmunu": {
        "az": "Mesajın Məzmunu",
        "en": "Message Content",
        "ru": "Содержимое сообщения"
    },
    "Status və Tarix": {
        "az": "Status və Tarix",
        "en": "Status and Date",
        "ru": "Статус и дата"
    },
    "Müraciət göndərən şəxsin əlaqə vasitələri": {
        "az": "Müraciət göndərən şəxsin əlaqə vasitələri",
        "en": "Contact details of the applicant",
        "ru": "Контактные данные отправителя"
    },
    "Göndərilən müraciət mövzusu və ətraflı mətn": {
        "az": "Göndərilən müraciət mövzusu və ətraflı mətn",
        "en": "Submitted inquiry subject and detailed text",
        "ru": "Тема обращения и подробный текст"
    },
    "Mesajın oxunma vəziyyəti və qəbul edilmə vaxtı": {
        "az": "Mesajın oxunma vəziyyəti və qəbul edilmə vaxtı",
        "en": "Message read status and reception time",
        "ru": "Статус прочтения и время получения"
    }
}

LANGUAGES = ['az', 'en', 'ru']

for lang in LANGUAGES:
    lang_dir = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES')
    os.makedirs(lang_dir, exist_ok=True)
    po_path = os.path.join(lang_dir, 'django.po')
    mo_path = os.path.join(lang_dir, 'django.mo')
    
    # Create or load PO file
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': 'WebSuper 1.0',
        'Report-Msgid-Bugs-To': '',
        'POT-Creation-Date': '2026-09-22 00:00+0400',
        'PO-Revision-Date': '2026-09-22 00:00+0400',
        'Last-Translator': 'Antigravity <info@websuper.az>',
        'Language-Team': lang,
        'Language': lang,
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Transfer-Encoding': '8bit',
    }
    
    for msgid, translations in TRANSLATIONS.items():
        msgstr = translations.get(lang, msgid)
        entry = polib.POEntry(
            msgid=msgid,
            msgstr=msgstr
        )
        po.append(entry)
        
    po.save(po_path)
    po.save_as_mofile(mo_path)
    print(f"[{lang}] Compiled {len(po)} entries -> {mo_path} (exists: {os.path.exists(mo_path)}, size: {os.path.getsize(mo_path)} bytes)")

print("\n=== All translation catalogs compiled successfully! ===")
