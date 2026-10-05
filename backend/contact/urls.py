from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('chat-message/', views.send_chat_message, name='send_chat_message'),
]
