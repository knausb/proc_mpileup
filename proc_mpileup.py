#  !/usr/bin/env python

# https://docs.python.org/3/tutorial/
# https://docs.python.org/3/howto/argparse.html#id1
# http://code.activestate.com/recipes/362193/
# https://docs.scipy.org/doc/numpy/user/quickstart.html

import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description='Process gzipped samtools mpileup output.')
parser.add_argument("bams", help="Text file of bam files, one file per line.")
parser.add_argument("dir", help="Directory containing *mpileup.gz files.")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
                    
args = parser.parse_args()

##### ##### ##### ##### #####
# Functions

def read_bam(bams):
    """Read in the list of bam files."""
    with open(bams) as f:
        read_data = f.readlines()
#    f.closed
    return(read_data)


def clean_filenames(file_names):
    """Clean filenames (remove path, extension)."""
    # https://stackoverflow.com/a/8384788
    # https://stackoverflow.com/a/678242
    import ntpath
    import os
    my_list = ["oops"] * len(file_names)
    for i in range(len(file_names)):
        tmp = ntpath.basename(file_names[i])
        my_list[i] = os.path.splitext(tmp)[0]
#        print(i, my_list[i])
    return(my_list)


def mp_files(mypath):
    """Create a list from a directory of *mpileup.gz files."""
    # https://stackoverflow.com/a/3215392
    import glob
#    print(mypath)
    my_files = glob.glob(mypath + "*.mpileup.gz")
    return(my_files)

def summa_mpile(my_gz_file):
    """Read and summarize gzipped mpileup file."""
#    print(len(my_sample_names))
    my_cols = list(range(3, 3 * (len(my_sample_names) + 1), 3))
#    print(my_cols)
    my_input = np.loadtxt(my_gz_file, dtype = 'i', comments = None,
                          delimiter = '\t', usecols=my_cols)
    if my_input.shape[0] > 0:
#        print(my_input)
#        print("nparray shape:")
#        print(my_input.shape)
        my_colsums = my_input.sum(axis=0)
        my_stds = my_input.std(axis=0)
        my_input[ my_input > 0 ] = 1
        my_nonzero = my_input.sum(axis=0)
#        print(my_input.count_nonzero(axis=0))
        return(my_colsums, my_stds, my_nonzero)
    else:
        print(my_gz_file + " has zero rows.")
        return(0)

##### ##### ##### ##### #####
#
# Main.
#
##### ##### ##### ##### #####

if args.verbose:
    print("verbosity turned on")

if args.verbose:
    print("Input bam files: " + args.bams)
    print("Input directory: " + args.dir)

# Read in file of bam filenames.
my_bams = read_bam(args.bams)

if args.verbose:
    print("len(my_bams): ")
    print(len(my_bams))
    print("my_bams[0]: " + my_bams[0])


# Clean bam filenames to get sample names.
my_sample_names = clean_filenames(my_bams)

if args.verbose:
    for i in my_sample_names:
        print(i)


# Read directory of gzipped mpileup files to get names.
my_mp = mp_files(args.dir)
my_locus_names = clean_filenames(my_mp)

if args.verbose:
    print("len(my_mp): ")
    print(len(my_mp))
#    print(my_mp[1])


# Initialize data structures.
# https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe
count_df = pd.DataFrame(columns=[my_sample_names], index=[my_locus_names])
std_df = pd.DataFrame(columns=[my_sample_names], index=[my_locus_names])
nonzero_df = pd.DataFrame(columns=[my_sample_names], index=[my_locus_names])
#print(count_df)

# Read and summarize gzipped files.

for i in range(0, len(my_mp)):
    if args.verbose:
        print("Working on: "+ my_mp[i])
    my_summa = summa_mpile(my_mp[i])
#    print("Returned from summa")
    if my_summa == 0:
        print(my_mp[i])
        print("summa equal to zero, handling empty file.")
    else:
#    print(my_summa[0])
#    print(len(my_summa[0]))
#    print(count_df.loc[my_locus_names[i], my_sample_names]) #= my_summa[0]
        count_df.loc[my_locus_names[i], my_sample_names] = my_summa[0]
        std_df.loc[my_locus_names[i], my_sample_names] = my_summa[1]
        nonzero_df.loc[my_locus_names[i], my_sample_names] = my_summa[2]


# Print to file.
count_df.to_csv("counts.csv")
std_df.to_csv("std.csv")
nonzero_df.to_csv("nonzero.csv")


##### ##### ##### ##### #####
# EOF.
