#calculate minimum, medium, mean, maximum TPM for each sample from abundance.tsv kallisto output
#args: srr samples again

#kallisto out:
#target_id length eff_length est_counts tpm
import argparse
import sys

#function to parse command line arguments
def check_arg(args=None):
    parser=argparse.ArgumentParser(description='differential expression pipeline')
    parser.add_argument('-s','--samples',help='SRR sample numbers',required='True')
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args=check_arg(sys.argv[1:])
samples=args.samples
samples=samples.split(',')

print('\t'.join(['sample','min_tpm','med_tpm','mean_tpm','max_tpm']))

for sample in samples:
    infile=sample+'/abundance.tsv'

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
    print('\t'.join([sample,str(mintpm),str(mediantpm),str(meantpm),str(maxtpm)]))


