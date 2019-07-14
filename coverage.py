#!/usr/bin/env python3
import re
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='This \
    this script will take in multiple fastq files, a genome length \
    and an optional kmer length in order to calculate expected \
    coverage and (optionally) Expected K-mer coverage')
parser = argparse.ArgumentParser()
parser.add_argument(
    '-gl', type=int, help='genome length')
parser.add_argument(
    '-k', type=int, help='[k-mer length]')
parser.add_argument(
    '-fastq', type=str, help='fast q files to process', nargs='+')
args = parser.parse_args()

def sequence_iterator():
    for fqf in args.fastq:
        fqfp = open(fqf,"r")
        for idx,line in enumerate(fqfp):
            if idx % 4 == 1:
                yield line.strip()

iter1 = sequence_iterator()
num_bp = 0
for num_read,read in enumerate(iter1):
    num_bp += len(read)    
coverage = num_bp / args.gl
print(f"coverage is: {coverage}")

#Ck =C*(L-K+1)/L
if args.k != None:  
    read_length_mean = num_bp / num_read
    C_k = coverage * (read_length_mean - args.k + 1) / read_length_mean
    print(f"kmer coverage is {C_k}")
