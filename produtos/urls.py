from django.urls import path
from .views import lista_produtos
from .views import produto_novo
from .views import atualizar_produtos
from .views import deletar_produtos

urlpatterns = [
    path('listagem/', lista_produtos, name='lista_produto'),
    path('adicionar/', produto_novo, name='produto_novos'),
    path('atualizar/<int:id>/', atualizar_produtos, name='update_produto'),
    path('deletar/<int:id>/', deletar_produtos, name='delete_produto'),
]

