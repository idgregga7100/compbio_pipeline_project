# compbio_pipeline_project

This project aims to develop a pipeline and wrapper script to compare HCMV from 2 and 6 days post infection through differential expression.

Step 1: downloading SRR paired-end fastq files using sra-toolkit: SRR5660030, SRR5660033, SRR5660044, SR5660045

SRR...30: donor 1, 2dpi

SRR...33: donor 1, 6dpi

SRR...44: donor 3, 2dpi

SRR...45: donor 3, 6dpi

```{r}
#run in command line
fasterq-dump --split-3 SRR5660030
```

Clone this github, and run the wrapper script. It will produce various intermediate files, and a log file summarizing the analysis.

Run the wrapper script inside the github directory (/home/user/compbio_pipeline_project/wrapper.py). Arguments required: sample numbers, sample directory, output directory, log file name
```{r}
#list all SRR sample numbers comma-delimited
#example command
python3 wrapper.py --samples SRR5660030,SRR5660033,SRR5660044,SRR5660045 --inpath /home/igregga/compbio_pipeline_project/SRR_files --outdir /home/igregga/PipelineProject_Gregga_Isadore --outlog PipelineProject.log
```

Dependencies: this pipeline uses Biopython Seq.IO, Entrez, Seq, and SeqRecord; python packages argparse, sys, subprocess, os, and statistics; R packages dplyr, stringr, data.table, argparse, and sleuth; Unix command line tools kallisto, datasets, and blast+ (makeblastdb and tblastn).
