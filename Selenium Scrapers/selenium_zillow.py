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
		element = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lead-form-submit-button_contact-tall"]')))
		address0 = browser.find_element_by_class_name('zsg-content-header addr').text.strip()
		address1 = browser.find_element_by_class_name('breadcrumb-wrapper').text.strip()
		
#				//*[@id="yui_3_18_1_1_1450912847129_3615"]
#				//*[@id="yui_3_18_1_1_1450912847129_3952"]
#				//*[@id="yui_3_18_1_1_1450913368789_3137"]
#				//*[@id="yui_3_18_1_1_1450913368789_3473"]
#				//*[@id="yui_3_18_1_2_1450912784064_2821"]

		listingAgent = browser.find_element_by_class_name('zsg-media-bd').text.strip()


				//*[@id="yui_3_18_1_1_1450912847129_9037"]

		zestimate =  browser.find_element_by_class_name('zest-value').text.strip()
		zestLow =  browser.find_element_by_class_name('zest-range-bar-low').text.strip()
		zestHigh =  browser.find_element_by_class_name('zest-range-bar-high').text.strip()


#				//*[@id="yui_3_18_1_1_1450912847129_9067"]
#				//*[@id="yui_3_18_1_1_1450912847129_9202"]
#				//*[@id="yui_3_18_1_1_1450913368789_3480"]
	
#		lastSoldDate = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_SoldDate"]').text.strip()
#		lastSoldPrice = browser.find_element_by_xpath('//*[@id="tdSalePriceVal"]').text.strip()
#		propertyType = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_PropertyType"]').text.strip()
#		yearBuilt = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_YearBuilt"]').text.strip()

#		CommunityName = //*[@id="house-info"]/div[3]/div/div[2]/table[1]/tbody/tr[2]/td[2]


#		livingSquareFeet = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_LivingSquareFeet"]').text.strip()
#		totalSquareFeet = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_TotalSquareFeet"]').text.strip()
#		latlong = browser.find_element_by_xpath('//*[@id="plcMain_rptrProperties_ctl01_Address"]/a').get_attribute('onclick')
#		latlong = latlong[21:-16]
#		APN = //*[@id="property-details-scroll"]/div/div[2]/div[1]/div[4]/div[2]/div[2]/ul/li[5]/span[2]

		pageContentElement = browser.find_element_by_xpath('//*[@id="hdp"]')
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


propertyListFile = open('propertyURLsLong.txt')
propertyList = propertyListFile.read().splitlines()
for propertyURL in propertyList:
	getPropertyEstimate(propertyURL)
	print('finished one!')
	seconds = 3 + (random.random() * 3)
	time.sleep(seconds)

print('done!')
# browser.quit()
