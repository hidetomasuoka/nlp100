# coding: utf-8

def ngram(n, mode, string):

	if mode =='char':
		feture_list = [char for char in string]
	else:
		feture_list = string.split()

	ngram_list = []

	for i in xrange(len(feture_list) - n+1):
		temp_ngram_list = []
		for j in xrange(n):
			temp_ngram_list.append(feture_list[i+j])

		ngram_list.append(''.join(temp_ngram_list))
	return ngram_list

if __name__ == '__main__':
	n = 2
	string = u"I am an NLPer"
	print(ngram(n, 'word', string))
	print(ngram(n, 'char', string))

