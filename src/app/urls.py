from django.urls import path
from app import views


urlpatterns = [
    path('about/', views.aboutpage, name='about'),
    path('', views.homepage, name='home'),
]