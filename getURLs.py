# Filename: getURLs
# Author: Nate Glod
# Purpose: Create a function that takes in a year, and then spits out all the urls for every meet of that year
# Shit gets weird before 2013 so let's just start there

import urllib3
from bs4 import BeautifulSoup as bs
import swimmerPrintHtml as sph


def main():
    for i in range(2014, 2019):
        getURLs(i)


def getURLs(year):
    suffixes = ["mcsl1res", "mcsl2res", "mcsl3res", "mcsl4res", "mcsl5res", "mcsldiv"]
    for i in suffixes:
        http = urllib3.PoolManager()
        response = http.request('GET', "http://www.mcsl.org/results/" + str(year) + "/" + i + ".html")
        soup = bs(response.data, 'html.parser')
        previousLink = ""
        for link in soup.find_all('a', href=True):
            # double slashes in divisionals is not a problem at all
            if link['href'] != previousLink:
                # print(str(year) + "/" + link['href'])
                sph.parseSheet(str(year) + "/" + link['href'])
            previousLink = link['href']
'''
TODO:
Get results in from 2014 on 
Make graphs and wealth/home-value/education correlations/analysis
Get PostgreSQL database going on so you can do more fancy queries and get a website up and running
Get website up and running and allow users to run queries and see ranks/percentiles for swimmers
'''

main()

