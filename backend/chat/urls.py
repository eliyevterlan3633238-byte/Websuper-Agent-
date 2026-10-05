from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('reset/', views.reset_chat, name='reset_chat'),
    path('', views.chat_list, name='chat_list'),
    path('<uuid:chat_id>/', views.chat_detail, name='chat_detail'),
    path('delete/<uuid:chat_id>/', views.delete_chat, name='delete_chat'),
]
