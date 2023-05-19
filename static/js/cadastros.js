function mostrar_elementos(elemento) {
    elemento.style.display = 'block';
}

function ocultar_elemento(elemento) {
    elemento.style.display = 'none';
}

function mostrar_form(elemento_selecionado) {
    categoria = document.getElementById("categorias");
    livro = document.getElementById("livros");
    emprestimo = document.getElementById("emprestimos");
    devolucao = document.getElementById("devolucao");   
    
    ocultar_elemento(categoria);
    ocultar_elemento(livro);
    ocultar_elemento(emprestimo);
    ocultar_elemento(devolucao);

    if (elemento_selecionado == categoria) {
        mostrar_elementos(categoria);
    }
    else if(elemento_selecionado == livro) {
        mostrar_elementos(livro);
    }
    else if(elemento_selecionado == emprestimo) {
        mostrar_elementos(emprestimo);
    }
    else if(elemento_selecionado == devolucao) {
        mostrar_elementos(devolucao);
    }
}

function   exibir_input_emprestado(elemento) {
    usuario_cadastrado = document.getElementById('usuario_cadastrado');
    usuario_anonimo = document.getElementById('usuario_anonimo');
    usu_cadastrado = document.getElementById('usu_cadastrado');
    usu_anonimo = document.getElementById('usu_anonimo');
    form_emprestimo = document.getElementById('form_emprestimo');

    ocultar_elemento(usu_cadastrado);
    ocultar_elemento(usu_anonimo);
    ocultar_elemento(form_emprestimo);
    
    if (elemento == usuario_cadastrado) {
        mostrar_elementos(form_emprestimo);
        mostrar_elementos(usu_cadastrado);
    }
    else if (elemento == usuario_anonimo) {
        console.log('usuario_anonimo');
        mostrar_elementos(form_emprestimo);
        mostrar_elementos(usu_anonimo);
    }
}
