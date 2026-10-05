from django.contrib import admin
from django.shortcuts import redirect
from .models import Chat, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        # Sol menyudan "Çatlar"a kliklədikdə bizim qurduğumuz xüsusi Canlı Çat səhifəsinə yönləndirsin
        return redirect('chat:chat_list')
        
    def add_view(self, request, form_url='', extra_context=None):
        return redirect('chat:chat_list')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        # Sol menyudan "Mesajlar"a kliklədikdə də həmin xüsusi Canlı Çat səhifəsinə yönləndirsin
        return redirect('chat:chat_list')
        
    def add_view(self, request, form_url='', extra_context=None):
        return redirect('chat:chat_list')
