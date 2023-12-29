from django.urls import path
from pedido.views import (Pagar, SalvarPedido, Detalhes, Lista)

app_name = 'pedido'

urlpatterns = [
    path('pagar/<int:pk>', Pagar.as_view(), name='pagar'),
    path('salvar-pedido/', SalvarPedido.as_view(), name='salvar'),
    path('detalhes/<int:pk>', Detalhes.as_view(), name='detalhes'),
    path('lista/', Lista.as_view(), name='lista'),
]
