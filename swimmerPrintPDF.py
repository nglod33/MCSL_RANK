# Author: Nate Glod
# FileName: swimmerPrintPDF.py

import pandas as pd
import numpy as np

import tabula as tb


def main():
    # parseSheet("http://mcsl.org/results/2018/asi18.pdf")
    # parseCSV("allStar.csv", "2018")
    # replaceStuff("allStar18Cleaned.csv")
    df = pd.read_csv("allSwims1.csv")

    # This does really well for replacing names, remember to use masks in the future


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
    firstName = ""
    lastName = ""
    teamName = ""
    week = "7"
    j = 0
    print("lastName,firstname,age,team,time,sex,distance,event,year,week")
    for i in df:
        firstName = ""
        lastName = ""
        teamName = ""
        week = "7"
        j = 0
        # Checks to see if the event changes
        if i[0] == "Event":
            sex = i[2]
            distance = i[4]
            stroke = i[7]
            continue
        firstName = i[1]
        j = 2
        while not (48 <= ord(i[j][0]) <= 57):
            lastName = lastName + " " + i[j]
            j = j+1
        age = i[j]
        teamName = i[j+1]
        j = j+2
        while not (48 <= ord(i[j][0]) <= 57):
            teamName = teamName + " " + i[j]
            j = j+1
        time = i[j+1]
        print(lastName + "," + firstName + "," + age + "," + teamName.upper() + "," + time + "," + sex + "," + distance + ","
              + stroke + "," + year + "," + week)


def replaceStuff(fileName):
    teamNames = {
        "ASHTON": "A",
        "BANNOCKBURN": "B",
        "BETHESDA": "BE",
        "CEDARBROOK": "C",
        "CALVERTON": "CA",
        "CONNECTICUT BELAIR": "CB",
        "CHEVY CHASE REC.": "CCR",
        "COUNTRY GLEN": "CG",
        "CLARKSBURG VILLAGE": "CLK",
        "CLOPPER MILL KINGSVIEW": "CLM",
        "CARDEROCK SPRINGS": "CS",
        "CLARKSBURG TOWN CENTER": "CTC",
        "DALEVIEW": "D",
        "DAMASCUS": "DA",
        "DIAMOND FARM": "DF",
        "DARNESTOWN": "DT",
        "ELDWICK": "EW",
        "FLOWER HILL": "FH",
        "FALLSMEAD": "FM",
        "FOREST KNOLLS": "FO",
        "FRANKLIN KNOLLS": "FR",
        "FLOWER VALLEY": "FV",
        "GLENWOOD": "G",
        "GERMANTOWN": "GER",
        "GLENMONT": "GM",
        "GARRETT PARK": "GP",
        "HILLANDALE": "H",
        "HALLOWELL": "HA",
        "INVERNESS RECREATION": "IF",
        "JAMES CREEK": "JC",
        "KENMONT": "K",
        "KING FARM": "KFM",
        "KENTLANDS": "KL",
        "KEMP MILL": "KM",
        "LONG BRANCH": "LB",
        "LITTLE FALLS": "LF",
        "LAKELANDS": "LLD",
        "LAKE MARION": "LM",
        "MIDDLEBRIDGE": "MB",
        "MANCHESTER FARM": "MCF",
        "MILL CREEK TOWNE": "MCT",
        "MERRIMACK PARK": "MM",
        "MOHICAN": "MO",
        "MONTGOMERY SQUARE": "MS",
        "MANOR WOODS": "MW",
        "NORTH CHEVY CHASE": "NCC",
        "NORBECK GROVE": "NGV",
        "NORBECK HILLS": "NH",
        "NEW MARK COMMONS": "NMC",
        "NORTH CREEK": "NO",
        "NORTHWEST BRANCH": "NWB",
        "OLD FARM": "OF",
        "OLD GEORGETOWN": "OG",
        "OLNEY MILL": "OM",
        "PALISADES": "PM",
        "POTOMAC GLEN": "PGL",
        "POOLESVILLE": "PL",
        "PLANTATIONS": "PLT",
        "POTOMAC": "PO",
        "POTOMAC WOODS": "PW",
        "QUINCE ORCHARD": "QO",
        "QUAIL VALLEY": "QV",
        "ROCK CREEK": "RC",
        "REGENCY ESTATES": "RE",
        "RIVER FALLS": "RF",
        "ROBIN HOOD": "RH",
        "ROCKSHIRE": "RS",
        "ROCKVILLE": "RV",
        "STONEBRIDGE": "SB",
        "STONEGATE": "SG",
        "SEVEN LOCKS": "SL",
        "SOMERSET": "SO",
        "TANTERRA": "TA",
        "TWINBROOK": "TB",
        "TWIN FARMS": "TF",
        "TALLYHO": "TH",
        "TANGLEWOOD": "TN",
        "TILDEN WOODS": "TW",
        "UPPER COUNTY": "UC",
        "WHETSTONE": "W",
        "WOODCLIFFE": "WCF",
        "WOODLEY GARDENS": "WG",
        "WEST HILLANDALE": "WHI",
        "WESTLEIGH": "WL",
        "WILLOWS OF POTOMAC": "WLP",
        "WILDWOOD MANOR": "WM",
        "WATERS LANDING": "WTL",
        "WASHINGTONIAN WOODS": "WWD"
    }
    # for replacing ages that get messed up in conversion
    ages = {
        "3.0": "3",
        "4.0": "4",
        "5.0": "5",
        "6.0": "6",
        "7.0": "7",
        "8.0": "8",
        "9.0": "9",
        "10.0": "10",
        "11.0": "11",
        "12.0": "12",
        "13.0": "13",
        "14.0": "14",
        "15.0": "15",
        "16.0": "16",
        "17.0": "17",
        "18.0": "18"
    }
    events = {
        "Individual": "IM",
        "Medley": "Medley Relay",
        "Freestyle": "Free",
        "Backstroke": "Back",
        "Butterfly": "Fly"
    }
    df = pd.read_csv(fileName).astype(str)
    df['team'].replace(to_replace=teamNames, inplace=True)
    df['age'].replace(to_replace=ages, inplace=True)
    df['event'].replace(to_replace=events, inplace=True)
    # Create mask for replacement
    mask = (df['distance'] == '175')
    df['event'] = df['event'].mask(mask, 'Graduated Relay')
    df.to_csv("asi18.csv")

# We do need a printSwimmers, we can't use the standard one
# They need to be able to find the event names as well because they don't have the


if __name__ == "__main__":
    # execute only if run as a script
    main()

