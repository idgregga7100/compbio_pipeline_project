#get the protein sequences from the cds sections that had significant diffex
#args, i think none actually
#nope jk outdir
import argparse
import sys

#function to parse command line arguments
def check_arg(args=None):
    parser=argparse.ArgumentParser(description='differential expression pipeline')
    parser.add_argument('-o','--outdir',help='output directory',required='True')
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args=check_arg(sys.argv[1:])
outdir=args.outdir

#read in output from step 4
f=open(outdir+'/sleuth_fdr0.05.txt','r').read().rstrip().split('\n')
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
SeqIO.write(records,handle=open(outdir+'/proteins.fasta','w'),format='fasta')

