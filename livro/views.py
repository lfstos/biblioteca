from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Livros, Categoria, Emprestimo, User
from .forms import LivroForm, CategoriaForm
from datetime import date
from django.http import HttpResponse


@login_required
def status_livros(request, usuario_id, emprestado):
    return Livros.objects.filter(usuario_id=usuario_id).filter(emprestado=emprestado)


@login_required
def home(request):
    livros = Livros.objects.filter(usuario=request.user.id)
    total_livros = livros.count()
    form = LivroForm(request)
    form_categoria = CategoriaForm()
    status = request.GET.get('status')
    usuarios = User.objects.all()
    livros_emprestados = status_livros(request, request.user.id, True)
    livros_disponiveis = status_livros(request, request.user.id, False)

    context = {
        'livros': livros,
        'form': form,
        'form_categoria': form_categoria,
        'status': status,
        'usuarios': usuarios,
        'total_livros': total_livros,
        'usuario_id': request.user.id,
        'livros_disponiveis': livros_disponiveis,
        'livros_emprestados': livros_emprestados
    }
    return render(request, 'home.html', context)


@login_required
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)
    total_livros = Livros.objects.filter(usuario=request.user.id).count()
    usuario_id = request.user.id
    categorias = Categoria.objects.filter(usuario=usuario_id)
    emprestimos = Emprestimo.objects.filter(livro_id=id)
    form = LivroForm(request)
    form_categoria = CategoriaForm()
    usuarios = User.objects.all()
    livros = Livros.objects.all()
    livros_disponiveis = status_livros(request, request.user.id, False)
    livros_emprestados = status_livros(request, request.user.id, True)
    context = {
        'livro': livro,
        'categorias': categorias,
        'emprestimos': emprestimos,
        'form': form,
        'form_categoria': form_categoria,
        'usuarios': usuarios,
        'livros': livros,
        'livros_emprestados': livros_emprestados,
        'livros_disponiveis': livros_disponiveis,
        'total_livros': total_livros,
        'usuario_id': request.user.id
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
        return redirect('/livro/home?status=1')
    else:
        return redirect('sair')


@login_required
def cadastrar_emprestimo(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        if request.user.is_authenticated and int(usuario_id) == int(request.user.id):
            usuario_cadastrado = request.POST.get('usu_cadastrado')
            usuario_anonimo = request.POST.get('usu_anonimo')
            livro_emprestado = request.POST.get('livro_emprestado')

            livro = Livros.objects.get(id=livro_emprestado)
            livro.emprestado = True
            livro.save()

            if usuario_anonimo:
                emprestimo = Emprestimo(nome_emprestado_anonimo=usuario_anonimo, livro_id=livro_emprestado)
                emprestimo.save()
            else:
                emprestimo = Emprestimo(nome_emprestado_id=usuario_cadastrado, livro_id=livro_emprestado)
                emprestimo.save()
            return redirect('/livro/home?status=2')
        else:
            return redirect('sair')


@login_required
def devolver_livro(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        if request.user.is_authenticated and int(usuario_id) == int(request.user.id):
            try:
                livro_id = request.POST.get('livro_emprestado_id')
                livro = Livros.objects.get(id=livro_id)
                livro.emprestado = False
                livro.save()
            except:
                print('Falha ao gravar livro')

            try:
                # emprestimo = Emprestimo.objects.filter(livro_id=livro_id).filter(data_devolucao=None)
                emprestimo = Emprestimo.objects.get(livro_id=livro_id)
                emprestimo.data_devolucao = date.today()
                emprestimo.save()
            except:
                print('Falha ao gravar emprestimo')

            return redirect('/livro/home?status=4')


@login_required
def alterar_livro(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        if request.user.is_authenticated and int(usuario_id) == int(request.user.id):
            livro_id = request.POST.get('livro_id')
            nome = request.POST.get('nome')
            autor = request.POST.get('autor')
            co_autor = request.POST.get('co_autor')
            categoria_id = request.POST.get('categoria_id')

            # categoria = Categoria.objects.get(id=categoria_id)

            livro = Livros.objects.get(id=livro_id)

            if request.user.id == livro.usuario_id:
                livro.nome = nome
                livro.autor = autor
                livro.co_autor = co_autor
                # livro.categoria = categoria
                livro.categoria_id = categoria_id
                livro.save()
                return redirect('/livro/home?status=5')
            else:
                return redirect('sair')
        else:
            return redirect('sair')


@login_required
def seus_emprestimos(request):
    usuario = User.objects.get(id=request.user.id)
    emprestimos = Emprestimo.objects.filter(nome_emprestado=usuario)
    livros_emprestados = status_livros(request, request.user.id, True)
    context = {
        'emprestimos': emprestimos,
        'livros_emprestados': livros_emprestados
    }
    return render(request, 'seus_emprestimos.html', context)
