from django.template import Library
from utils import tools

register = Library()

@register.filter
def formataPreco(value):
    return tools.formataPreco(value)