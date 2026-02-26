from django.urls import path
from . import views

app_name = 'animateurs'
urlpatterns = [
    path('', views.liste, name='liste'),
]