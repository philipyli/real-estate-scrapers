import re
import sys
import csv
from sys import argv

script, rawAPNFilename, APNOutputFilename = argv


def loadAPNFile(filename):
	APNList = []
 	with open(filename, 'rU') as APNfile:
 		for line in APNfile:
			APNList.append(line.strip())
	return APNList

def cleanAPN(rawAPN, myWriter):
	row = []
	m = re.match(r'([0-9]{1,4})([a-zA-Z]?)([0-9]{3})([a-zA-Z]?)', rawAPN)
	row.append(rawAPN)
	print "%s," % rawAPN,
	if(m):
		row.append('%04d%01s%03d%01s' % (int(m.group(1)), m.group(2), int(m.group(3)), m.group(4)))
	myWriter.writerow(row)

APNList = loadAPNFile(rawAPNFilename)
with open(APNOutputFilename, 'w') as APNOutputFile:
	myWriter = csv.writer(APNOutputFile)
	for nextAPN in APNList:
		cleanAPN(nextAPN, myWriter)