from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('pk', 'usuario', 'cidade', 'bairro', 'estado',)
    list_display_links = ('usuario',)
    list_per_page = 9
    search_fields = ('pk', 'usuario', 'data_nascimento', 'cpf', 'cidade', 'bairro', 'estado',)