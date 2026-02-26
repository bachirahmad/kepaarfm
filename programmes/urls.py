from django.urls import path
from . import views

app_name = 'programmes'
urlpatterns = [
    path('', views.liste, name='liste'),
]