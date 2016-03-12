# -*- coding: utf-8 -*-

import sys 

argvs = sys.argv
argv = argvs.encode('utf-8')
argc = len(argvs)
print argc

if(argc != 4):
	print 'Usage: this program use three arguments' 
	quit()

print(argv[1] + u"時の" + argv[2] + u"は" + argvs[3])