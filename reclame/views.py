from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Usuario

# Create your views here.


def index(request):
    return render(request, 'reclame/index.html')

def cadUsuario(request):
    u = User.objects.create_user(username=request.POST['login'],email=request.POST['email'], password=request.POST['password'])
    #u.email = request.POST['email']
    #u.set_password = request.POST['password']
    u.first_name = request.POST['first_name']
    u.is_staff = True
    u.save()
    
    return render(request,'reclame/index.html', { 'feedback': 'Cadastro realizado com sucesso!'})

def cadView(request):
    return render(request,'reclame/cadusuario.html')

def autentica(request):
    user = authenticate(request, username=request.POST['login'],password=request.POST['password'])
    
    if user is not None:
        login(request, user)
        return render(request, 'reclame/home.html', { 'user': user })
    else:
        return render(request, 'reclame/index.html', { 'feedback': 'Falha ao tentar relizar login' })
    

def logout_view(request):
    logout(request)
    return render(request, 'reclame/index.html')
    