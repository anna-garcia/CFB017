refArquivo = open("/home/carol/Documents/CFB017/TriTrypDB_Proteins.fasta")
# open(“caminho completo para o arquivo que vai ser analisado”)
cabeçalho = ""
sequência = ""
# criação de variáveis
for line in refArquivo.readlines():
# o readlines() gera uma LISTA com todas as linhas
    if ">" in line:
        cabeçalho = line
# adiciona a linha atual à variável
        print('\n', cabeçalho, end="")
# end="" retira a quebra de linha do final
# eu acho que esse \n no início do print gera uma linha em branco no início
    else:
        sequência = line.replace('\n',"")
# deleção das quebras de linha (\n)
        print(sequência, end="")

refArquivo.close()
