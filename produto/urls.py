from django.urls import path
from produto.views import (ListaProdutos, DetalheProduto, AdicionarCarrinho, RemoverCarrinho,
                           Carrinho, Resumo, Busca)

app_name = 'produto'

urlpatterns = [
    path('', ListaProdutos.as_view(), name='lista'),
    path('<slug>', DetalheProduto.as_view(), name='detalhe'),
    path('adicionar-carrinho/', AdicionarCarrinho.as_view(), name='adicionar'),
    path('remover-carrinho/', RemoverCarrinho.as_view(), name='remover'),
    path('resumo-compra/', Resumo.as_view(), name='resumo'),
    path('carrinho/', Carrinho.as_view(), name='carrinho'),
    path('busca/', Busca.as_view(), name='busca'),
]
