from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .forms import ProdutosForm
# Create your views here.

@login_required
def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'listagem_produtos.html', {'produtos': produtos})


@login_required
def produto_novo(request):
    form = ProdutosForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'produtos_form.html', {'form': form})


@login_required
def atualizar_produtos(request, id):
    produtos = get_object_or_404(Produtos, pk=id)
    form = ProdutosForm(request.POST or None, instance=produtos)
    if form.is_valid():
        produtos.save()
        return redirect('lista_produto')
    return render(request, 'produtos_form.html', {'form': form})


@login_required
def deletar_produtos(request, id):
    produtos = get_object_or_404(Produtos, pk=id)
    form = ProdutosForm(request.POST or None, instance=produtos)
    if request.method == 'POST':
        produtos.delete()
        return redirect('lista_produto')
    return render(request, 'delete_produto.html', {'produtos': produtos})
