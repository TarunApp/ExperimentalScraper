import tkinter as tk
from tkinter import *
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

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



#---------------------------GUI----------------------------#
root = tk.Tk()

Label(root, text="Hello World").grid(row=0, column=0)
x = Entry(root) #<----- Split the formatting and the initialized variable, otherwise the code doesnt work
x.grid(row = 0, column = 2)          #<-- Can use Pack, but .grid allows for more flexibility
Button(root, text="Enter", command=scrape).grid(row=1)  #<---- The third paramater, command, doesnt need any parentheses




root.mainloop()

