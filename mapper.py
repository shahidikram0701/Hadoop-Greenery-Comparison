from os import sys
import numpy as np

gcolor="green"
ngcolor="non-green"
count=0

for line in sys.stdin:
	data = line.strip().split("\t")
	data = list(map(int, data))
	blue, green, red = data
	if((blue>=0 and blue<=60) and (green>=0 and green<=255) and (red>=0 and red<=60)):
		print "{0}\t{1}".format(gcolor,1)
	else:
		print "{0}\t{1}".format(ngcolor,1)



	
	
	
 	
