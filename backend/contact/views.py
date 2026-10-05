from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız uğurla göndərildi. Qısa zamanda sizinlə əlaqə saxlayacağıq.')
            return redirect('contact:index')
        else:
            messages.error(request, 'Zəhmət olmasa, formadakı xətaları düzəldin.')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})

from django.http import JsonResponse
from .models import LiveChatMessage

def send_chat_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            LiveChatMessage.objects.create(name=name, message=message)
            return JsonResponse({'status': 'success', 'message': 'Mesajınız uğurla göndərildi.'})
        return JsonResponse({'status': 'error', 'message': 'Bütün sahələri doldurun.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Yalnız POST müraciətləri dəstəklənir.'}, status=405)
