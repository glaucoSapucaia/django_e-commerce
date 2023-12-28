def formataPreco(value):
    return f'R$ {value:.2f}'.replace('.', ',')

def totalCarrinhoQtd(carrinho: dict):
    return sum([item['quantidade'] for item in carrinho.values()])

def totalCarrinho(carrinho: dict):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item in carrinho.values()
        ]
    )   