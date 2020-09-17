# importar biblioteca csv.
import csv
# open(“caminho completo para o arquivo que vai ser analisado”).
with open("/home/carol/Documents/CFB017/species.csv") as csvfile:
# leitura e identificação do separador (já age como um “split(,)”).
    all_species = csv.reader(csvfile, delimiter=',')
    for lines in all_species:
# a função .upper() deixa os caracteres da string em caixa alta.
# a função .rstrip() remove espaços em branco (default) no final da string.       
        if lines[3].upper().rstrip() == "BIRD":
# o operador '*' retorna apenas os elementos da lista 'lines'. 
# sep="\t" define tab como separador.
            print(*lines,sep="\t")
