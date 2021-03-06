import tkinter as tk
from tkinter import *
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup


#Functions Should be Easier to Handle with seperate file systems
#Variables should be changed

def scrape():
    url = x.get()                #<--------- Use Get function to get text from text boxes
    request = requests.get(url)		#Moved into seperate Function
    html_content = request.text

    soup = BeautifulSoup(html_content, "html.parser")

    #Find the tag and its attribute
    y = soup.findAll("div", class_ = "paragraph")
    return y

def scrapelinks():
    url = x.get()                #<--------- Function to get links
    request = requests.get(url)
    html_content = request.text

    soup = BeautifulSoup(html_content, "html.parser")              #Assign functions to buttons

    links = (soup.find_all("a"))
    for link in links:
        y = link.get("href")
    return y

def scrapetext():
    url = x.get()                #<--------- Function to get text
    request = requests.get(url)
    html_content = request.text
                                                                        #Assign functions to buttons
    soup = BeautifulSoup(html_content, "html.parser")

    #Find the tag and its attribute
    y = soup.findAll("a", text="Exampel") #Find certain text, but with certain tags
    return y
