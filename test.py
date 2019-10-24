

import numpy as np
import pandas as pd

my_cols = list(range(3, 3 * (99 + 1), 3))


my_input = np.loadtxt("rep_pu/gypsy_00001.mpileup.gz", dtype = 'i', comments = None, delimiter = '\t', usecols=my_cols)


my_input = np.loadtxt("rep_pu/gypsy_13810.mpileup.gz", dtype = 'i', comments = None, delimiter = '\t', usecols=my_cols)

my_input = np.loadtxt("rep_pu/gypsy_40825.mpileup.gz", dtype = 'i', comments = None, delimiter = '\t', usecols=my_cols)

#my_input = pd.read_csv("rep_pu/gypsy_00001.mpileup.gz", sep = "\t")
#my_input = pd.read_csv("rep_pu/gypsy_13810.mpileup.gz", sep = "\t")


