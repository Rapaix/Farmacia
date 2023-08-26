from cliente import Cliente
from laboratorio import Laboratorio
from medicamento import MedicamentoFitoterapico, MedicamentoQuimicoterapico
from venda import Venda


clientes = [Cliente("704532888999", "Zezin Da Silva", "07/12/1993"),
            Cliente("7485682564", "Alexandre o Grande", "26/08/1914")
           ]

laboratorio1 = Laboratorio("HurbFarma", "Rua Bilclinton, Numero 74", "55265283", "Cotia", "São Paulo")
laboratorio2 = Laboratorio("HerbaLife", "Rua Joao Pessoa, Numero 98", "55428922", "Sao Caetano do Sul", "São Paulo")

medicamentos = [
                MedicamentoFitoterapico('Dipirona', 'Dipirona', laboratorio1, 'Dipirona é um analgésico e antitérmico', 'descrição', 90.0),
                MedicamentoQuimicoterapico('Dipirona', 'Dipirona', 'Bayer', 'Dipirona é um analgésico e antitérmico',False, 45.0)
               ]
vendas =  [
    Venda("10/08/2023 14:30", [medicamentos[0]], clientes[0]),
    Venda("10/08/2023 15:45", [medicamentos[1]], clientes[1])
          ]


def calcular_desconto(valor_total, idade_cliente):
    desconto = 0
    if idade_cliente > 65:
        desconto = 0.2
    elif valor_total > 150:
        desconto = 0.1
    return valor_total * desconto

# ----- RELATORIOS --------------------------------------------------------------------------------------------------
def clientes_em_ordem_alfabetica(clientes):
    clientes_ordem = sorted(clientes, key=lambda cliente: cliente.nome)
    for cliente in clientes_ordem:
        print(f"Cpf: {cliente.cpf}, Nome: {cliente.nome}, Data de nascimento: {cliente.data_nascimento}")

def medicamentos_em_ordem_afabetica(medicamentos):
  list_medicamentos = sorted(medicamentos, key=lambda medicamento: medicamento.nome)

  return list_medicamentos

def listagem_medicamentos_fitoterapico(medicamentos):
  for medicamento in medicamentos:
    if isinstance(medicamento, MedicamentoFitoterapico):
        print(f"Nome: {medicamento.nome}, Composto: {medicamento.principal_composto}, Laboratorio: {medicamento.laboratorio}, Descricao: {medicamento.descricao}, Preco: {medicamento.preco} ")

def listagem_medicamentos_quimioterapico(medicamentos):
  for medicamento in medicamentos:
    if isinstance(medicamento, MedicamentoQuimicoterapico):
        print(f"Nome: {medicamento.nome}, Composto: {medicamento.principal_composto}, Laboratorio: {medicamento.laboratorio}, Descricao: {medicamento.descricao}, Preco: {medicamento.preco}")  
def relatorio_vendas(vendas):
    total_clientes = len(set(venda.cliente for venda in vendas))
    total_quimioterapicos = sum(1 for venda in vendas if isinstance(venda.produtos[0], MedicamentoQuimicoterapico))
    total_fitoterapicos = sum(1 for venda in vendas if isinstance(venda.produtos[0], MedicamentoFitoterapico))
    mais_vendido = max(vendas, key=lambda venda: venda.produtos[0].preco)
  
    print("Relatório de Vendas:")
    print(f"Remédio mais vendido: {mais_vendido.produtos[0].nome}, Quantidade: {len(vendas)}, Valor Total: {mais_vendido.valor_total}")
    print(f"Total de pessoas atendidas: {total_clientes}")
    print(f"Número de remédios Quimioterápicos vendidos: {total_quimioterapicos}")
    print(f"Número de remédios Fitoterápicos vendidos: {total_fitoterapicos}")

print("Clintes em ordem alfabetica: ")
clientes_em_ordem_alfabetica(clientes)
print("-"*40)
print("Listadem de medicamentos fitorepicos: ")
listagem_medicamentos_fitoterapico(medicamentos)
print("-"*40)
print("Listadem de medicamentos Quimioterapicos: ")
listagem_medicamentos_quimioterapico(medicamentos)
print("-"*40)
print("Estatísticas dos atendimentos realizados no dia: ")
relatorio_vendas(vendas)

# TODO - ajustar as def para as classes, deixando somente o essencial na MAIN 
#TODO - Terminar a documentação do projeto no README
#TODO - ZIPAR o projeto e enviar no LMS