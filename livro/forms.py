from django import forms
from .models import Livros, Categoria


# class CadastroLivroForm(forms.ModelForm):
class LivroForm(forms.ModelForm):
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


class CategoriaForm(forms.Form):
    nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # usuario = forms.ChoiceField()1
    
    
    
    # nome = models.CharField(max_length=30)
    # descricao = models.TextField()
    # usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)