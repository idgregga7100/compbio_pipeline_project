#args needed: email

from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
Entrez.email='igregga@luc.edu'
handle=Entrez.efetch(db='nucleotide',id='NC_006273.2',rettype='genbank',retmode='text')
record=SeqIO.read(handle,format='genbank')

#get all features of type=cds to get transcriptome sections
cdsfeatures=[]
for feature in record.features:
    if feature.type=='CDS':
        cdsfeatures.append(feature)

#get sequences of each cds and protein_ids, save as seq records
rnarecords=[]
for cds in cdsfeatures:
    start=cds.location.start
    end=cds.location.end
    sequence=record.seq[start-1:end-1]
    sequence=sequence.transcribe()
    proteinid=cds.qualifiers['protein_id'][0]
    rec=SeqRecord(sequence,id=proteinid)
    rnarecords.append(rec)

#write out fasta with each cds as entry with refseq protein_id as the label
o=open('NC_006273.2_reference.fasta','w')
SeqIO.write(handle=o,sequences=rnarecords,format='fasta')
o.close()