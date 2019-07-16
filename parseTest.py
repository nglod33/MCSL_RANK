# Author: Nate Glod
# FileName: parseTest.py

# What do I need this to do?
# Fetch the back half of the results urls, the part with the format:
# /[year]/week[number]/[team1]v[team2].html
# After that we can pipe those names into a document and yeet all those results into a CSV

import pandas as pd
import numpy as np
import html5lib as h5
from bs4 import BeautifulSoup as bs
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initiates the Selenium instance and gets the results webpage
driver = webdriver.Firefox()
driver.get("http://www.mcsl.org/Results2.aspx")
print(driver)

# Finds the year and then sets it to 2019
# The find_elements function returns a list of web elements, and therefore you cannot just select the return value you
# need to select an index of the return value
# Selects an element of the webpage (in this case the box for choosing the year) and then goes and chooses it
yearBox = Select(driver.find_elements_by_id("ctl00_BodyContent_ddYr")[0])
print("yearBox: " + str(yearBox))
yearBox.select_by_value("2016")

# Waits for the week 1 link to appear before clicking it
waitForLink = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.LINK_TEXT, "Week 1 Results"))
resultsLink = driver.find_element(By.LINK_TEXT, "Week 1 Results")
resultsLink.click()
waitForResults = WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_id("resultText"))

# List of link ids: mcsl1res.html, mcsl2res.html, mcsl3res.html, mcsl4res.html, mcsl5res.html, mcsldiv.html
# asi[year].html


# Waits until the resultText pops up and then selects it
try:
    soup = bs(driver.page_source, 'html.parser')
    for link in soup.find_all('a'):
        print(link)

    '''
    html = bs(results, 'html.parser').a.html
    for i in html:
        print(i)
    '''

finally:
    print("hello")
    driver.quit()
