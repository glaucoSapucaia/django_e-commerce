from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    total = models.FloatField()
    qtd_total = models.PositiveBigIntegerField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado', ),
            ('C', 'Criado', ),
            ('R', 'Reprovado', ),
            ('P', 'Pendente', ),
            ('E', 'Enviado', ),
            ('F', 'Finalizado', ),
        ),
    )

    def __str__(self) -> str:
        return f'Pedido N. {self.pk}'

class ItemPedido(models.Model):
    class Meta:
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens do pedido'

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
    )
    produto = models.CharField(max_length=100)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=100)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveBigIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f'Item do Pedido {self.pedido}'