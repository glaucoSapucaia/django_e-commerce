def formataPreco(value):
    return f'R$ {value:.2f}'.replace('.', ',')

def totalCarrinhoQtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])