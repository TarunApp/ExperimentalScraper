import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import time, random





							#Function to distribute data points throughout graph

url = ""
request = requests.get(url)  # <---------- Move this into a seperate function
html_content = request.text
soup = BeautifulSoup(html_content, "html.parser")

def checktext():
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
            return False
    else:
        print("False else")
        return False


#PIE CHART
#Add points to x, y 
#x = []
#y = []


#fig, plot1 = plt.subplots()
#plot1 = pl
#plt.scatter(x, y, 100, 'b')
#plt.show()


#labels = 
#sizes = 

#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, labels=labels).
#plt.show()




# BAR GRAPH
#tuple
#fig, ax = plt.subplots()


#Calculate Data
#dataset = ()
#yaxis = np.arange(len(people)) #Y Axis 
#Max 
#xaxis = 1 * 100 * np.random.rand(len(people))


#yaxis
#Format Data Display
#ax.barh(yaxis  , xaxis, align='center', color='green')
#ax.set_yticks(yaxis)
#ax.set_yticklabels(dataset)
#ax.set_xlabel()
#ax.set_title()

#plt.show()
