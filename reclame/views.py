from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Usuario

# Create your views here.


def index(request):
    return render(request, 'reclame/index.html')

def cadUsuario(request):
    u = User.objects.create_user(request.POST['login'],request.POST['email'], request.POST['password'])
    u.set_password = request.POST['password']
    u.first_name = request.POST['first_name']
    
    
    u.save()
    
    return render(request,'reclame/cadusuario.html')

def autentica(request):
    user = authenticate(login=request.POST['login'],password=request.POST['password'])
    if user is not None:
        return render(request, 'reclame/home.html', { 'user': user })
    else:
        return render(request, 'reclame/index.html', { 'feedback': 'Falha ao tentar relizar login' })
        