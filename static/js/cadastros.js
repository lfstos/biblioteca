function mostrar_form(arg) {
    categoria = document.getElementById('categorias');
    livro = document.getElementById('livros');
    emprestimo = document.getElementById('emprestimos');

    if (arg == categoria) {
        categoria.style.display = 'block';
        livro.style.display = 'none';
        emprestimo.style.display = 'none';
    }
    else if (arg == livro) {
        livro.style.display = 'block';
        emprestimo.style.display = 'none';
        categoria.style.display = 'none';
    }
    else if (arg == emprestimo) {
        emprestimo.style.display = 'block';
        livro.style.display = 'none';
        categoria.style.display = 'none';
    }
}

function   exibi_input_emprestado(arg) {
    usuario_cadastrado = document.getElementById('usuario_cadastrado');
    usuario_novo = document.getElementById('usuario_novo');
    form_emprestimo = document.getElementById('form_emprestimo');
    nome_emprestado = document.getElementById('nome_emprestado')
    nome_emprestado_anonimo = document.getElementById('nome_emprestado_anonimo')

    if (arg == usuario_cadastrado) {
        form_emprestimo.style.display = 'block';
        nome_emprestado.style.display = 'Block';
        nome_emprestado_anonimo.style.display = 'none';
    }
    else if (arg == usuario_novo) {
        form_emprestimo.style.display = 'block';
        nome_emprestado.style.display = 'none';
        nome_emprestado_anonimo.style.display = 'block';
    }
}
