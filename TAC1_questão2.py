refArquivo = open("/home/carol/Documents/CFB017/TriTrypDB_Proteins.fasta")
# open(“caminho completo para o arquivo que vai ser analisado”)
cabeçalho = ""
sequência = ""
# criação de variáveis
for line in refArquivo.readlines():
# o readlines() gera uma LISTA com todas as linhas
# line é uma variável que a cada loop recebe como valor uma lista que contém uma linha do arquivo
    if ">" in line:
        cabeçalho = line.strip('\n')
# adiciona a linha atual à variável
# o .rstrip('\n') deleta quebras de linha no final da string.
# sem o .rstrip, o print abaixo gera uma linha em branco entra o cabeçalho e a sequencia
        print(cabeçalho)
        if sequência != "":
# nesse caso, é o mesmo que perguntar se sequência não está vazia
            sequência = ""
# a variável sequência deve ser zerada dentro do loop para não acumular sequencias de outros cabeçalhos
    else:
        sequência += line.strip('\n')
        print(sequência)
# deleção das quebras de linha (\n)
refArquivo.close()
