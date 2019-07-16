# Filename: getURLs
# Author: Nate Glod
# Purpose: Create a function that takes in a year, and then spits out all the urls for every meet of that year

import pandas as pd
import urllib3
from lxml import html
from bs4 import BeautifulSoup as bs
import re


def getURLs(year):
    suffixes = ["mcsl1res", "mcsl2res", "mcsl3res", "mcsl4res", "mcsl5res", "mcsldiv"]
    print("Start")
    for i in suffixes:
        http = urllib3.PoolManager()
        response = http.request('GET', "http://www.mcsl.org/results/" + str(year) + "/" + i + ".html")
        soup = bs(response.data, 'html.parser')
        previousLink = ""
        for link in soup.find_all('a', href=True):
            # Divisionals href has a / at the start of the href WHEN LITERALLY NO OTHER LINK DOES
            # This isn't a problem but it is very annoying to deal with
            if link['href'] != previousLink:
                print(str(year) + "/" + link['href'])
            previousLink = link['href']
    print("Done")


getURLs(2018)

