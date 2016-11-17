from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import csv
import sys

def getPropertyDetail(latlong):
#	print('latlong = ')
#	print(latlong)
	browser.get('http://www.esg.montana.edu/gl/xy-data.html')

	try:
		submitButton = browser.find_element_by_xpath('/html/body/form/input[2]')
#		element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(submitButton))
		inputBox = browser.find_element_by_name('xydt')	
		inputBox.send_keys(latlong)
		submitButton.click()
#		element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(By.XPATH, '/html/body/a[1]/img'))
		legalDescParagraph = browser.find_element_by_xpath('/html/body').text
		legalDescLines = legalDescParagraph.splitlines()
#		print('legalDesc = ')
#		print(legalDescLines[2])
	except:
		print("Unexpected error:", sys.exc_info()[0])
		print(latlong +' not loaded successfully.')
		return False

	else:
#		with open(txtStreetAddress+'.html', 'a') as htmlSnippetFile:
#			htmlSnippetFile.write(pageContentHTML.encode('utf8'))
		with open('latlongoutput.csv', 'a') as csvFile:
			myWriter = csv.writer(csvFile)
			data = [latlong, legalDescLines[2]]
			print(data)
			myWriter.writerow(data)
#			print('row written!')
		return True


##############
## starts here
##############

path_to_chromedriver = '/Users/pli/Desktop/selenium_scrape/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)


latlongListFile = open('latlongs.txt')
latlongList = latlongListFile.read().splitlines()
for latlong in latlongList:
	getPropertyDetail(latlong)
#	print('finished one!')
	seconds = .1 + (random.random() * .1)
	time.sleep(seconds)


# browser.quit()
