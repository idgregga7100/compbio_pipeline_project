#!/bin/bash
#use kallisto to calculate tpm
#args: the four srr numbers and path
#stealing shell script args method from ryan's gwas qc pipeline lmao

while :
do
    case "$1" in
      -p | --path)
	        path=$2
	        shift 2
	        ;;
      -s | --samples)
	        samples=$2
            samples=${samples//,/ }
	        shift 2
	        ;;
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

#path='SRR_files'
#samples='SRR5660030 SRR5660033 SRR5660044 SRR5660045'

for sample in $samples
do
time kallisto quant \
-i ${outdir}/index.idx \
-o ${outdir}/${sample} \
-b 30 \
-t 4 \
${path}/${sample}_1.fastq ${path}/${sample}_2.fastq
done
