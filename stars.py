import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(starturl)
soup = BeautifulSoup(page.text, 'html.parser')
startable = soup.find('table')
templist = []
rows = startable.find_all('tr')
for row in rows:
    td = row.find_all('td')
    line = [i.text.strip() for i in td]
    templist.append(line) 
starnames = []
distance = []
mass = []
radius = []
luminosity = []
for i in range(1, len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][2])
    mass.append(templist[i][3])
    radius.append(templist[i][4])
    luminosity.append(templist[i][5])
datafile = pd.DataFrame(list(zip(starnames, distance, mass, radius, luminosity)), columns = ["starnames", "distance", "mass", "radius", "luminosity"])
datafile.to_csv("brightstars.csv")