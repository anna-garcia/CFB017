# importação da biblioteca para o script.
import pandas
# para o .read_excel poder rodar, o IDE exigiu o xlrd, um pacote do pandas para leitura de tabelas em excel (.xls ou .xlsx)
import xlrd
# leitura da tabela em formato excel.
WHO_data = pandas.read_excel('/home/carol/Documents/CFB017/WHO.xls')
# deixar a tabela em ordem crescente pela terceira coluna.
# a função .sort_values('Nome da Coluna') realiza essa organização.
ascending_deaths = WHO_data.sort_values('TB deaths')
# seleção da primeira e da ultima linha com .iloc[].
# primeira linha: 0, última linha: -1
first_and_last = ascending_deaths.iloc[[0, -1]]
# seleção das colunas que queremos imprimir: [['coluna 1','coluna 2']]
# além de deletar a coluna com index, podemos deletar o cabeçalho da tabela com header=None
print(first_and_last[['Country','TB deaths']].to_string(index=False, header=None))
