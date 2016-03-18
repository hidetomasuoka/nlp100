# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
n = int(argvs[1])
f = open('../data/hightemp.txt','r')

for line, index in zip(f,xrange(n)):
    print line,
    if n == index: break
