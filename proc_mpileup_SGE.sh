#!/bin/bash

#$ -cwd
#$ -S /bin/bash
#$ -N mpile
#$ -o proc_mpile_out
#$ -e proc_mpile_err
# $ -l mem_free=2G
#$ -V
# $ -q !(gbs|grungall1)
# $ -h
# $ -t 11-18179:1

# A few hints.
# https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html
# conda info --envs
# conda activate bjk_biopython

# bash arrays are zero based, SGE is one based.
# i=$(expr $SGE_TASK_ID - 1)

echo -n "Running on: "
hostname
echo "SGE job id: $JOB_ID"
echo "SGE_TASK_ID: $SGE_TASK_ID"

echo
echo "Path:"
echo $PATH
echo

date

export OMP_NUM_THREADS=1

# eval "bash"

# eval "/local/cluster/miniconda2/bin/conda activate ~/.conda/envs/bjk_biopython/"

# /local/cluster/miniconda2/condabin/conda ~/.conda/envs/bjk_biopython/


#
eval "python ~/gits/proc_mpileup/proc_mpileup.py ~/gits/proc_mpileup/bams.txt ~/gits/proc_mpileup/rep_pu -v"

#
eval "mv counts.csv ~/gits/proc_mpileup/counts.csv"

#
eval "mv std.csv ~/gits/proc_mpileup/std.csv"

#
eval "mv nonzero.csv ~/gits/proc_mpileup/nonzero.csv"

#eval "conda deactivate"

date

echo
echo "##### ##### ##### ##### #####"
echo

# EOF.
