#importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel. Coloque todo o caminho até o arquivo.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# imprimir toda a tabela.
print(WHO_data)
