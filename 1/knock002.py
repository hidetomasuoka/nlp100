# coding: utf-8
# -*- coding: utf-8 -*-

s1 = u"パトカー"
s2 = u"タクシー"
s3 = u''

print(''.join([char1 + char2 for char1, char2 in zip(s1, s2)]))