# Author: Nate Glod
# FileName: swimmerPrintPDF.py

import pandas as pd
import numpy as np
import re

import tabula as tb


def main():
    # parseSheet("http://mcsl.org/results/2018/asi18.pdf")
    parseCSV("allStar.csv", 2019)


def parseSheet(fileName):
    df = tb.read_pdf(fileName, pages="all", guess="False", output_format="dataframe")
    df = df.values
    printString = ""
    for i in df:
        printString = ""
        for j in range(0, 6):
            if i[j] != i[j]:
                continue
            printString = printString + str(i[j])
            if j < 5:
                printString = printString + ", "
        printString = printString.replace("  ", ", ")
        printString = printString.replace(" ", ",")
        printString = printString.replace(",,", ", ")
        print(printString)


def parseCSV(fileName, year):
    df = pd.read_csv(fileName)
    df = df.values
    stroke = ""
    distance = ""
    sex = ""
    name = ""
    team = ""
    week = 7
    for i in df:
        # Checks to see if the event changes
        if i[0] == "Event":
            sex = i[2]
            distance = i[4]
            stroke = i[7]
        try:
            age = int(i[3])
            name = i[1] + ", " + i[2] + ", "

        except:
            age = int(i[4])
            name = i[1] + " " + i[2] + ", " + i[3] + ", "
    print(df[1])


def getTeamAbrv(teamName):
    teamNames = {
        "Ashton": "A",
        "Bannockburn": "B",
        "Bethesda": "BE",
        "Cedarbrook": "C",
        "Calverton": "CA",
        "Connecticut Belair": "CB",
        "Chevy Chase Rec.": "CCR",
        "Country Glen": "CG",
        "Clarksburg Village": "CLK",
        "Clopper Mill Kingsview": "CLM",
        "Carderock Springs": "CS",
        "Clarksburg Town Center": "CTC",
        "Daleview": "D",
        "Damascus": "DA",
        "Diamond Farm": "DF",
        "Darnestown": "DT",
        "Eldwick": "EW",
        "Flower Hill": "FH",
        "Fallsmead": "FM",
        "Forest Knolls": "FO",
        "Franklin Knolls": "FR",
        "Flower Valley": "FV",
        "Glenwood": "G",
        "Germantown": "GER",
        "Glenmont": "GM",
        "Garrett Park": "GP",
        "Hillandale": "H",
        "Hallowell": "HA",
        "Inverness Recreation": "IF",
        "James Creek": "JC",
        "Kenmont": "K",
        "King Farm": "KFM",
        "Kentlands": "KL",
        "Kemp Mill": "KM",
        "Long Branch": "LB",
        "Little Falls": "LF",
        "Lakelands": "LLD",
        "Lake Marion": "LM",
        "Middlebridge": "MB",
        "Manchester Farm": "MCF",
        "Mill Creek Towne": "MCT",
        "Merrimack Park": "MM",
        "Mohican": "MO",
        "Montgomery Square": "MS",
        "Manor Woods": "MW",
        "North Chevy Chase": "NCC",
        "Norbeck Grove": "NGV",
        "Norbeck Hills": "NH",
        "New Mark Commons": "NMC",
        "North Creek": "NO",
        "Northwest Branch": "NWB",
        "Old Farm": "OF",
        "Old Georgetown": "OG",
        "Olney Mill": "OM",
        "Palisades": "PM",
        "Potomac Glen": "PGL",
        "Poolesville": "PL",
        "Plantations": "PLT",
        "Potomac": "PO",
        "Potomac Woods": "PW",
        "Quince Orchard": "QO",
        "Quail Valley": "QV",
        "Rock Creek": "RC",
        "Regency Estates": "RE",
        "River Falls": "RF",
        "Robin Hood": "RH",
        "Rockshire": "RS",
        "Rockville": "RV",
        "Stonebridge": "SB",
        "Stonegate": "SG",
        "Seven Locks": "SL",
        "Somerset": "SO",
        "Tanterra": "TA",
        "Twinbrook": "TB",
        "Twin Farms": "TF",
        "Tallyho": "TH",
        "Tanglewood": "TN",
        "Tilden Woods": "TW",
        "Upper County": "UC",
        "Whetstone": "W",
        "Woodcliffe": "WCF",
        "Woodley Gardens": "WG",
        "West Hillandale": "WHI",
        "Westleigh": "WL",
        "Willows Of Potomac": "WLP",
        "Wildwood Manor": "WM",
        "Waters Landing": "WTL",
        "Washingtonian Woods": "WWD"
    }
    if teamName in teamNames:
        return teamNames[teamName]
    else:
        return teamName


# We do need a printSwimmers, we can't use the standard one
# They need to be able to find the event names as well because they don't have the


if __name__ == "__main__":
    # execute only if run as a script
    main()

