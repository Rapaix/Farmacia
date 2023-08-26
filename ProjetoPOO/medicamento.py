class Medicamento:

  def __init__(self, nome, principal_composto, laboratorio, descricao, preco):
    self.nome = nome
    self.principal_composto = principal_composto
    self.laboratorio = laboratorio
    self.descricao = descricao
    self.preco = preco

  def __repr__(self):
    return f'nome: {self.nome}, {self.principal_composto},laboratorio: {self.laboratorio} descricao: {self.descricao}, preco: {self.preco}'


class MedicamentoFitoterapico(Medicamento):

  def __init__(self, nome, principal_composto, laboratorio, descricao,
               necessita_receita, preco):
    super().__init__(nome, principal_composto, laboratorio, descricao, preco)
    


class MedicamentoQuimicoterapico(Medicamento):

  def __init__(self, nome, principal_composto, laboratorio, descricao, necessita_receita, preco):
    super().__init__(nome, principal_composto, laboratorio, descricao, preco)
    self.necessita_receita = necessita_receita