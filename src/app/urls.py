from django.urls import path
from app import views


urlpatterns = [
    path('', views.api_root , name='root'),
]