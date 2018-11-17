import tkinter as tk
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

url = ""

request = requests.get(url)
html_content = request.text

soup = BeautifulSoup(html_content, "html.parser")

#Find the tag and its attribute
#print(soup.findAll("div", class_ = "paragraph"))


#Use this model to find a particular element, this example is not restricted to links
#links = (soup.find_all("a"))
#for link in links:
    #print(link.get("href"))

root = tk.Tk()

btn = tk.Button(root, text="Find")
btn.pack()


def btnpress():
    print(soup.findAll("div", class_ = "paragraph"))

btn['command']= btnpress
#Move button
btn.pack(side="bottom")


root.mainloop()

