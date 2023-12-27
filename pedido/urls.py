from django.urls import path
from pedido.views import (Pagar, FecharPedido, Detalhes)

app_name = 'pedido'

urlpatterns = [
    path('', Pagar.as_view(), name='pagar'),
    path('fechar-pedido/', FecharPedido.as_view(), name='fechar_pedido'),
    path('detalhes/', Detalhes.as_view(), name='detalhes'),
]
