# importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# deixar a tabela em ordem crescente pela terceira coluna.
# a função .sort_values('Nome da Coluna') realiza essa organização.
ascending_deaths = WHO_data.sort_values('TB deaths')
# printar sem o index (primeira coluna que indica os números das linhas).
# a função .to_string transforma a váriavel tabular em strings e retira a indexação.
print(ascending_deaths.to_string(index=False))