# importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# cálculo da média pela função .mean().
média = WHO_data['TB deaths'].mean()
# cálculo da mediana pela função .median().
mediana = WHO_data['TB deaths'].median()
print('Média:',média,'Mediana:',mediana)