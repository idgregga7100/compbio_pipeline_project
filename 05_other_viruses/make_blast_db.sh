#!/bin/bash
#blast+ steps
#want to download all relevant database genomes to do the blast search locally
#need to do makeblastdb command with bash
#need to download refseq sequences from ncbi first with ncbi datasets tool

#datasets download blah blah
#class ex: makeblastdb -in ncbi_dataset/data/genomic.fna -out coronaviridae -title coronaviridae -dbtype nucl

#download Betaherpesvirinae subfamily sequences for database
datasets download virus genome taxon betaherpesvirinae --refseq --include genome > betaherpesvirinae_download.zip
