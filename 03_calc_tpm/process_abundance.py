#calculate minimum, medium, mean, maximum TPM for each sample from abundance.tsv kallisto output
#args: srr samples again

#kallisto out:
#target_id length eff_length est_counts tpm

infile='SRR5660030/abundance.tsv'

inlist = open(infile,'r').read().rstrip().split('\n')
#inlist[0] is colnames. rest of items are one line WITH tab delim chrs between cols

#get all tpms
tpmlist=[]
for line in inlist[1:]:
    row=line.split('\t')
    tpm=row[4]
    tpm=float(tpm)
    tpmlist.append(tpm)

import statistics as stat

meantpm=stat.mean(tpmlist)
mediantpm=stat.median(tpmlist)
mintpm=min(tpmlist)
maxtpm=max(tpmlist)


