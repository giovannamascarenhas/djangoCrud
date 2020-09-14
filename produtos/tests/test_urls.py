from django.test import SimpleTestCase
from django.urls import reverse, resolve
from produtos.views import (
    lista_produtos, 
    produto_novo,
    atualizar_produtos,
    deletar_produtos
    )


class TestUrls(SimpleTestCase):

    def test_lista_produto_url_resolves(self):
        url = reverse('lista_produto')
        resolved_url = resolve(url)
        self.assertEquals(resolved_url.func, lista_produtos)

    def test_produto_novo_url_resolves(self):
        url = reverse('produto_novos')
        resolved_url = resolve(url)
        self.assertEquals(resolved_url.func, produto_novo)

    def test_update_produto_url_resolves(self):
        url = reverse('update_produto', kwargs={"id":1})
        resolved_url = resolve(url)
        self.assertEquals(resolved_url.func, atualizar_produtos)

    def test_delete_produto_url_resolves(self):
        url = reverse('delete_produto', kwargs={"id":1})
        resolved_url = resolve(url)
        self.assertEquals(resolved_url.func, deletar_produtos)
