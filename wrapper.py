import argparse
import sys

#function to parse command line arguments
def check_arg(args=None):
    parser=argparse.ArgumentParser(description='differential expression pipeline')
    parser.add_argument('-s','--samples',help='SRR sample numbers',required='True')
    parser.add_argument('-p','--path',help='path to directory holding fastq samples')
    parser.add_argument('-o','--output',help='output log file name',required='True')
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args=check_arg(sys.argv[1:])
samples=args.samples
path=args.path
outlog=args.output
#path='SRR_files'
samples='SRR5660030,SRR5660033,SRR5660044,SRR5660045'
outlog='PipelineProject.log'

import subprocess

#open log file to write
log=open(outlog,'a')

#02_build_index, no args needed here
step2=subprocess.check_output('python3 02_build_index/retrieve_reference.py',shell=True,universal_newlines=True)
subprocess.run('./02_build_index/build_index.sh',shell=True)

step2=step2.strip('\n')
log.write('The HCMV genome (NC_006273.2) has '+step2+' CDS.\n')

#03_calc_tpm, deal with input args here
#samples=samples.split(',')
command='./03_calc_tpm/calc_tpm.sh --path '+path+' --samples '+samples
subprocess.run(command,shell=True)
command='python3 03_calc_tpm/process_abundance.py --samples '+samples
step3=subprocess.check_output(command,shell=True,universal_newlines=True)

log.write(step3)

#04_find_diffex
command='Rscript 04_find_diffex/use_sleuth.R --samples '+samples
subprocess.run(command,shell=True)

f=open('sleuth_fdr0.05.txt','r')
diffex<-f.read().rstrip()
log.write(diffex[0:10])

