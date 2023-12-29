from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from produto.models import Variacao
from utils import tools
from pedido.models import Pedido, ItemPedido

class Pagar(View):
    template_name = 'pedido/pagar.html'
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'É necessário fazer login!'
            )
            redirect('pedido:carrinho')

        if not self.request.session['carrinho']:
            messages.error(
                self.request,
                'Carrinho vazio'
            )
            redirect('produto:lista')

        carrinho = self.request.session.get('carrinho')
        carrinho_variacao_ids = [v for v in carrinho]
        db_variacoes = list(Variacao.objects.select_related('produto').filter(id__in=carrinho_variacao_ids))

        for variacao in db_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qtd_carrinho = carrinho[vid]['quantidade']
            preco = carrinho[vid]['preco_unitario']
            preco_promo = carrinho[vid]['preco_unitario_promocional']
            error_msg_estoque = ''

            if estoque < qtd_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * preco_promo

                error_msg_estoque = 'Alguns produtos estão indisponiveis!'
            
        if error_msg_estoque:
            messages.error(
                self.request,
                error_msg_estoque
            )
            self.request.session.save()
            return redirect('produto:carrinho')

        qtd_total_carrinho = tools.totalCarrinhoQtd(carrinho)
        total_carrinho = tools.totalCarrinho(carrinho)

        pedido = Pedido(
            usuario=self.request.user,
            total=total_carrinho,
            qtd_total = qtd_total_carrinho,
            status='C',
        )
        pedido.save()

        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido=pedido,
                    produto=v['produto_nome'],
                    produto_id=v['produto_id'],
                    variacao=v['variacao_nome'],
                    variacao_id=v['variacao_id'],
                    preco=v['preco_quantitativo'],
                    preco_promocional=v['preco_quantitativo_promocional'],
                    quantidade=v['quantidade'],
                    imagem=v['imagem'],
                )
                for v in carrinho.values()
            ]
        )

        del self.request.session['carrinho']
        return redirect('pedido:lista')

class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar pedido')

class Detalhes(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes')

class Lista(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista')
