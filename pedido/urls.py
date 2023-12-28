from django.urls import path
from pedido.views import (Pagar, SalvarPedido, Detalhes)

app_name = 'pedido'

urlpatterns = [
    path('', Pagar.as_view(), name='pagar'),
    path('salvar-pedido/', SalvarPedido.as_view(), name='salvar'),
    path('detalhes/', Detalhes.as_view(), name='detalhes'),
]
