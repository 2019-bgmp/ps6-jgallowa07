#!/usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(description='This file is for PS5 for UO BGMP. We are creating and counting kmers')
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help='file to parse')
args = parser.parse_args()

k_mer_lengths = []
k_mer_coverages = []
with open(args.f,"r") as fafp:
    for line in fafp:
        if line[0] == ">":
            matches = re.match(".+_.+_.+_(.+)_.+_(.+)",line)
            k_mer_lengths.append(int(matches.groups()[0]))
            k_mer_coverages.append(float(matches.groups()[1]))

            

