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
#def scrape():
    #links = (soup.find_all("a"))
    #for link in links: #Find a href tag in the a tag
    	#y = []
    	#y.append(link.get('href'))
    #return 	
    		
    	
    

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
	
	#if r in names:
		#print(True)
		#print(r) 
	#else:
		#print(False)
		#return 0

	a = len(r)
	random.seed(time)
	rand1 = random.randrange(0, a)
	rand2 = random.randrange(0, a)
	rand3 = random.randrange(0, a)
	rand4 = random.randrange(0, a)
	#rand5 = random.randrange(0, a)
	#rand6 = random.randrange(0, a)

	list(r)
	r1 = r[rand1]
	r2 = r[rand2]
	r3 = r[rand3]
	r4 = r[rand4]
	#r5 = r[rand5]
	#r6 = r[rand6]
	print(r)
	print(r1, r2, r3, r4)
	rlist = []
	rlist.append(r1)
	rlist.append(r2)
	rlist.append(r3)
	rlist.append(r4)

	#asdjke = ""
	#str(asdjke)

	#if r1 and r2 and r3 and r4 in names:
		#print(True)
	#else:
		#print(False)

	for i in names:
		print(i.lstrip(r1) and i.lstrip(r2) and i.lstrip(r3) and i.lstrip(r4)) 
#-----------------------------Google Sheets Display--------------------------------------#






#sheets.update_cell(1,1, "" )
#sheets.update_cell(1,3, "Contains Website Content")
#sheets.update_cell(1,4, "Contains Picture")
#sheets.update_cell(1,5, "Website Contains Required links")
#sheets.update_cell(1,6, " ")

namecollect(url)


