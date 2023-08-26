class Laboratorio:

  def __init__(self, nome, endereco, telefone, cidade, estado):
    self.nome = nome
    self.__endereco = endereco
    self.__telefone = telefone
    self.cidade = cidade
    self.estado = estado

  def __repr__(self):
    return f'nome: {self.nome}, endereço {self.__endereco},telefone: {self.__telefone} cidade: {self.cidade} estado: {self.estado}'
