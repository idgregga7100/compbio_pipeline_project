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

To run wrapper:
```{r}
#list all SRR sample numbers comma-delimited
#example command
python3 wrapper.py --samples SRR5660030,SRR5660033 --path SRR_files --output PipelineProject.log
```
