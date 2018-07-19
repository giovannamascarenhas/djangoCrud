from django.forms import ModelForm
from .models import Produtos


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produto', 'quantidade', 'preço']