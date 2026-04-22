from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('compare/', views.compare, name='compare'),
]