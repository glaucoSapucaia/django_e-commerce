from django.contrib import admin
from pedido.models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'usuario', 'total', 'status', )
    list_display_links = ('pk', 'usuario', 'total', )
    list_per_page = 9
    search_fields = ('pk', 'usuario', 'total', 'status', )
    inlines = (
        ItemPedidoInline,
    )

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pedido', 'produto', 'variacao', 'preco', 'quantidade', 'imagem', )
    list_display_links = ('pedido', 'produto', 'variacao', )
    list_per_page = 9
    search_fields = ('pedido', 'produto', 'variacao', 'preco', 'quantidade')