# importação de bibliotecas: 
import sys
import pandas
import xlrd
# para chamar no prompt de comando (terminal):
tabela = sys.argv[1] #
coef_m = float(sys.argv[2])
coef_b = float(sys.argv[3])
CT_values = pandas.read_excel(tabela)
## adiciona uma nova coluna na tabela.
## os valores dessa coluna serão as quantidades absolutas calculadas com a equação 2.    
CT_values['Quantity'] = 10 ** ((CT_values['CT']-coef_b)/coef_m)
## salvar aletrações em outro arquivo excel.
CT_values.to_excel("/home/carol/Documents/CFB017/Tabela_Qntd_Abs_anna.xlsx",sheet_name="CT_Abs")
## impressão da tabela:
print(CT_values)
# para chamar a função no prompt digite no terminal:
# python nome_desse_script.py caminho_até_a_sua_tabela coeficiente_m coeficiente_b
# ex: python Calc_Quant_Abs.py ~/Documents/CFB017/Valores_CT.xlsx -3.4 58.5
