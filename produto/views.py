from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from produto.models import Produto

class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3
    ordering = ('-pk',)

class DetalheProduto(DetailView):
    model = Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'  

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
