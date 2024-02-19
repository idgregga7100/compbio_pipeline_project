# compbio_pipeline_project

This project aims to develop a pipeline and wrapper script to compare HCMV from 2 and 6 days post infection through differential expression.

Step 1: downloading SRR paired-end fastq files using sra-toolkit

'''{bash}
#example for one file:
fasterq-dump --split-3 SRR5660030
'''
