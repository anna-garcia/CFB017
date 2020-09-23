def quantidade_absoluta(coef_m, coef_b, tabela):
    import pandas
    import xlrd
    CT_values = pandas.read_excel(tabela)
## adiciona uma nova coluna na tabela.
## os valores dessa coluna serão as quantidades absolutas calculadas com a equação 2.    
    CT_values['Quantity'] = 10 ** ((CT_values['CT']-coef_b)/coef_m)
## salvar aletrações em outro arquivo excel.
    CT_values.to_excel("/home/carol/Documents/CFB017/Tabela_Qntd_Abs.xlsx",sheet_name="CT_Abs")
## impressão da tabela
    print(CT_values)
## para chamar a função utilize o comando abaixo
## quantidade_absoluta(-3.397186047, 58.53223295, '/home/carol/Documents/CFB017/Valores_CT.xlsx')