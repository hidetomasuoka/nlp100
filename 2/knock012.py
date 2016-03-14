# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subprocess import PIPE, Popen

import difflib

def cmdline(command):
    """
    コマンドを実行する。shell=Trueの場合シェル経由で実行する。
    :param command: str
    :return: Popen
    """
    return Popen(
        args=command,
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )

f = open('../data/hightemp.txt', 'r')

f_col1 = open('./col1.txt','w')
f_col2 = open('./col2.txt','w')

for line in f:
    col1, col2, temperature, timestamp = line.decode('utf-8').split("\t")
    f_col1.write(("%s\n" % col1).encode('utf-8'))
    f_col2.write(("%s\n" % col2).encode('utf-8'))


cmdline('cat ../data/hightemp.txt | cut f1 > ../data/cut1.txt' ).stdout.readline()
cmdline('cat ../data/hightemp.txt | cut f2 > ../data/cut2.txt' ).stdout.readline()

