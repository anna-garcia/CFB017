## ITEM 1
# importação de bibliotecas
# o meu apenas funciona se eu importar pandas E pandas as pd.
import sys
import pandas
import pandas as pd
import xlrd
# para chamar no prompt de comando (terminal):
tabela = sys.argv[1] #
coef_m = float(sys.argv[2])
coef_b = float(sys.argv[3])
## ITEM 2
df = pd.read_excel(tabela) 
## ITEM 3
# criação de uma nova tabela:
df_q = df[['Target_Name','Stage']]
# adição de uma nova coluna:
df_q['Quantity'] = 10 ** ((df['CT']-coef_b)/coef_m)
## ITEM 4
# juntar as tabelas (deleção das colunas iguais):
df_final = pd.merge(df,df_q)
## ITEM 5
# salvar a nova tabela:
df_final.to_excel("/home/carol/Documents/CFB017/Tabela_Qntd_Abs.xlsx",sheet_name="CT_Abs")
## ITEM 6
print(df_final)
# para chamar a função no prompt digite no terminal:
# python nome_desse_script.py caminho_até_a_sua_tabela coeficiente_m coeficiente_b
# ex: python Calc_Quant_Abs.py ~/Documents/CFB017/Valores_CT.xlsx -3.397186047 58.53223295
