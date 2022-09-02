from django.urls import path, include
from . import views

app_name = 'reclame'

urlpatterns = [
    path('', views.index, name='index'),
    path('cad/', views.cadUsuario, name='cad')
]
