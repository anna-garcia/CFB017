# importação de bibliotecas:
import pandas
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline
# blastx path:
blastx = "/home/carol/anaconda3/bin/blastx"
# query:
seq_hipot = r"/home/carol/Documents/CFB017/sequenciaDesconhecida.fasta"
# Subject:
Tcruzi_data = r"/home/carol/Documents/CFB017/TriTrypDB-47_Tcruzi_AnnotatedProteins.fasta"
# Resultado:
Blast_TAC3 = r"/home/carol/Documents/CFB017/Blast_TAC3.txt"
# blast x
meu_blast = NcbiblastxCommandline(cmd = blastx ,query = seq_hipot, subject = Tcruzi_data, evalue = 0.05, outfmt = 6, out = Blast_TAC3)
# redirecionando resultados: 
stdout, stdeer = meu_blast()
# adicionando cabeçalho à tabela de resultados do blastx:
result = pd.read_csv("/home/carol/Documents/CFB017/Blast_TAC3.txt", sep='\t', names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])
# ordenando resultado BLASTX por ordem crescente de bitscore:
max_score = result.sort_values('bitscore')
# printando a última linha (maior score):
print(max_score.iloc[[-1]])
