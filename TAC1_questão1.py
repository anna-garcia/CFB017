refArquivo = open("/home/carol/Documents/CFB017/gabarito_gene")
# open(“caminho completo para o arquivo que vai ser analisado”)
cabeçalho = ""
sequência = ""
# criação de variáveis
for line in refArquivo.readlines():
# o readlines() gera uma LISTA com todas as linhas
    if ">" in line:
        gene_nome = line.split(':')[0]
# o split vai fatiar a lista dentro da variável 'line' com o separador ':'. Utilizamos apenas o primeiro item da lista([0])
        cabeçalho = gene_nome.replace(">",'')
# adiciona a linha atual à variável
# o .replace deleta o caractére ‘>’
    else:
        sequência += line.replace('\n',"")
# adição em loop das linhas de sequencia (tem mais de uma por causa das quebras do texto)
# line.replace retira as quebras de linha/new lines(\n)
print(cabeçalho,'\t',sequência)
# ‘\t’ é o símbolo para a tabulação (tab) que age como separador das colunas
refArquivo.close()
