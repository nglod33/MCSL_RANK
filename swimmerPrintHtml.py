# Author: Nate Glod
# FileName: swimmerPrintHtml.py
# Made to turn MCSL results sheets into .csv files

import pandas as pd
import numpy as np
import html5lib as h5
import bs4


# Parses an entire meet sheet
def parseSheet(url):

    if url.split(".")[1] == "pdf":
        return
    # Gets the week and year out before adding them to the url for simplicity's sake
    yearWeek = url.split("/")[0] + ", " + url.split("/")[-2][4]
    # Reads in the actual results
    # Format after should be:
    # lastName, firstName, age, team, time, sex, length, stroke, year, week
    # In the cases of relays, lastName and firstName will be N/A
    # In the case of relays, age will be NaN
    # IM Stroke will be Individual
    # 175m relay stroke will be "Freestyle", you must specify 175M to get the relays
    # 200m relay stroke will be "Medley"
    # Relay team names will be the full team names and not the abbreviations

    df = pd.read_html("http://www.mcsl.org/Results/" + url)
    for i in range(0, 25):
        for j in range(0, 2):
            printSwimmers(df[1 + 2*i + j], df[0].iloc[i].iloc[j], yearWeek)


# race should just be a long string containing information about the race
def printSwimmers(swimmers, race, yearWeek):
    swimmers = swimmers.values

    race = race.split()
    raceInfo = race[3] + ", " + race[5][:-1] + ", " + race[6].split("A")[0] + ", "

    # Case for relays
    if swimmers.size == 0:
        return
    split = swimmers[0][1].split(" (")
    if split[0] == swimmers[0][1] or split[1] == "NON-Conforming Pool)":
        for i in swimmers:
            # Checks for NaN values to filter out certain relay
            if i[0] != i[0]:
                continue
            else:
                print("NULL, NULL, NULL, " + i[1] + ", " + str(i[3]) + ", " + raceInfo + yearWeek)

    # Case for normal events
    else:
        # Gets individual swimmer information. Relays need a different format
        for i in swimmers:
            personal = i[1].split(" (")
            print(personal[0] + ", " + personal[1][:-1] + ", " + personal[2][:-1] + ", " + str(i[3]) + ", " + raceInfo + yearWeek)



