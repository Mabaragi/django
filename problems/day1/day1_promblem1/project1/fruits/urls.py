from django.urls import path
from . import views

app_name = 'fruits'

urlpatterns = [
    path('fruits/', views.fruits, name = 'fruits'),
]