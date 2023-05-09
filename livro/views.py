from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivroForm
from django.http import HttpResponse


@login_required
def home(request):
    id = request.user.id
    livros = Livros.objects.filter(usuario=id)
    form = CadastroLivroForm(request)
    # form.fields['usuario'].initial = request.user.id
    context = {
        'livros': livros,
        'form': form,
    }
    return render(request, 'home.html', context)


@login_required
def ver_livro(request, id):
    livro = Livros.objects.get(id=id)
    usuario_id = request.user.id
    categorias = Categoria.objects.filter(usuario=usuario_id)
    emprestimos = Emprestimo.objects.filter(livro_id=id)
    form = CadastroLivroForm(request)
    
    context = {
        'livro': livro,
        'categorias': categorias,
        'emprestimos': emprestimos,
        'form': form
    }
    if request.user.id == livro.usuario.id:
        return render(request, 'ver_livro.html', context)
    else:
        return redirect('home')


@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivroForm(request=request, data=request.POST)

        if form.is_valid():
            # if form.cleaned_data['usuario'] == request.user.id:
            print(form.cleaned_data['usuario'])
            form.save()
            return redirect('home')
            # else:
            #     return HttpResponse('Tentou salvar em outra conta de usuário')
        return HttpResponse('não salvou')
    

@login_required
def excluir_livro(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect('home')
