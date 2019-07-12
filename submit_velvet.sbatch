#!/bin/bash
#SBATCH --account=bgmp          ### SLURM account which will be charged for the job
#SBATCH --partition=bgmp        ### Partition (like a queue in PBS)
#SBATCH --job-name=PS6          ### Job Name
#SBATCH --output=velvet.out         ### File in which to store job output
#SBATCH --error=velvet.err          ### File in which to store job error messages
#SBATCH --time=0-00:01:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job (usually 1)
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Node (usually 1)
#SBATCH --cpus-per-task=1       ### Number of cpus (cores) per task
#SBATCH --mail-user=jaredgalloway07@gmail.com
#SBATCH --mail-type=ALL

# Load modules

# SCRIPT BELOW
fq1=800_3_PE5_interleaved.fq_1
fq2=800_3_PE5_interleaved.fq_2
fq3=800_3_PE5_interleaved.fq.unmatched
velveth /output_directory 31 -fastq -shortPaired -seperate $fq1 $fq2 -fastq -short2 $fq3
