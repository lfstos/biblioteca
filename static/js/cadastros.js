function mostrar_form(arg) {
    categoria = document.getElementById('categorias');
    livro = document.getElementById('livros');
    emprestimo = document.getElementById('emprestimos');

    if (arg == categoria) {
        console.log('categoria');
        categoria.style.display = 'block';
        livro.style.display = 'none';
        emprestimo.style.display = 'none';
    }
    else if (arg == livro) {
        console.log('livro')
        livro.style.display = 'block';
        emprestimo.style.display = 'none';
        categoria.style.display = 'none';
    }
    else if (arg == emprestimo) {
        console.log('emprestimos')
        emprestimo.style.display = 'block';
        livro.style.display = 'none';
        categoria.style.display = 'none';
    }
}
