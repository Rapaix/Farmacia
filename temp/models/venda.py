class Venda:
    def __init__(self, data_hora, produtos, cliente):
        self.data_hora = data_hora
        self.produtos = produtos  # Esperado ser uma lista de objetos com atributo 'preco'
        self.cliente = cliente
        self.valor_total = sum(produto.get_preco() for produto in produtos)  # Usando método get_preco()
