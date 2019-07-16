#!/usr/bin/env python3
import re
import argparse
from collections import defaultdict
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description='This file is for PS5 for UO BGMP. We are creating and counting kmers')
parser = argparse.ArgumentParser()

parser.add_argument('-f', type=str, help='file to parse')
parser.add_argument('-o', type=str, help='where to output buckets')
parser.add_argument('-kl', type=int, help='kmer_length')
parser.add_argument('-cc', type=str, help='coverage cutoff')
parser.add_argument('-min_contig_lgth', type=str, help='min contig length')

args = parser.parse_args()


K_MER_LENGTH = args.kl

# initialize variables
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
            
            # pretty terrible way to do this but it works ...
            matches = re.match(".+_.+_.+_(.+)_.+_(.+)",line)    
            k_mer_length = int(matches.groups()[0])
            k_mer_coverage = float(matches.groups()[1])
            k_mer_lengths.append(k_mer_length)
            k_mer_coverages.append(k_mer_coverage)
            kmer_coverages_sum += k_mer_coverage

            # Algebra from num_kmers = len(seq) + len(k) + 1
            contig_length = k_mer_length + K_MER_LENGTH - 1
            contig_lengths.append(contig_length)
            max_contig_length = max(max_contig_length, contig_length)
            sum_nucleotides_from_header += contig_length
            num_contigs += 1

# final calcs
mean_contig_length = sum_nucleotides_from_header / num_contigs
kmer_coverage_mean = kmer_coverages_sum / num_contigs

# weighted median
contig_lengths.sort()
running_sum = 0
N50 = 0
for length in contig_lengths:
    running_sum += length
    if running_sum > (sum_nucleotides_from_header/2):
        N50 = length
        break

# common way to bucket a list of numbers 
bucket_size = 100
length_counts = defaultdict(int)
for length in contig_lengths:
    lower = length // bucket_size
    length_counts[lower*bucket_size] += 1

if args.o != None:
    out_fi = open(args.o,"w")
    out_fi.write(f"{sum_nucleotides_from_header}\t{num_contigs}\t \
        {max_contig_length}\t{mean_contig_length}\t{kmer_coverage_mean}\t{N50}\n")
    for key in sorted(length_counts):
        out_fi.write(f"{key}\t{length_counts[key]}\n")
else:
    print("# contig length\tNumber of contigs in this category")
    for key in sorted(length_counts):
        print(f"{key}\t{length_counts[key]}")

# Print stats
print("N50: ", N50)
print("total length: ", sum_nucleotides_from_header)
print("num contigs: ", num_contigs)
print("max contig len: ",max_contig_length)
print("mean contig length: ",mean_contig_length)
print("mean coverage: ",kmer_coverage_mean)

# going to plot here so it plots during run of all parameters
params_for_plot = f"$k$={args.kl} | cc={args.cc} | mcl={args.min_contig_lgth}"
plot_name = f"k{args.kl}_cc{args.cc}_mcl{args.min_contig_lgth}.pdf"
stats_for_plot = f"N50 = {N50}"

fig, ax = plt.subplots(1)
ax.plot(list(length_counts.keys()),list(length_counts.values()))

ax.set_title("Contig length distribution\nvelvetg Params: "+params_for_plot)
ax.set_xlabel("bucket size")
ax.set_ylabel("Number of contigs in this bucket")
ax.legend([f"N50={N50}"])
plt.xscale("log")
plt.yscale("log")
fig.savefig("plots/"+plot_name)



