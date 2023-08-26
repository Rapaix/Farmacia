class Cadastro:
  def __init__(self, lista):
    self.lista = lista

  def buscar(self, filtro):
    for i in self.lista:
      if i.nome == filtro:
        return i

lista = Cadastro('medicamentos')
lista2 = Cadastro('clientes')
lista.buscar('rafael')

lista.buscar('dipirona')