#!/bin/bash
#use kallisto to calculate tpm
#args: the four srr numbers

path='SRR_files'
samples='SRR5660030 SRR5660033 SRR5660044 SRR5660045'

for sample in $samples
do
time kallisto quant \
-i index.idx \
-o ${sample} \
-b 30 \
-t 4 \
${path}/${sample}_1.fastq ${path}/${sample}_2.fastq
done