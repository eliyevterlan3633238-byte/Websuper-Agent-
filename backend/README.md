# WebSuper Agency

WebSuper Agency, müştərilərə "wow" effekti yaşadan, müasir və premium dizayna malik, Django əsaslı korporativ agentlik saytıdır.

## 🌟 Əsas Xüsusiyyətlər

- **Müasir Dizayn**: Sarı-yaşıl gradient ilə Premium hiss (Dark/Light mode).
- **Parallax & Animasiyalar**: GSAP, ScrollTrigger və AOS istifadə edilərək hərəkətli səhifələr.
- **Hero Video Slider**: Mərkəzi səhifədə Swiper.js istifadə edərək video slaydlar.
- **5 Ayrı App**: Home, About, Portfolio, Blog, və Contact tətbiqləri.
- **Tam Responsiv**: Bütün cihazlarda (Mobile, Tablet, Laptop) mükəmməl görünüş. Mobile-da videoların avtomatik performans optimizasiyası.
- **Contact Form Validation**: Həm frontend (JS), həm də backend (Django Form) validasiyası, mesajların admin-də oxunub-oxunmamasını təqib etmək.
- **Genişləndirilə bilən Portfolio & Blog**: Admin-dən idarə olunan xüsusiyyətlər, case study formatında portfolio, `order` və `is_featured` filtrləri.

## 🛠 Texnoloji Stek

- **Backend**: Django 6, Python, SQLite (MVT arxitekturası)
- **Frontend**: HTML5 (semantik), CSS3 (CSS Variables, Flexbox/Grid), Vanilla JS
- **Kitabxanalar**: GSAP, AOS.js, Swiper.js, FontAwesome

## ⚙️ Quraşdırma (Local Development)

Aşağıdakı addımları izləyərək layihəni öz kompüterinizdə qura bilərsiniz.

1. **Repozitoriyanı klonlayın**:
   ```bash
   git clone <repo_url>
   cd websuper
   ```

2. **Virtual mühit yaradın və aktivləşdirin**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Asılılıqları yükləyin**:
   ```bash
   pip install django pillow
   ```

4. **Verilənlər bazasını (migrations) tətbiq edin**:
   ```bash
   python manage.py migrate
   ```

5. **Superuser yaradın (Admin panelinə giriş üçün)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Serveri başladın**:
   ```bash
   python manage.py runserver
   ```
   
Layihə `http://127.0.0.1:8000` ünvanında aktiv olacaq.

## 📈 Performans & Verification
- GSAP parallax və videolar yalnız desktop/laptop ölçülərində intensiv istifadə edilmişdir. Mobil cihazlarda performansı qorumaq üçün animasiyalar və videolar optimize edilmişdir (statik alternativlərlə əvəz oluna bilər).
- Bütün səhifələr üçün Lighthouse testləri keçirilmişdir. Asetlərin (şəkillər, videolar) ölçülərinə diqqət edilmişdir.

## 📜 Lisenziya
WebSuper Agency - Bütün hüquqlar qorunur.
