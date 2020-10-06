seq_a = str(input('Sequência 1:'))
seq_b = str(input('Sequência 2:'))
# concatenação de strings
seq = seq_a + seq_b
# invertendo a ordem da sequência
rev_seq = seq[::-1]
complemento_reverso = ''
# essa parte pode ser feita com dicionário também
for i in rev_seq:
    if i.upper() == 'A':
# inserção de um novo caracter à string complemento reverso
        complemento_reverso += 'T'
    if i.upper() == 'T':
        complemento_reverso += 'A'
    if i.upper() == 'G':
        complemento_reverso += 'C'
    if i.upper() == 'C':
        complemento_reverso += 'G'
print(complemento_reverso)
