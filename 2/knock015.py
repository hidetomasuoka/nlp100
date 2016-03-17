# -*- coding: utf-8 -*-

import sys

argvs = sys.argv
n = int(argvs[1])+1

f = open('../data/hightemp.txt','r')
f_arr = f.read().split("\n")
f_len = len(f_arr)

for i in range(f_len-n, f_len):
    print f_arr[i]