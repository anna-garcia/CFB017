#importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# Selecionando apenas os países da BRICS. 
BRICS = WHO_data.iloc[[1, 2, 5, 8, 10]]
# calcular a soma e colocar numa variável.
total_BRICS = BRICS['TB deaths'].sum()
# calculo da média. a função .sum() já deixa a váriável como um número ao invés de uma string.
media_BRICS = total_BRICS/5
# imprimir total.
print('Total de Mortes: ',total_BRICS)
# imprimir média.
print('Média de Mortes: ',media_BRICS)