import math
import numpy as np
import scipy.stats 
import random

def normal_seq_gen(n):

    seq1 = np.random.standard_normal(n)
    seq2 = np.random.standard_normal(n)

    return seq1, seq2

rand_var_1, rand_var_2 = normal_seq_gen(1000)


###### E(a), in assumption 