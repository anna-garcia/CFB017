#definindo função:
def Aprovação(total_faltas, nota_1, nota_2, nota_3):
#recebendo do usuário o nome do aluno:
    nome = str(input("Nome Completo do Aluno:"))
#calculando a porcentagem de faltas:
    percent = float(100*(total_faltas/80))
#calculando média:
    média = float((nota_1+nota_2+nota_3)/3)
#condições e situações de aprovação:
    if percent <= 25 and média >= 7.0:
        print("Nome: ",nome,"Média: ",média, "Faltas: ",percent, "Aprovado")
    elif percent > 25 and média >= 7.0:
        print("Nome: ",nome,"Média: ",média, "Faltas: ",percent, "Reprovado por Falta")
    elif média <= 7.0 and percent <= 25:
        print("Nome: ",nome,"Média: ",média, "Faltas: ",percent, "Reprovado por Média")
    elif percent > 25 and média <= 7.0:
        print("Nome: ",nome,"Média: ",média, "Faltas: ",percent, "Reprovado por Falta e Média")
#para chamar a função: 
#Aprovação(total_faltas, nota_1, nota_2, nota_3)