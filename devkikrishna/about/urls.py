from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book_room, name='book_room'),
]