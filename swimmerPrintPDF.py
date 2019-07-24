# Author: Nate Glod
# FileName: swimmerPrintPDF.py

import pandas as pd
import numpy as np
import re

import tabula as tb


def main():
    parseSheet("http://mcsl.org/results/2018/asi18.pdf")


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
        # Find the regular expressions to comma separate the rank and the name
        re.sub()
        print(printString)

# We do need a printSwimmers, we can't use the standard one
# They need to be able to find the event names as well because they don't have the


if __name__ == "__main__":
    # execute only if run as a script
    main()

