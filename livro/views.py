from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Livros


@login_required
def home(request):
    id = request.user.id
    livros = Livros.objects.filter(usuario=id)
    return render(request, 'home.html', {'livros': livros})


@login_required
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)
    return render(request, 'ver_livro.html', {'livro': livro})