from django.shortcuts import render

from django.contrib.auth import authenticate, logout, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, get_object_or_404
from .models import User
from django.http import HttpResponse

# Create your views here.


# @login_required(login_url='/auth/login/')
def login(request):
    id = request.user.id
    if id:
        return redirect('home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    id = request.user.id
    if id:
        return redirect('home')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    context = {
        'nome': nome,
        'email': email,
    }

    user = User.objects.filter(email=email)

    if user:
        return redirect('/auth/cadastro/?status=1')

    if nome.strip() == '' or email.strip() == '':
        return redirect('/auth/cadastro/?status=2', context)

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=3', context)

    try:
        senha = make_password(senha)
        user = User(first_name=nome, email=email, password=senha)
        user.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = authenticate(request, email=email, password=senha)
    if user is not None:
        login_django(request, user)
        return redirect('home')
    else:
        return redirect('/auth/login/?status=1')


def sair(request):
    logout(request)
    return redirect('/auth/login/')
