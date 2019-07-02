# Nate Glod
# swimmerPrintHtml.py
# Made to turn MCSL results sheets into .csv files

import pandas as pd
import numpy as np


def parseSheet(url):

    # Gets the week and year out before adding them to the url for simplicity's sake
    yearWeek = url[0:4] + ", " + url[9]

    # Reads in the actual results
    # Format after should be:
    # lastName, firstName, age, team, time, sex, length, stroke, year, week
    # In the cases of relays, lastName and firstName will be N/A
    # In the case of relays, age will be NaN
    # 175m relay stroke will be "Graduated"
    # 200m relay stroke will be "Medley"
    df = pd.read_html("http://www.mcsl.org/Results/" + url)
    for i in range(0, 25):
        for j in range(0, 2):
            printSwimmers(df[1 + 2*i + j], df[0].iloc[i].iloc[j], yearWeek)

def printSwimmers(swimmers, race, yearWeek):
    print(swimmers)
    print(race)
    print("")


parseSheet("2019/week1/DTvMO.html")
