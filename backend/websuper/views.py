import re
from urllib.parse import urlsplit, urlunsplit
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation

def custom_set_language(request, lang_code=None):
    """
    Switches language seamlessly by correctly updating URL prefix (e.g. /ru/ -> /az/)
    and updating the session and cookies so user never gets stuck.
    Supports both POST (form) and GET (direct link / fallback).
    """
    if not lang_code:
        lang_code = request.POST.get('language') or request.GET.get('language')
        
    available_codes = [code for code, name in settings.LANGUAGES]
    if not lang_code or lang_code not in available_codes:
        lang_code = settings.LANGUAGE_CODE

    next_url = request.POST.get('next') or request.GET.get('next') or request.META.get('HTTP_REFERER') or f"/{lang_code}/"
    parsed = urlsplit(next_url)
    path = parsed.path or '/'

    pattern = r'^/(' + '|'.join(available_codes) + r')(?:/(.*))?$'
    match = re.match(pattern, path)
    if match:
        rest = match.group(2) or ''
        new_path = f"/{lang_code}/{rest}" if rest else f"/{lang_code}/"
    else:
        if path == '/':
            new_path = f"/{lang_code}/"
        elif path.startswith('/admin/'):
            new_path = path
        else:
            clean_path = path.lstrip('/')
            new_path = f"/{lang_code}/{clean_path}"

    redirect_url = urlunsplit(('', '', new_path, parsed.query, parsed.fragment))
    response = HttpResponseRedirect(redirect_url)

    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,
        lang_code,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    if hasattr(request, 'session'):
        request.session['_language'] = lang_code
        
    translation.activate(lang_code)
    return response
