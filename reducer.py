from os import sys

total=0
greenTotal=0
oldKey=None
full_total=0
green_percentage="Green percentage in this image"

for line in sys.stdin:
	data=line.strip().split("\t")
	thisKey,thisValue=data
	if oldKey and oldKey!=thisKey:
		print "{0}\t{1}".format(oldKey,total)
		greenTotal=total
		total=0
	oldKey=thisKey
	total=total + int(thisValue)
	full_total=full_total + int(thisValue)

if oldKey!=None:
	percent=round((greenTotal/float(full_total) * 100), 3)
	cubbon_park = 62.002 # Found by running the code individually on cubbon park image
	comparison = round(((percent / cubbon_park) * 100), 3)
	print "{0}\t{1}".format("Green percentage in Cubbon Park", cubbon_park)
	print "{0}\t{1}".format(green_percentage, percent)
	print "{0}\t{1}".format("Comparison with Cubbon park", comparison)