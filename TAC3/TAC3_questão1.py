# importação de biblioteca:
from Bio.Seq import Seq
# recebendo a sequência de DNA como input
DNA = Seq(str(input('Insira sua sequência de DNA:')))
# a função .transcribe realiza a transcrição
mRNA = DNA.transcribe()
# a função .translate() realiza a tradução A PARTIR de um RNA
ptn = mRNA.translate()
# imprimir cada sequência abaixo de um identificador
print('mRNA:',mRNA,'ptn:',ptn,sep='\n')
