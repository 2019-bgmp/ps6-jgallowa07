#!/bin/bash
#SBATCH --account=bgmp          ### SLURM account which will be charged for the job
#SBATCH --partition=bgmp        ### Partition (like a queue in PBS)
#SBATCH --job-name=PS6          ### Job Name
#SBATCH --output=velvet.out         ### File in which to store job output
#SBATCH --error=velvet.err          ### File in which to store job error messages
#SBATCH --time=0-01:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job (usually 1)
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Node (usually 1)
#SBATCH --cpus-per-task=8       ### Number of cpus (cores) per task
#SBATCH --mail-user=jaredgalloway07@gmail.com
#SBATCH --mail-type=ALL

# Load modules

# SCRIPT BELOW
fq1=800_3_PE5_interleaved.fq_1
fq2=800_3_PE5_interleaved.fq_2
fq3=800_3_PE5_interleaved.fq.unmatched
rd=output_dir/

#Part 1
for k in 31 41 49
do
    /usr/bin/time -v velveth output_dir \
        $k -fastq -shortPaired -separate $fq1 $fq2 -fastq -short2 $fq3
    /usr/bin/time -v velvetg output_dir \
        -exp_cov 98.5912995
    #./PS6.py -f output_dir/contigs.fa
        # -o output_dir_$k/contig_analysis.txt.k$k
    ./PS6.py -f output_dir/contigs.fa \
        -kl $k
done

#Part 2
for cc in 20 60 auto
do
    /usr/bin/time -v velveth output_dir \
        49 -fastq -shortPaired -separate $fq1 $fq2 -fastq -short2 $fq3
    /usr/bin/time -v velvetg output_dir \
        -exp_cov 98.5912995 -cov_cutoff $cc
    #./PS6.py -f output_dir/contigs.fa
        # -o output_dir_$k/contig_analysis.txt.k$k
    ./PS6.py -f output_dir/contigs.fa \
        -kl 49 -cc $cc
done

#Part 3
/usr/bin/time -v velveth output_dir \
    49 -fastq -shortPaired -separate $fq1 $fq2 -fastq -short2 $fq3
/usr/bin/time -v velvetg output_dir \
    -exp_cov 98.5912995 -cov_cutoff auto -min_contig_lgth 500
./PS6.py -f output_dir/contigs.fa \
    -kl 49 -cc auto -min_contig_lgth 500











