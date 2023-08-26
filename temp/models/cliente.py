class Cliente:
  """
    Classe Cliente
    Contém informações básicas de um cliente.

    Atributos:
        cpf (str): CPF do cliente.
        nome (str): Nome do cliente.
        data_nascimento (str): Data de nascimento do cliente no formato "YYYY-MM-DD".
    """
  def __init__(self, cpf, nome, data_nascimento):
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento
    
  @property
  def cpf(self):
    return self.cpf

  @property
  def nome(self):
    return self.nome

  

  
#Deverá ser possível emitir relatórios:
#De listagem de clientes, cadastrados por nome, em ordem alfabética crescrente (A-Z), especificando os dados do cliente

