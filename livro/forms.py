from django import forms
from .models import Livros, Categoria


# class CadastroLivroForm(forms.ModelForm):
class CadastroLivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'co_autor': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            # 'usuario': forms.HiddenInput()
        }

    def __init__(self, request, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['usuario'].initial = request.user.id
        self.fields['usuario'].widget = forms.HiddenInput()
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=request.user.id)
