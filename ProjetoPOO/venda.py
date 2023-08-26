class Venda:
    def __init__(self, data_hora, produtos, cliente):
        self.data_hora = data_hora
        self.produtos = produtos
        self.cliente = cliente
        self.valor_total = sum(produto.preco for produto in produtos)
