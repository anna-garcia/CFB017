## ITEM 1
def quantidade_absoluta(tabela, coef_m, coef_b):
# pra mim só funciona se eu imprtar pandas E pandas as pd.
    import pandas
    import pandas as pd
    import xlrd
## ITEM 2
    df = pd.read_excel(tabela) 
## ITEM 3
    df_q = df[['Target_Name','Stage']]
    df_q['Quantity'] = 10 ** ((df['CT']-coef_b)/coef_m)
## ITEM 4
    df_final = pd.merge(df,df_q)
## ITEM 5
    df_final.to_excel("/home/carol/Documents/CFB017/Tabela_Qntd_Abs.xlsx",sheet_name="CT_Abs")
## ITEM 6
    print(df_final)
# para chamar a função utilize o comando abaixo sem as'#'
# quantidade_absoluta('/home/carol/Documents/CFB017/Valores_CT.xlsx', -3.397186047, 58.53223295)
