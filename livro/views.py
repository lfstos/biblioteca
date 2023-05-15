from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Livros, Categoria, Emprestimo
from .forms import LivroForm, CategoriaForm
from django.http import HttpResponse


@login_required
def home(request):
    id = request.user.id
    livros = Livros.objects.filter(usuario=id)
    form = LivroForm(request)
    form_categoria = CategoriaForm()
    status_categoria = request.GET.get('cadastrar_categoria')
    # form.fields['usuario'].initial = request.user.id
    context = {
        'livros': livros,
        'form': form,
        'form_categoria': form_categoria,
        'status_categoria': status_categoria
    }
    return render(request, 'home.html', context)


@login_required
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)
    usuario_id = request.user.id
    categorias = Categoria.objects.filter(usuario=usuario_id)
    emprestimos = Emprestimo.objects.filter(livro_id=id)
    form = LivroForm(request)
    form_categoria = CategoriaForm()

    context = {
        'livro': livro,
        'categorias': categorias,
        'emprestimos': emprestimos,
        'form': form,
        'form_categoria': form_categoria
    }
    if request.user.id == livro.usuario.id:
        return render(request, 'ver_livro.html', context)
    else:
        return redirect('home')


@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request=request, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
            # else:
            #     return HttpResponse('Tentou salvar em outra conta de usuário')
        return HttpResponse('não salvou')


@login_required
def excluir_livro(request, id):
    Livros.objects.get(id=id).delete()
    return redirect('home')


@login_required
def cadastrar_categoria(request):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    usuario_id = request.POST.get('usuario_id')

    if request.user.is_authenticated and int(usuario_id) == int(request.user.id):
        # Duas formas diferentes de cadastrar chave estrageira, passando o Usuario para Categoria.usuario
        # usuario = User.objects.get(id=request.user.id)
        # Categoria(nome=nome, descricao=descricao, usuario=usuario).save()
        Categoria(nome=nome, descricao=descricao, usuario_id=usuario_id).save()
        return redirect('/livro/home?cadastrar_categoria=1')
    else:
        return HttpResponse('Errooooo')
