import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

#------------------------------------Data Collection--------------------------------------#
url = ""
request = requests.get(url)  # <---------- Move this into a seperate function
html_content = request.text
soup = BeautifulSoup(html_content, "html.parser")
# Fid the tag and its attribute
y = soup.findAll("div", class_="paragraph")
str(y)


def scrape():
    #links = (soup.find_all("a"))
    #for link in links: #Find a href tag in the a tag
    	#y = []
    	#y.append(link.get('href'))
    	
    		
    	
    

#----------------------------Auth-------------------------------------------------------#
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']﻿
         #'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('file.json', scope)
client = gspread.authorize(creds)

retrieved = sheets.get_all_records()
#pprint.PrettyPrinter().pprint(retrieved)





#-----------------------------Google Sheets Display--------------------------------------#






sheets.update_cell(1,1, "Last Name" )
sheets.update_cell(1,2, "First Name")
sheets.update_cell(1,3, "Contains Website Content")
#sheets.update_cell(1,4, "Contains Picture")
sheets.update_cell(1,5, "Website Contains Required links")

