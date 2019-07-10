#!/usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(description='This file is for PS5 for UO BGMP. We are creating and counting kmers')
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help='file to parse')
args = parser.parse_args()

K_MER_LENGTH = 49

sum_nucleotides_from_header = 0
num_contigs = 0
max_contig_length = 0
mean_contig_length = 0
total_contig_length = 0
contig_legths = []

k_mer_lengths = []
k_mer_coverages = []
with open(args.f,"r") as fafp:
    for line in fafp:
        if line[0] == ">":
            matches = re.match(".+_.+_.+_(.+)_.+_(.+)",line)
            k_mer_lengths.append(int(matches.groups()[0]))
            k_mer_coverages.append(float(matches.groups()[1]))
            contig_length = int(matches.groups()[0]) + K_MER_LENGTH - 1
            contig_lengths.append(contig_length)
            max_contig_length = max(max_contig_length, contig_length)
            sum_nucleotides_from_header += contig_length
            num_contigs += 1

mean_contig_length = total_contig_length / num_contigs







            

            

