# -*- coding: utf-8 -*-

import random

input_text = u"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typolycemia(string):
	input_text_to_arr = input_text.split()

	for word in input_text_to_arr:
		if len(word) > 4 :
			top = word[0]
			tail = word[-1]
			text_list = list(word[1:-1])
			random.shuffle(text_list)
			print "%s%s%s" % (top, ''.join(text_list), tail),

		else:
			print word,

typolycemia(input_text)