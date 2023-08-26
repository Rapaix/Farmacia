class Laboratorio:
  def __init__(self, nome, endereco, telefone, cidade, estado):
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
    self.cidade = cidade
    self.estado = estado

  def __repr__(self):
    return f'nome: {self.nome}, endereço: {self.endereco}, telefone: {self.telefone}, cidade: {self.cidade}, estado: {self.estado}'
