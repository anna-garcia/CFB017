# recebendo sequ�ncia de pr�-mRNA
RNA = str(input('Digite sua sequ�ncia de RNA:'))
# recebendo coordenadas ex�nicas
## o split separa o input e gera uma lista com os itens que foram separados
coordenada_a = str(input('coordenada 1:')).split(';')
coordenada_b = str(input('coordenada 2:')).split(';')
# fatiando a string sequ�ncia
## elementos da lista gerada pelo .split s�o transformadasem n�meros
## em python a contagem se inicia do zero, logo, deve-se subtrair 1 das coordenadas
exon1 = RNA[int(coordenada_a[0])-1:int(coordenada_a[-1])-1]
exon2 = RNA[int(coordenada_b[0])-1:int(coordenada_b[-1])-1]
# concatena��o dos exons
mRNA = exon1+exon2
print(mRNA)