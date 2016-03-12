# -*- coding: utf-8 -*-

import re

str1 = raw_input()

def cipher(string):

	str2 = ''
	for char in str1:
		str2 += chr(219-ord(char)) if re.search(r"[a-z]",char) else char

	return str2

print cipher(str1)