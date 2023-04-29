from django.db import models
from usuario.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome


class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, null=True, blank=True)
    nome_emprestado = models.CharField(max_length=30, null=True, blank=True)
    emprestado = models.BooleanField(default=False)
    data_cadastro = models.DateField(auto_now_add=True)
    data_emprestimo = models.DateField(null=True, blank=True)
    deta_devolucao = models.DateField(null=True, blank=True)
    tempo_duracao = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Livro'
