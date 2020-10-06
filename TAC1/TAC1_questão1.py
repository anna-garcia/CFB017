# open(“caminho completo para o arquivo que vai ser analisado”).
refArquivo = open("/home/carol/Documents/CFB017/gabarito_gene")
# criação de variáveis.
cabeçalho = ""
sequência = ""
# o readlines() gera uma LISTA com todas as linhas.
for line in refArquivo.readlines():
# encontrar cabeçalho.
    if ">" in line:
# o split vai fatiar a lista dentro da variável 'line' com o separador ':'. 
# utilizamos apenas o primeiro item da lista([0]).
        gene_nome = line.split(':')[0]
# adiciona a linha atual à variável.
# o .replace deleta o caractére ‘>’.
        cabeçalho = gene_nome.replace(">",'')
    else:
# adição em loop das linhas de sequencia (tem mais de uma por causa das quebras do texto).
# line.replace retira as quebras de linha/new lines(\n).
        sequência += line.replace('\n',"")
# ‘\t’ é o símbolo para a tabulação (tab) que age como separador das colunas.
    print(cabeçalho,'\t',sequência)
refArquivo.close()
