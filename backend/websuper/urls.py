"""
URL configuration for websuper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.views.generic import RedirectView
from decouple import config

from .views import custom_set_language

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    path('admin/chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('i18n/setlang/', custom_set_language, name='set_language'),
    path('set-language/<str:lang_code>/', custom_set_language, name='switch_language'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
