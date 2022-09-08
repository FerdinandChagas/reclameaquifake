from django.urls import path, include
from . import views

app_name = 'reclame'

urlpatterns = [
    path('', views.index, name='index'),
    path('cad/', views.cadView, name='cad'),
    path('cad_user/', views.cadUsuario, name='cad_user'),
    path('home/', views.index, name='index'),
    path('autentica/', views.autentica, name='autentica'),
    path('logout/', views.logout_view, name='logout')
    
]
