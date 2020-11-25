# importação de bibliotecas:
import sys
import pandas
import pandas as pd
import xlrd
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast.Applications import NcbiblastxCommandline
# blastx path:
blastx = "/home/carol/anaconda3/bin/blastx"


## ITEM A:
# interação com o termiunal/linha de comando:
# tabela = sys.argv[1]
# arquivo1 = sys.argv[2]
# arquivo2 = sys.argv[3]
# RNA_seq = pandas.read_excel(tabela)
# Rhodnius_desconhecido = SeqIO.parse(open(arquivo1,'r'), "fasta")
# Vector_Base =  SeqIO.parse(open(arquivo2,'r'), "fasta")

# para a IDE:
RNA_seq = pandas.read_excel('/home/carol/Documents/CFB017/Projeto Final/Tabela_1.xlsx')
Rhodnius_desconhecido = SeqIO.parse(open("/home/carol/Documents/CFB017/Projeto Final/Rdesconhecidus.fasta",'r'), "fasta")
Vector_Base =  SeqIO.parse(open("/home/carol/Documents/CFB017/Projeto Final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta",'r'), "fasta")


## ITEM B:
# adiciona novas colunas à tabela.
# os valores dessa coluna serão as quantidades absolutas calculadas com a fórmula de CPM.    
RNA_seq['Rep1_A_CPM'] = RNA_seq['Rep1_A']/(10**6)*(RNA_seq['Rep1_A'].sum())
RNA_seq['Rep1_B_CPM'] = RNA_seq['Rep1_B']/(10**6)*(RNA_seq['Rep1_B'].sum())
RNA_seq['Rep2_A_CPM'] = RNA_seq['Rep2_A']/(10**6)*(RNA_seq['Rep2_A'].sum())
RNA_seq['Rep2_B_CPM'] = RNA_seq['Rep2_B']/(10**6)*(RNA_seq['Rep2_B'].sum())


## ITEM C:
RNA_seq['Cond_A_CPM_media'] = (RNA_seq['Rep1_A_CPM'] + RNA_seq['Rep2_A_CPM'])/2
RNA_seq['Cond_B_CPM_media'] = (RNA_seq['Rep1_B_CPM'] + RNA_seq['Rep2_B_CPM'])/2


## ITEM D:
# ascending = [False] deixa a tabela ordenada em ordem decrescente.
# .head() nos dá os 5 primeiros itens.
Cond_A = RNA_seq.sort_values(['Cond_A_CPM_media'], ascending = [False]).head()
Cond_B = RNA_seq.sort_values(['Cond_B_CPM_media'], ascending = [False]).head()
# incluindo genes_id em uma lista:
A = Cond_A['gene_id'].tolist()
B = Cond_B['gene_id'].tolist()
# há genes que estão expressos no top 5 em ambas as condições.
# gene_4174 e gene_11244
# set() para retirar os genes duplicados:
genes = list(set(A+B))


## ITEM E:
record_list = []
# comparando os id da tabela com os id do multifasta desconhecido:
for line in Rhodnius_desconhecido:
    for i in genes:
        if i == line.id:
# gerando um novo arquivo fasta apenas com os genes mais expressos da tabela (lista genes):
            record = SeqRecord(line.seq, line.id, description='')
# para gerar um multifasta pode acrescentar divesros records em uma lista:
            record_list.append(record)
# O SeqIO.write entende a lista como um multifasta e gera um novo arquivo:
SeqIO.write(record_list, 'Most_expressed_genes.fasta',"fasta")

# BLAST X

Blast_Projeto_Final = r"/home/carol/Documents/CFB017/Projeto Final/Blast_Projeto_Final.txt"
meu_blast = NcbiblastxCommandline(cmd = blastx ,query = '/home/carol/Documents/CFB017/Projeto Final/Most_expressed_genes.fasta' , subject = '/home/carol/Documents/CFB017/Projeto Final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta', evalue = 0.05, outfmt = 6, out = Blast_Projeto_Final)
# redirecionando resultados: 
stdout, stdeer = meu_blast()
# adicionando cabeçalho à tabela de resultados do blastx:
blast = pd.read_csv("/home/carol/Documents/CFB017/Projeto Final/Blast_Projeto_Final.txt", sep='\t', names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])


## ITEM F:
#max_score = blast.sort_values(['qseqid','bitscore'], ascending=[True, False])
result = blast[['qseqid','sseqid','evalue','bitscore']]


##ITEM G:
# selecionando as colunas relacionadas aos genes mais expressos:
df = pd.DataFrame({'gene_id':genes}).merge(RNA_seq[['gene_id','Cond_A_CPM_media','Cond_B_CPM_media']])
# realizando merge com os reultados do BLAST e a seleção do maior hit p/ cada gene:

print (df)
