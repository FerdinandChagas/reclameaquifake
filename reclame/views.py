from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Usuario

# Create your views here.


def index(request):
    return render(request, 'reclame/cadusuario.html')

def cadUsuario(request):
    u = User(username=request.POST['nome'])
    u.is_staff=True
    u.usuario = Usuario()
    u.usuario.email = request.POST['email']
    u.email = request.POST['email']
    u.password = request.POST['senha']
    
    u.save()
    
    return render(request,'reclame/cadusuario.html')