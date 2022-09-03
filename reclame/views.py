from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Usuario

# Create your views here.


def index(request):
    return render(request, 'reclame/cadusuario.html')

def cadUsuario(request):
    u = User.objects.create_user(request.POST['login'],request.POST['email'], request.POST['password'])
    u.set_password = request.POST['password']
    u.first_name = request.POST['first_name']
    
    
    u.save()
    
    return render(request,'reclame/cadusuario.html')