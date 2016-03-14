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

f_col1 = open('./col1.txt','r')
f_col2 = open('./col2.txt','r')


for col1, col2 in zip(f_col1, f_col2):
    print "%s %s" % ((col1.rstrip().decode('utf-8')),(col2.rstrip()).decode('utf-8'))

cmdline('paste ../data/cut1.txt ../data/cut2.txt > ../data/cut3.txt' ).stdout.readline()
    
