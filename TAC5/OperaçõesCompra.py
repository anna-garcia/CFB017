# Este módulo será importado no código principal ControleAquisiçãoBioMol.py

# recebe como entrada o dicionário criado com itens do estoque mais a lista como valor
def ImprimeProdutos(dic): 
# formatando para sair todos os nomes numa mesma linha sem 'dic.keys' aparecer no output
    print(', '.join("{}".format(k) for k, v in dic.items()))

# recebe de entrada o dicionário estoque
def ImprimeQuantidade(dic):
# criação de lista vazia pra receber as quantidades - segundo item da lista em dic.values
    l=[]
    for v in dic.values():
        l.append(v[-1])
# só consegui imprimir tudo na mesma linha realizando a formatação e realizando o append em uma nova lista
    print(', '.join(map(str, l)))
    
# recebe como entrada uma lista chamada gastos.
# linhas 23 e 24 do código principal!!!
def CalculaTotalCompra(lista):
# realizando somatório de todos os itens da lista:
    return sum(lista)
