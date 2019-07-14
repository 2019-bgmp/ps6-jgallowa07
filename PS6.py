#!/usr/bin/env python3
import re
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='This file is for PS5 for UO BGMP. We are creating and counting kmers')
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help='file to parse')
parser.add_argument('-o', type=str, help='where to output buckets')
args = parser.parse_args()


K_MER_LENGTH = 49

sum_nucleotides_from_header = 0
num_contigs = 0
max_contig_length = 0
mean_contig_length = 0
total_contig_length = 0
kmer_coverages_sum = 0
contig_lengths = []

k_mer_lengths = []
k_mer_coverages = []
with open(args.f,"r") as fafp:
    for line in fafp:
        if line[0] == ">":
            matches = re.match(".+_.+_.+_(.+)_.+_(.+)",line)    
            k_mer_length = int(matches.groups()[0])
            k_mer_coverage = float(matches.groups()[1])
            k_mer_lengths.append(k_mer_length)
            k_mer_coverages.append(k_mer_coverage)
            kmer_coverages_sum += k_mer_coverage
            contig_length = k_mer_length + K_MER_LENGTH - 1
            contig_lengths.append(contig_length)
            max_contig_length = max(max_contig_length, contig_length)
            sum_nucleotides_from_header += contig_length
            num_contigs += 1

mean_contig_length = sum_nucleotides_from_header / num_contigs
kmer_coverage_mean = kmer_coverages_sum / num_contigs

contig_lengths.sort()
running_sum = 0
N50 = 0
for length in contig_lengths:
    running_sum += length
    if running_sum > (sum_nucleotides_from_header/2):
        N50 = length
        break

bucket_size = 100
length_counts = defaultdict(int)
for length in contig_lengths:
    lower = length // bucket_size
    length_counts[lower*bucket_size] += 1

if args.o != None:
    out_fi = open(args.o,"w")
    for key in sorted(length_counts):
        out_fi.write(f"{key}\t{length_counts[key]}\n")
else:
    print("# contig length\tNumber of contigs in this category")
    for key in sorted(length_counts):
        print(f"{key}\t{length_counts[key]}")

print("total length: ", sum_nucleotides_from_header)
print("num contigs: ", num_contigs)
print("max contig len: ",max_contig_length)
print("mean contig length: ",mean_contig_length)
print("mean coverage: ",kmer_coverage_mean)







            

            

