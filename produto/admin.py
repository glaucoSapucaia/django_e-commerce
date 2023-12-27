from django.contrib import admin
from produto.models import Produto, Variacao

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'slug', 'getPreco', 'tipo', )
    list_display_links = ('nome', )
    list_per_page = 9
    search_fields = ('pk', 'nome', 'preco_marketing', 'tipo', )
    inlines = (
        VariacaoInLine,
    )

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'produto', 'nome', 'preco', 'estoque', )
    list_display_links = ('produto', 'nome')
    list_per_page = 9
    search_fields = ('pk', 'produto', 'nome', 'preco', 'estoque', )
