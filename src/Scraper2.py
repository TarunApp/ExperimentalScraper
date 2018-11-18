import tkinter as tk
from tkinter import *
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

#------------SCRAPING------------------#
#url = "https://christianhudspeth.weebly.com/project-introduction--purpose-paper.html"

#request = requests.get(url)		#<---------- Move this into a seperate function
#html_content = request.text

#soup = BeautifulSoup(html_content, "html.parser")

#Find the tag and its attribute
#print(soup.findAll("div", class_ = "paragraph"))


#Use this model to find a particular element, this example is not restricted to links
#links = (soup.find_all("a"))
#for link in links:
    #print(link.get("href"))

def scrape():
    url = x.get()
    request = requests.get(url)		#<---------- Move this into a seperate function
    html_content = request.text

    soup = BeautifulSoup(html_content, "html.parser")

    #Find the tag and its attribute
    print(soup.findAll("div", class_ = "paragraph"))



#---------------------------GUI----------------------------#
root = tk.Tk()

Label(root, text="Hello World").grid(row=0, column=0)
x = Entry(root)
x.grid(row = 0, column = 2)
Button(root, text="Enter", command=scrape).grid(row=1)

root.mainloop()

