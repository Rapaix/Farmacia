class Cliente:
  def __init__(self, cpf, nome, data_nascimento):
    self.__cpf = cpf
    self.__nome = nome
    self.data_nascimento = data_nascimento
    
  @property
  def cpf(self):
    return self.__cpf

  @property
  def nome(self):
    return self.__nome

  

  
#Deverá ser possível emitir relatórios:
#De listagem de clientes, cadastrados por nome, em ordem alfabética crescrente (A-Z), especificando os dados do cliente

