import tkinter as tk
from tkinter import *
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

#------------SCRAPING------------------#
url = "https://christianhudspeth.weebly.com/project-introduction--purpose-paper.html"

request = requests.get(url)		#<---------- Move this into a seperate function
html_content = request.text

soup = BeautifulSoup(html_content, "html.parser")

#Find the tag and its attribute
#print(soup.findAll("div", class_ = "paragraph"))


#Use this model to find a particular element, this example is not restricted to links
#links = (soup.find_all("a"))
#for link in links:
    #print(link.get("href"))


#---------------------------GUI----------------------------#
root = tk.Tk()

btn = tk.Button(root, text="Find")
btn2 = tk.Button(root, text="Asdjke")

websiteurl = ""
urlwidget = tk.Entry(root, textvariable=websiteurl)


btn.pack()
btn2.pack()


def btnpress(url):
	url = websiteurl

	request = requests.get(url)
	html_content = request.text

	soup = BeautifulSoup(html_content, "html.parser")
	print(soup.findAll("div", class_ = "paragraph"))


def helloworld():
	links = (soup.find_all("a"))
	for link in links:
    		print(link.get("href"))

btn['command']= btnpress
btn2['command']= helloworld
#Move button
btn.pack(side="bottom")
btn2.pack(side="right")
urlwidget.pack(side="top")



root.mainloop()

