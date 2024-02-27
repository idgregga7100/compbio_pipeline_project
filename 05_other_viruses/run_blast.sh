#!/bin/bash
#class ex: blastn -query sarscov2ref/ncbi_dataset/data/genomic.fna -db coronaviridae -out results -outfmt '6 qseqid sseqid stitle evalue pident qcovs'
#blast from command line
#max_hsps 'Setting it to one will show only the best HSP for every query-subject pair'
#want these for top ten hits:
#sacc pident length qstart qend sstart send bitscore evalue stitle

tblastn -query proteins.fasta -db betaherpesvirinae -out blastresults.tsv -max_hsps 1 -outfmt '6 sacc pident length qstart qend sstart send bitscore evalue stitle'