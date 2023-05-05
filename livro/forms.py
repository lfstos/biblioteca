from django import forms
from .models import Livros


class CadastroLivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'co_autor': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            # 'usuario': forms.HiddenInput,
        }
        exclude = ['emprestado']
