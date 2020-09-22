#!/usr/bin/python

# https://docs.python.org/3/tutorial/
# https://docs.python.org/3/howto/argparse.html#id1

import argparse

parser = argparse.ArgumentParser(description='Determine nucleotide composition of FASTA files.')
parser.add_argument("FASTA", help="FASTA file.")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
                    
args = parser.parse_args()

##### ##### ##### ##### #####
# Functions


##### ##### ##### ##### #####
#
# Main.
#
##### ##### ##### ##### #####

if args.verbose:
    print("verbosity turned on")

if args.verbose:
    print("Input FASTA file: " + args.FASTA)




# EOF.