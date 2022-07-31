from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]