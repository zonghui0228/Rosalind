# ^_^ coding:utf-8 ^_^

from Bio import SeqIO

# ==============================
# config the input
data = "../data/rosalind_grph.txt"
n = 3

# ==============================
# 1. read fastq file
seq_name, seq_string = [], []
with open (data,'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))
# print(seq_name)
# print(seq_string)

# 2. get adjacency list
for i in range(len(seq_string)):
    for j in range(len(seq_string)):
        if i != j:
            if seq_string[i][-n:] == seq_string[j][:n]:
                print(seq_name[i], seq_name[j])


