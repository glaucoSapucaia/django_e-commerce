from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista Produtos')


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe Produto')


class AdicionarCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao carrinho')


class RemoverCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover Carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
