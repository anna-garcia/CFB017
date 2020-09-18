# importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# criação de váriável
# seleção da coluna que se quer somar.
# .sum() realiza a soma e retorna o total.
total_deaths = WHO_data['TB deaths'].sum()
print(total_deaths)