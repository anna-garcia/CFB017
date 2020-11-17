# importação de bibliotecas:
import sys
import pandas
import pandas as pd
import xlrd

## ITEM A:
# interação com o termiunal/linha de comando:
# tabela = sys.argv[1]
# arquivo1 = sys.argv[2]
# arquivo2 = sys.argv[3]
# gravando toda a tabela em uma variável para leitura - .read_excel:
RNA_seq = pandas.read_excel('/home/carol/Documents/CFB017/Projeto Final/Tabela_1.xlsx')

## ITEM B:
## adiciona novas colunas à tabela
## os valores dessa coluna serão as quantidades absolutas calculadas com a fórmula de CPM.    
RNA_seq['Rep1_A_CPM'] = RNA_seq['Rep1_A']/(10**6)*(RNA_seq['Rep1_A'].sum())
RNA_seq['Rep1_B_CPM'] = RNA_seq['Rep1_B']/(10**6)*(RNA_seq['Rep1_B'].sum())
RNA_seq['Rep2_A_CPM'] = RNA_seq['Rep2_A']/(10**6)*(RNA_seq['Rep2_A'].sum())
RNA_seq['Rep2_B_CPM'] = RNA_seq['Rep2_B']/(10**6)*(RNA_seq['Rep2_B'].sum())

## ITEM C:
RNA_seq['Cond_A_CPM_media'] = (RNA_seq['Rep1_A_CPM'] + RNA_seq['Rep2_A_CPM'])/2
RNA_seq['Cond_B_CPM_media'] = (RNA_seq['Rep1_B_CPM'] + RNA_seq['Rep2_B_CPM'])/2

##ITEM D:
Cond_A = RNA_seq.sort_values(['Cond_A_CPM_media'], ascending = [False])
Cond_B = RNA_seq.sort_values(['Cond_B_CPM_media'], ascending = [False])
print(Cond_A,'\n',Cond_B)
## salvar aletrações em outro arquivo excel.
#CT_values.to_excel("/home/carol/Documents/CFB017/Tabela_Qntd_Abs_anna.xlsx",sheet_name="CT_Abs")
