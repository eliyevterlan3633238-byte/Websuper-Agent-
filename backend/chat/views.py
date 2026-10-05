from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Q
from .models import Chat, Message

@staff_member_required
def chat_list(request):
    query = request.GET.get('q', '')
    chats = Chat.objects.annotate(
        unread_count=Count('messages', filter=Q(messages__is_read=False, messages__sender_type='customer'))
    )
    if query:
        chats = chats.filter(customer_name__icontains=query)
    chats = chats.order_by('-unread_count', '-updated_at')
    
    # get the last message for each chat
    for chat in chats:
        chat.last_message = chat.messages.order_by('-created_at').first()

    context = {
        'chats': chats,
        'title': 'Canlı Çat',
        'site_header': 'WebSuper Admin',
    }
    return render(request, 'chat/admin_chat_list.html', context)

@staff_member_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    # Mark customer messages as read when admin opens the chat
    Message.objects.filter(chat=chat, sender_type='customer', is_read=False).update(is_read=True)
    
    messages = chat.messages.order_by('created_at')
    
    context = {
        'chat': chat,
        'chat_messages': messages,
        'title': f'Çat: {chat.customer_name}',
        'site_header': 'WebSuper Admin',
    }
    return render(request, 'chat/admin_chat_detail.html', context)

@staff_member_required
def delete_chat(request, chat_id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=chat_id)
        chat.delete()
        from django.http import JsonResponse
        return JsonResponse({'status': 'success'})
    from django.http import HttpResponseBadRequest
    return HttpResponseBadRequest()
def reset_chat(request):
    if 'chat_id' in request.session:
        del request.session['chat_id']
    from django.http import JsonResponse
    return JsonResponse({'status': 'success'})
