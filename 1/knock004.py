# coding: utf-8
# -*- coding: utf-8 -*-

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
array_s = s.split()
list_atom = []

for word, index in zip(array_s, xrange(len(array_s))):
# use python3
## for word, index in zip(array_s, range(len(array_s))):

    list_atom.append(word[0] if index+1 in (1, 5, 6, 7, 8, 9, 15, 16, 19) else word[0:2])

print list_atom