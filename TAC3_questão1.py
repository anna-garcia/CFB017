# importação de biblioteca:
from Bio.Seq import Seq
# recebendo a sequência de DNA como input
## DNA = Seq(str(input('Insira sua sequência de DNA:')))
### como arquivo FASTA:
FASTA = open("/home/carol/Documents/CFB017/sequenciaDesconhecida.fasta")
for lines in FASTA.readlines():
    if ">" not in lines:
        DNA = Seq(str(lines))
# a função .transcribe realiza a transcrição
        mRNA = DNA.transcribe()
# a função .translate() realiza a tradução A PARTIR de um RNA
        ptn = mRNA.translate()
# imprimir cada sequência abaixo de um identificador
print('mRNA:',mRNA,'ptn:',ptn,sep='\n')