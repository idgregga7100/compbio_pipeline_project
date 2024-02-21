#process kallisto out with sleuth package
#args: srr samples
library(dplyr)
library(data.table)
library(sleuth)

samples<-c('SRR5660030','SRR5660033','SRR5660044','SRR5660045')

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

fwrite(intable,'intable.txt',quote=F,row.names=F,sep='\t')

#do the sleuthing
stab<-fread('intable.txt',header=T)
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
fwrite(sigwrite,'sleuth_fdr0.05.txt',quote=F,row.names=F,sep='\t')
