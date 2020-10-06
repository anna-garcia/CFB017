# guarda a sequencia numa variável em formato de string
seq = str(input('Sequência de Nucleotídeos:'))
# contador de conteúdo GC
count = 0
for i in seq:
# função upper para facilitar
# 'or' booleano. Reescreve a variavel(x==y or x==z) ou utiliza elif
    if str(i).upper() == "G" or str(i).upper() == "C" :
# contador recebe valor
        count = count+1
print(count)
