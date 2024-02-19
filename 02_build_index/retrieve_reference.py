#args needed: email

from Bio import Entrez
from Bio import SeqIO
Entrez.email='igregga@luc.edu'
handle=Entrez.efetch(db='genome',id='NC_006273.2',rettype='fasta')
records=list(SeqIO.parse(handle,'fasta'))

#need transcriptome reference, so retrieve CDS features
#write out fasta with each cds as entry with refseq protein_id as the label
