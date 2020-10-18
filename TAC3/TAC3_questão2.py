# importação de bibliotecas:
from Bio.Seq import Seq
from Bio import SeqIO
# para escrever um arquivo fasta
from Bio.SeqRecord import SeqRecord
# abrindo, lendo e identificando os itens do arquivo fasta:
multifasta = SeqIO.parse(open("/home/carol/Documents/CFB017/sequencias.fasta",'r'), "fasta")
# contador para os arquivos:
num = 0
# leitura das linhas:
for line in multifasta:
    num = num + 1
# o SeqRecord precisa ser gerado nessa ordem (id primeiro e seq depois dá bug)
    record = SeqRecord(line.seq, line.id)
# escrevendo o fasta inserindo a variável num no nome do arquivo
    SeqIO.write(record, 'Sequência_%d.fasta' % num,"fasta")