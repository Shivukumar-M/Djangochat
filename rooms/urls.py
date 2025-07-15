from django.contrib.auth import views as auth_views
from django.urls import path
from rooms import views


urlpatterns = [
    path('',views.rooms,name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    
]