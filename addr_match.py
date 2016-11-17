# 
#


import sys, csv
from sys import argv

script, masterListFilename, recentlySoldFilename = argv

def loadAddrMaster(filename):
 	with open(filename, 'r') as csvfile:
		myReader = csv.reader(csvfile)
		addrDBList = []
		for row in myReader:
			rowTuple = row[0], row[2].strip(), row[1].strip(), row[3].strip()
			addrDBList.append(rowTuple)
	return addrDBList

def loadRecentSales(filename):
 	with open(filename, 'rU') as csvfile:
		myReader = csv.reader(csvfile)
		addrDBList = []
		for row in myReader:
			rowTuple = row[0], row[1].strip(), row[4]
			addrDBList.append(rowTuple)
	return addrDBList

def findOneAPN(stAddr, zipCode, addrDBList):
	for addr in addrDBList:
		if(addr[2]): # does address have a suite number, if so, append it in the Corelogic way
			coreLogicStyleStAddr = addr[1]+'  '+addr[2]
		else:
			coreLogicStyleStAddr = addr[1]
		stAddr = stAddr.upper()
		if (coreLogicStyleStAddr == stAddr) and (addr[3] == zipCode):
			return addr[0]
	return False

def matchAPNs(recentSaleList, addrMasterList):
	for recentSale in recentSaleList:
		recentSaleIndex = recentSale[0]
		recentSaleStAddr = recentSale[1]
		recentSaleZipCode = recentSale[2]
		recentSaleAPN = findOneAPN(recentSaleStAddr, recentSaleZipCode, addrMasterList)
#		print recentSaleIndex, recentSaleStAddr, recentSaleZipCode
		print '%s, %s, %s, %s' % (recentSaleIndex, recentSaleStAddr, recentSaleZipCode, recentSaleAPN)


addrMasterList = loadAddrMaster(masterListFilename)
recentSaleList = loadRecentSales(recentlySoldFilename)
#print recentlySoldList
matchAPNs(recentSaleList, addrMasterList)

#print findAPN('9551 E REDFIELD RD  1019','85260', addrMasterList)

