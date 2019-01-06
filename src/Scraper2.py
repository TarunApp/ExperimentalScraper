import tkinter as tk
from tkinter import *
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import string, random, time
import re
#------------SCRAPING------------------#
#url = ""

#request = requests.get(url)		#<---------- Move this into a seperate function
#html_content = request.text

#soup = BeautifulSoup(html_content, "html.parser")

#Find the tag and its attribute
#print(soup.findAll("div", class_ = "paragraph"))


#Use this model to find a particular element, this example is not restricted to links
#links = (soup.find_all("a"))
#for link in links:
    #print(link.get("href"))
#------------------------Functions---------------------------#
def scrape():
    url = x.get()	#Implement wheter url contains a link or not
    if url:                #<--------- Use Get function to get text from text boxes
    	request = requests.get(url)		#Moved into seperate Function
    	html_content = request.text

    	soup = BeautifulSoup(html_content, "html.parser")

    	#Find the tag and its attribute
    	y = soup.findAll("div", class_ = "paragraph")
   	#Name 
    	textarea1.insert(END, "Loading...")
    	time.sleep(1.2)  
    	textarea1.insert(END, y)
        #Add Textarea for URLGrabber
        #b = url.split(".")
        #e = (b[0])
        #str(e)
        #h = e.split("/")
        #r = h[2]
        #return r
    else:
    	textarea1.insert(END, "Please enter a valid URL")

def scrapelinks():
    url = x.get()
    
    if url:                #<--------- Function to get links
    	request = requests.get(url)
    	html_content = request.text

    	soup = BeautifulSoup(html_content, "html.parser")              #Assign functions to buttons
	
    	links = (soup.find_all("a"))
    	for link in links:
        	y = link.get("href")
    	textarea2.insert(END, y)
        #Add TextArea For URLgrabber
        
        #b = url.split(".")
        #e = (b[0])
        #str(e)
        #h = e.split("/")
        #r = h[2]
    else:
    	textarea2.insert(END, "Please enter a valid URl")

def scrapetext():	
    url = x.get()  
    if url:             #<--------- Function to get text
    	request = requests.get(url)
    	html_content = request.text
                                                                        #Assign functions to buttons
    	soup = BeautifulSoup(html_content, "html.parser")

    #Find the tag and its attribute
    	y = soup.findAll("a", text="Exampel") #Find certain text, but with certain tags
    	textarea3.insert(END, y)
    else:
    	textarea3.insert(END, "Please enter a valid URL") #Replace with seperate window

def namecollect(websiteurl):
    b = websiteurl.split(".") #Returns name, although combined
    #print(b[0])
    e = (b[0])
    str(e)
    #print(e)
    h = e.split("/")
    r = h[2]
    return r


def findtext():
    para = soup.body.findAll(text=re.compile('The purpose'))
    para2 = soup.body.findAll(text=re.compile('Click on the tabs'))
    paracombine = para + para2
    list(para)
    print(para)
    if "The purpose" in para or paracombine:
        print("True1")
        return True
        if "Click on" in para or para2:
            print("True2")
            return True
        else:
            print("False")
    else:
        print("False else")



#---------------------------GUI----------------------------#
root = tk.Tk()

root.title("QuickScrape")


Label(root, text="Enter Website URL:").grid(padx=10, pady=1)
x = Entry(root, width=25) #<----- Split the formatting and the initialized variable, otherwise the code doesnt work
x.grid(padx=20, pady=1)          #<-- Can use Pack, but .grid allows for more flexibility, same functions

urlname = Entry(root, width=25) #<----- Split the formatting and the initialized variable, otherwise the code doesnt work
urlname.grid(padx=20, pady=1)


Button(root, text="Find Paragraph", command=scrape,).grid(padx=1, pady=0)  #<---- The third paramater, command, doesnt need any parentheses

Button(root, text="Find Links", command=scrapelinks).grid(padx=1, pady=0)
Button(root, text="Scrape Text", command=scrapetext).grid(padx=1, pady=0)

#Button(root, text="Find WebsiteLinks", command=scrapelinks).grid()



#Label(root, text="Scraped Data").grid()



#---------------------------Textoutput----------------------#


Label(root, text="User:").grid(padx=10, pady=1)


Label(root, text=("Scraped Text")).grid(row=1, column=7)
textarea1 = Text(root, width=40, height=25)
textarea1.grid(row=2, column=7, sticky=E)


Label(root, text="Links").grid(row=1, column=8)
textarea2 = Text(root, width=40, height=25)
textarea2.grid(row=2, column=8, sticky=E)

Label(root, text="Additional").grid(row=1, column=9)
textarea3 = Text(root, width=40, height=25)
textarea3.grid(row=2, column=9, sticky=E)


Label(root, text="Additional").grid(row=1, column=10)
textarea4 = Text(root, width=40, height=25)
textarea4.grid(row=2, column=10, sticky=E)

Label(root, text="Website Content").grid(row=1, column=10)
textarea4 = Text(root, width=40, height=25)
textarea4.grid(row=2, column=10, sticky=E)


root.mainloop()

