import argparse
import sys

#function to parse command line arguments
def check_arg(args=None):
    parser=argparse.ArgumentParser(description='differential expression pipeline')
    parser.add_argument('-s','--samples',help='SRR sample numbers',required='True')
    parser.add_argument('-p','--inpath',help='path to directory holding fastq samples',required='True')
    parser.add_argument('-l','--outlog',help='output log file name',required='True')
    parser.add_argument('-o','--outdir',help='output directory',required='True')
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args=check_arg(sys.argv[1:])
samples=args.samples
path=args.inpath
outlog=args.outlog
outdir=args.outdir
#path='/home/igregga/compbio_pipeline_project/SRR_files'
#samples='SRR5660030,SRR5660033,SRR5660044,SRR5660045'
#outlog='PipelineProject.log'
#outdir='/home/igregga/PipelineProject_Gregga_Isadore'

#using subprocess instead of os because of stackexchange recommendations
#makes it easy to capture command line output as a string in a variable. even tho i only do that twice i guess
#shell=True makes it work like os.system where it takes a string of what you'd type in the command line
#universal_newlines=True triggers the output to be string type instead of bytes. also adds newlines yay
import subprocess
import os

#establishing output directory
os.system('mkdir '+outdir)
#is it cheating to uhhhh move all intermediate output there? bcuz i want to just have this run in this directory? idk
#nooooo no i should add it as a real argumenttttt fine

#open log file to write
log=open(outdir+outlog,'a')

#02_build_index, need to send to outdir
step2=subprocess.check_output('python3 02_build_index/retrieve_reference.py --outdir '+outdir,shell=True,universal_newlines=True)
subprocess.run('./02_build_index/build_index.sh --outdir '+outdir,shell=True)

step2=step2.strip('\n')
log.write('The HCMV genome (NC_006273.2) has '+step2+' CDS.\n')

#03_calc_tpm, input args and send to outdir
command='./03_calc_tpm/calc_tpm.sh --path '+path+' --samples '+samples+' --outdir '+outdir
subprocess.run(command,shell=True)
command='python3 03_calc_tpm/process_abundance.py --samples '+samples+' --outdir '+outdir
step3=subprocess.check_output(command,shell=True,universal_newlines=True)

log.write(step3)

#04_find_diffex, inputs and send to outdir
command='Rscript 04_find_diffex/use_sleuth.R --samples '+samples+' --outdir '+outdir
subprocess.run(command,shell=True)

f=open(outdir+'sleuth_fdr0.05.txt','r')
diffex=f.read().rstrip()
log.write(diffex)
f.close()

#05_other_viruses, send to outdir
subprocess.run('python3 05_other_viruses/get_protein_fastas.py --outdir '+outdir,shell=True)
subprocess.run('./05_other_viruses/make_blast_db.sh --outdir '+outdir,shell=True)
subprocess.run('./05_other_viruses/run_blast.sh --outdir '+outdir,shell=True)

f=open(outdir+'blastresults.tsv','r')
blast=f.read().rstrip()
log.write(blast[0:10])

log.close()
