from django.urls import path
from . import views
from .views import getData
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('stats/', views.stats, name='stats'),
    path('api/data/', getData, name='api-data')
    path('buy/', views.buy_view, name='buy'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
]
