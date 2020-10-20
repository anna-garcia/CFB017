# todos os números digitados pelo usuário serão inseridos diretamente numa lista
val = [float(i) for i in input("Digite números aleatórios:").split()]
# soma de todos os elementos da lista e cálculo da média
media =float(sum(val)/len(val))
# contadores para os números positivos e negativos
n = 0
p = 0
for num in val:
    if num < 0:
        n = n + 1
    elif num > 0:
        p = p + 1
# no print já calcula-se a porcentagem
print("Média:",media,"Números Positivos:",p,"Porcentagem:",((p/len(val))*100),"Números Negativos:",n,"Porcentagem:",((n/len(val))*100),sep=" ")