# coding: utf-8
# -*- coding: utf-8 -*-

s = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s2 = []
words = s.split(" ")

for word in words:
	s2.append(len(word))

print(s2)