from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import csv
import sys

def getPropertyEstimate(url):
	print("url = ")
	print(url)
	browser.get(url)

######
## not DONE!!!  watch out for active vs pending vs sold listing format differences!

	try:
		element = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerUnifiedSearch"]/div/form/div/input)')))
		streetAddress = browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/h1/span/span[1]/span[1]').text
				//*[@id="public-records-scroll"]/div/div[1]/h2/span[2]/span[2]

		Estimate = browser.find_element_by_xpath('//*[@id="redfin-estimate"]/div/div[1]/div[1]/div[1]/div[1]/div[1]').text.strip()
		EstimateRange = browser.find_element_by_xpath('//*[@id="lblValue"]').text.strip()		
		lastSoldDate = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_SoldDate"]').text.strip()
		lastSoldPrice = browser.find_element_by_xpath('//*[@id="tdSalePriceVal"]').text.strip()
		propertyType = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_PropertyType"]').text.strip()
		yearBuilt = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_YearBuilt"]').text.strip()
//*[@id="house-info"]/div[3]/div/div[2]/table[2]/tbody/tr[3]/td[2]
//*[@id="content"]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div/div/span[1]/span[2]
//*[@id="basicInfo"]/div/table[1]/tbody/tr[4]/td[2]

		CommunityName = //*[@id="house-info"]/div[3]/div/div[2]/table[1]/tbody/tr[2]/td[2]


		livingSquareFeet = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_LivingSquareFeet"]').text.strip()
		totalSquareFeet = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_TotalSquareFeet"]').text.strip()
		latlong = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_Address"]/a').get_attribute('onclick')
		latlong = latlong[21:-16]
		APN = //*[@id="property-details-scroll"]/div/div[2]/div[1]/div[4]/div[2]/div[2]/ul/li[5]/span[2]


		//*[@id="basicInfo"]/div/div/div[2]/span[2]
		pageContentElement = browser.find_element_by_xpath('//*[@id="divContent01"]')
		pageContentHTML = pageContentElement.get_attribute('innerHTML')

MLSNum = 
//*[@id="basicInfo"]/div/table[1]/tbody/tr[4]/td[2]


	except:
		print("Unexpected error:", sys.exc_info()[0])
		print(url +' not loaded successfully.')
		return False

	else:
		with open(txtStreetAddress+'.html', 'a') as htmlSnippetFile:
			htmlSnippetFile.write(pageContentHTML.encode('utf8'))
		with open('output.csv', 'a') as csvFile:
			myWriter = csv.writer(csvFile)
			data = [txtStreetAddress, tdOrigValue, lblValue, lastSoldDate, lastSoldPrice, propertyType, yearBuilt, livingSquareFeet, totalSquareFeet, latlong]
			print(data)
			myWriter.writerow(data)
		return True


##############
## starts here
##############

path_to_chromedriver = '/Users/pli/Desktop/selenium_try/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)


propertyListFile = open('propertyURLs.txt')
propertyList = propertyListFile.read().splitlines()
for propertyURL in propertyList:
	getPropertyEstimate(propertyURL)
	print('finished one!')
	seconds = 3 + (random.random() * 3)
	time.sleep(seconds)

print('done!')
# browser.quit()
