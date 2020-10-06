# open(“caminho completo para o arquivo que vai ser analisado”)
refArquivo = open("/home/carol/Documents/CFB017/TriTrypDB_Proteins.fasta")
# criação de variáveis
cabeçalho = ""
sequência = ""
# o readlines() gera uma LISTA com todas as linhas
# line é uma variável que a cada loop recebe como valor uma lista que contém uma linha do arquivo.
for line in refArquivo.readlines():
# busca por cabeçalhos.
    if ">" in line:       
# perguntar se sequência não está vazia
        if sequência != "":
            print(cabeçalho)
            print(sequência)
# a variável sequência deve ser zerada dentro do loop para não acumular sequencias de outros cabeçalhos
            sequência = ""
# sem o .strip, o print abaixo gera uma linha em branco entra o cabeçalho e a sequencia
# adiciona a linha atual à variável
        cabeçalho = line.strip('\n')
    else:
# concatenação de sequências de AA
# deleção das quebras de linha (\n)
        sequência += line.strip('\n')
# precisa realizar o print novamente para imprimir os últimos itens
print(cabeçalho)
print(sequência)
refArquivo.close()
