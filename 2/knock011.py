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

s1 = cmdline('expand ../data/hightemp.txt' ).stdout.readline()

with open('../data/hightemp.txt') as f:
    s2 = (f.read().replace('\t', ' '))
    print s2
    for buf in difflib.context_diff(s1, s2):
    	print buf

    

