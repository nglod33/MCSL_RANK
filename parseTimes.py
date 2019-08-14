# Author: Nate Glod
# FileName: parseTimes.py
# Purpose: Parse through the allSwims.csv file and convert all times to floats of seconds

import pandas as pd
import locale


def convertTimes(fileName):
    # There's definitely a smoother way around this but I'm only going to run this a few times
    df = pd.read_csv(fileName).astype(str)
    print(df['time'])
    mask = (df['time'].str.contains(":"))
    df['minutes'] = df['time'].mask(mask, df['time'].str[0])
    df['seconds'] = df['time'].mask(mask, df['time'].str[2:])
    timeMask = (df['minutes'] != df['seconds'])
    df['realTime'] = df['minutes'].mask(timeMask, 60 * df['minutes'].astype(float) + df['seconds'].astype(float))
    df['time'] = df['realTime']
    df = df.drop(columns=['minutes', 'seconds', 'realTime'])
    df.to_csv("allSwimsFloat.csv")
    # One kid swam 52 minutes in the 25 breast and is causing this to crash


def main():
    convertTimes("allSwims.csv")


if __name__ == "__main__":
    # execute only if run as a script
    main()
