import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup


month = ""
str(month)
day = ""
str(day)


month = "march"
day = "23"


url = "https://www.timeanddate.com/on-this-day" + "/" + month + "/" + day

request = requests.get(url)		#<---------- Move this into a seperate function
html_content = request.text

soup = BeautifulSoup(html_content, "html.parser")

#Find the tag and its attribute
x = soup.find("h3", class_ ='otd-ttl')
y = x.find_next("h3", class_ ='otd-ttl')
g = y.find_next("h3", class_='otd-ttl')
h = g.find_next("h3", class_ = 'otd-ttl')
e = h.find_next("h3", class_ = 'otd-ttl')
print(x)
print(y)
print(g)
print(h)
print(e)


