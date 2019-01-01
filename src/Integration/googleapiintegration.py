import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import string, random, time



#------------------------------------Data Collection--------------------------------------#
url = ""
request = requests.get(url)  # <---------- Move this into a seperate function
html_content = request.text
soup = BeautifulSoup(html_content, "html.parser")
# Fid the tag and its attribute
y = soup.findAll("div", class_="paragraph")
str(y)

names = []
def scrape():
    links = (soup.find_all("a"))
    y = [] #Note: For for loops, when using a list, initialize the list before starting the loop.
    for link in links:
    	y.append(link.get('href'))

    print(y)	
	
    		
    	
    

#----------------------------Auth-------------------------------------------------------#
#scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']﻿
         #'https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('file.json', scope)
#client = gspread.authorize(creds)

#retrieved = sheets.get_all_records()
#pprint.PrettyPrinter().pprint(retrieved)



#-----------------------------Functions---------------------------------------------------#

def namecollect(websiteurl):
	b = websiteurl.split(".")
	#print(b[0])
	e = (b[0])
	str(e)
	#print(e)
	h = e.split("/")
	r = h[2]
	#print(r)
	
	def findtext(websiteurl):
	para = soup.body.findAll(text=re.compile(''))
	para2 = soup.body.findAll(text=re.compile(''))
	paracombine = para + para2
	print(paracombine)
	if "" or "" in paracombine:
		return True
	else:
		return False

#-----------------------------Google Sheets Display--------------------------------------#






#sheets.update_cell(1,1, "" )
#sheets.update_cell(1,3, "Contains Website Content")
#sheets.update_cell(1,4, "Contains Picture")
#sheets.update_cell(1,5, "Website Contains Required links")
#sheets.update_cell(1,6, " ")

namecollect(url)


