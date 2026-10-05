import uuid
from .models import Chat, Message

def chat_widget(request):
    chat_id = request.session.get('chat_id')
    if not chat_id:
        new_chat = Chat.objects.create()
        chat_id = str(new_chat.id)
        request.session['chat_id'] = chat_id
    
    context = {'chat_id': chat_id}
    
    # Load history
    messages_qs = Message.objects.filter(chat_id=chat_id).order_by('created_at')
    chat_history = []
    for msg in messages_qs:
        chat_history.append({
            'id': msg.id,
            'type': msg.sender_type,
            'text': msg.text,
            'created_at': msg.created_at.isoformat()
        })
    context['chat_history'] = chat_history
    
    if hasattr(request, 'user') and request.user.is_staff:
        # Get global unread customer messages count
        unread_count = Message.objects.filter(is_read=False, sender_type='customer').count()
        context['chat_unread_count'] = unread_count
        
    return context
