# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subprocess import PIPE, Popen

data = '../data/hightemp.txt'


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


print len(open(data).readlines())
print cmdline('wc -l ../data/hightemp.txt' ).stdout.readline()