from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

from .models import Usuario

# Create your views here.


def index(request):
    return render(request, 'reclame/cadusuario.html')

def cadUsuario(request):
    usuario = Usuario()
    usuario.nome = request.POST['nome']
    usuario.email = request.POST['email']
    usuario.senha = request.POST['senha']
    
    usuario.save()
    
    return render(request,'reclame/cadusuario.html')