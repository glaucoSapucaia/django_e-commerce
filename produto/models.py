from django.db import models
from utils.resize_image import resizeImage

class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa =models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices = (
            ('V', 'Variação'),
            ('S', 'Simples'),
        ),
    )

    def __str__(self) -> str:
        return self.nome
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            resizeImage(self.imagem)

class Variacao(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocinal = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.nome or self.produto.nome