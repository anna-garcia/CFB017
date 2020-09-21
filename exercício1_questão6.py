# importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# normalização por 100.000 habitantes.
# [Population (1000s)] . 1000/100.000 = [Population (1000s)]/100
pop_normalizada = WHO_data['Population (1000s)']/100
# calculo da taxa de morte por país. 
# geração de uma nova coluna na tabela existente.
WHO_data['taxa_morte'] = WHO_data['TB deaths']/pop_normalizada
# impressão de apenas duas colunas: Países e a taxa de mortes.
# pode-se usar .to_csv também, e utilizar sep='\t' para separar as colunas por tabulação.
print(WHO_data[['Country','taxa_morte']].to_string(index=False))