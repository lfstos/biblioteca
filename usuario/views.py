from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User
from django.http import HttpResponse

# Create your views here.


def login(request):
    return HttpResponse('login')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    user = User.objects.filter(email=email)
    if user or email == '' or senha == '':
        return render(request, 'cadastro.html', {'nome': nome})
    else:
        user = User()
        user.first_name = nome
        user.email = email
        user.password = make_password(senha)
        user.save()
        return HttpResponse(f'Salvo com sucesso!')
