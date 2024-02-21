#get the protein sequences from the cds sections that had significant diffex
#args, i think none actually

#read in output from step 4
f=open('sleuth_fdr0.05.txt','r').read().rstrip().split('\n')
#f[0] is colnames. rest of items are one line WITH tab delim chrs between cols

#get all protein_ids
idlist=[]
for line in f[1:]:
    row=line.split('\t')
    id=row[0]
    idlist.append(id)

#use biopython for getting protein fastas using the protein ids
from Bio import Entrez
from Bio import SeqIO
Entrez.email='igregga@luc.edu'
handle=Entrez.efetch(db='protein',id=idlist,rettype='fasta',retmode='text')
#might not need to parsing step.......no i do actually the out file needs to be writable
records=SeqIO.parse(handle,format='fasta')
SeqIO.write(records,handle=open('proteins.fasta','w'),format='fasta')

