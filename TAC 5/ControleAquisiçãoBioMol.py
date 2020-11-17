# importação de módulos criados:
# é necessário adicionar a localização deste módulo ao path do IDE!!
import OperacõesCompra
#flag
f = 1
# criação de dicionário:
estoque = {}
# lista: 
gasto = []
#loop:
while f==1:
    produto=str(input("produto:"))
    if produto == str(-1):
        break
    else:
# gravando input do usuário em variáveis:
        preço=float(input("preço:"))
        quant=int(input("quantidade:"))
# gravando elemento de dicionário: 
        e = {produto : [preço,str(quant)]}
# atualizando o dicionário principal com os elementos acima:
        estoque.update(e)
# a lista gasto terá o valor total de cada item (preço x quantidade)
        gasto.append(float(preço*quant))
# utilização das funções criadas no modulo importado:
OperacõesCompra.ImprimeProdutos(estoque)
OperacõesCompra.ImprimeQuantidade(estoque)
print("Gastos Totais:",OperacõesCompra.CalculaTotalCompra(gasto),sep=" ")
