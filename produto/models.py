from django.db import models
from django.utils.text import slugify
from utils import resizeImage, tools

class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa =models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices = (
            ('V', 'Variavel'),
            ('S', 'Simples'),
        ),
    )

    def __str__(self) -> str:
        return self.nome
    
    @property
    def getPreco(self):
        return tools.formataPreco(self.preco_marketing)
    getPreco.fget.short_description = "Preço"

    @property
    def getPrecoPromocional(self):
        return tools.formataPreco(self.preco_marketing_promocional)
    getPrecoPromocional.fget.short_description = "Preço Promocional"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(f'{self.nome}')
            self.slug = slug

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