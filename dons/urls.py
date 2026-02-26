from django.urls import path
from . import views

app_name = 'dons'
urlpatterns = [
    path('', views.faire_don, name='faire_don'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
]