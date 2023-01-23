from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('getMessages/<str:room>/typing', views.typing, name='typing'),
    path('allrooms', views.all_rooms, name='list-rooms')
]