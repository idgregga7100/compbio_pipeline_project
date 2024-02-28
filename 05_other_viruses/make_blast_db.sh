#!/bin/bash
#blast+ steps
#want to download all relevant database genomes to do the blast search locally
#need to do makeblastdb command with bash
#need to download refseq sequences from ncbi first with ncbi datasets tool

#datasets download blah blah
#class ex: makeblastdb -in ncbi_dataset/data/genomic.fna -out coronaviridae -title coronaviridae -dbtype nucl
while :
do
    case "$1" in
      -o | --outdir)
	        outdir=$2
	        shift 2
	        ;;
      *)  # No more options
         	shift
	        break
	        ;;
     esac
done

#download Betaherpesvirinae subfamily sequences for database
#CANNOT figure out how to get this to download into a different dir so FINE
datasets download virus genome taxon betaherpesvirinae --refseq --include genome 
unzip ncbi_dataset.zip
mv ncbi_dataset ${outdir} 
makeblastdb -in ${outdir}/ncbi_dataset/data/genomic.fna -out ${outdir}/betaherpesvirinae -title betaherpesvirinae -dbtype nucl

