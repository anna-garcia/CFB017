import csv
with open("/home/carol/Documents/CFB017/species.csv") as csvfile:
# open(“caminho completo para o arquivo que vai ser analisado”).   
    all_species = csv.reader(csvfile, delimiter=',')
# leitura e identificação do separador (já age como um “split(,)”).
    for lines in all_species:
        if lines[3].upper().rstrip() == "BIRD":
# a função .upper() deixa os caracteres da string em caixa alta.
# a função .rstrip() remove espaços em branco (default) no final da string.
            print(*lines,sep="\t")
# o operador '*' retorna apenas os elementos da lista 'lines'. 
# sep="\t" define tab como separador.
