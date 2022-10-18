from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('send_message',views.send_message, name='send_message'),
    path('messages',views.messages, name='messages')
]