import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websuper.settings')
django.setup()

from blog.models import Post

html_content = '''
<p>Blog məzmunu burada başlayır. Veb dizayn daim inkişaf edir və yeni trendlər yaranır. İstifadəçilərin diqqətini cəlb etmək üçün bu trendləri izləmək mütləqdir.</p>
<img src="https://images.unsplash.com/photo-1542744094-3a31f272c490?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Dizayn" style="width: 100%; height: auto; border-radius: 10px; margin: 20px 0;">
<p>Yuxarıdakı şəkildə gördüyünüz kimi, müasir interfeyslər təmizlik və minimalizm üzərində qurulur. Əlavə olaraq, süni intellektin dizayn prosesinə inteqrasiyası işimizi daha da asanlaşdırır.</p>
<blockquote class="pull-quote" style="border-left: 4px solid var(--accent); padding-left: 20px; font-style: italic; color: var(--accent); margin: 30px 0;">
"İnnovasiya sadəcə yeni bir şey yaratmaq deyil, həm də köhnəni qeyri-adi şəkildə təqdim etməkdir."
</blockquote>
<p>Son olaraq, layihələrinizdə bu yenilikləri tətbiq etməkdən çəkinməyin.</p>
'''

Post.objects.all().update(content=html_content)
print("Updated all posts with rich HTML content including image and blockquote.")
