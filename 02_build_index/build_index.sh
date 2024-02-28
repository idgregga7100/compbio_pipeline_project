#!/bin/bash
#script to run kallisto
#can hardcode the output from retrieve_reference
#no jk adding output directory arg
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

kallisto index -i ${outdir}/index.idx ${outdir}/NC_006273.2_reference.fasta
