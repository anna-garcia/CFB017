# importação de bibliotecas:
import re
from Bio.Seq import Seq
from Bio import SeqIO

# ITEM B: Função que conta os motivos usando count()
def Counting_Motifs(sequence,motif):
    gene = str(line.id)
    mc = sequence.count(motif)
    if mc != 0:
#ITEM D: Printando os identificadores das sequencias que possuam o motivo
        print("Identificador:",gene,"Motivo:",motif,"Count:",mc,sep=" ")
        
# ITEM A: Lendo sequencia do usuário
motif = str(input("Insira seu motivo de DNA ou AA:")).upper()

# ITEM C: re.search para saber se o input é um DNA ou AA:
# o if sozinho sozinho é o mesmo que perguntar if condição é verdadeira
# se o motif tiver APENAS as letras A,C,G ou T, será considerada uma sequência de DNA
if re.search('^[ACGT]+$', motif):
    # DNA:
    print("É uma sequência de DNA.")
    multifasta = SeqIO.parse(open("/home/carol/Documents/CFB017/TriTrypDB_Annotated_CDS.fasta","r"), "fasta")
    for line in multifasta:
        sequence = str(line.seq)
        Counting_Motifs(sequence, motif)           

# se o motif tiver outra letra que não A,C,G ou, T, será considerada uma sequencia de AA
else:
    # Aminoácidos
    print("É uma sequência de AA.")
    multifasta = SeqIO.parse(open("/home/carol/Documents/CFB017/TriTrypDB_Proteins.fasta",'r'), "fasta")
    for line in multifasta:
        sequence = str(line.seq)
        Counting_Motifs(sequence, motif)
