#process kallisto out with sleuth package
#args: srr samples
#aaaaand outdir
library(dplyr)
library(data.table)
library(sleuth)
library(argparse)
library(stringr)

parser<-ArgumentParser()
parser$add_argument("-s", "--samples", type="character")
parser$add_argument('-o','--outdir',type='character')
args<-parser$parse_args()
samples<-args$samples
samples<-str_split(samples,',')[[1]]
outdir<-args$outdir

#samples<-c('SRR5660030','SRR5660033','SRR5660044','SRR5660045')

#create table for sleuth input
intable<-data.frame(matrix(nrow=length(samples),ncol=3))
colnames(intable)<-c('sample','condition','path')
intable$sample<-samples

#this is hard coded? idk? how else to attach the dpi condition info?
for (i in 1:length(samples)){
  if (intable[i,1]=='SRR5660030'){
    intable[i,2]='2dpi'
  }else if(intable[i,1]=='SRR5660044'){
    intable[i,2]='2dpi'
  }else if(intable[i,1]=='SRR5660033'){
    intable[i,2]='6dpi'
  }else if(intable[i,1]=='SRR5660045'){
    intable[i,2]='6dpi'
  }
  intable[i,3]<-samples[i]
}

for (sample in intable$samples){
  str_sub(intable$sample,start=0,end=0)<-paste(outdir,'/',sep='')
}
  
fwrite(intable,paste(outdir,'/intable.txt',sep=''),quote=F,row.names=F,sep='\t')

#do the sleuthing
stab<-fread(paste(outdir,'/intable.txt',sep=''),header=T)
so<-sleuth_prep(stab)
#model to compare 2 to 6dpi
so<-sleuth_fit(so,~condition,'full')
so<-sleuth_fit(so,~1,'reduced')
#likelihood ratio test
so<-sleuth_lrt(so,'reduced','full')

#looking at results
sleuthtable<-sleuth_results(so,'reduced:full','lrt',show_all=F)
sleuthsig<-filter(sleuthtable,qval<=0.05)%>%arrange(pval)

#results to print to log file: target_id test_stat pval qval
sigwrite<-select(sleuthsig,target_id,test_stat,pval,qval)
fwrite(sigwrite,paste(outdir,'/sleuth_fdr0.05.txt',sep=''),quote=F,row.names=F,sep='\t')
