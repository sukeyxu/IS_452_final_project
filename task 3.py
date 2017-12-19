import pandas as pd
import numpy as np
import csv


fileroutlist = ['C:/Users/sukey/PycharmProjects/final_project/AllstarFull.csv','C:/Users/sukey/PycharmProjects/final_project/Batting.csv','C:/Users/sukey/PycharmProjects/final_project/Fielding.csv','C:/Users/sukey/PycharmProjects/final_project/Pitching.csv','C:/Users/sukey/PycharmProjects/final_project/Salaries.csv']

continuity = "T"
playerID = input("Please tell me what is the PlayerID of which information you want to revise:")
while continuity == "T":
    filerout = input("Please tell me the rout of the first file that you want to revise")
    while filerout not in fileroutlist:
        filerout = input("Rout doesn't exist, Please input again:")
    filetorevise = pd.read_csv(filerout)
    attricontinuity = input("Do you want to revise any attribute from this file? Enter T to continue, otherwise enter any other letter.")
    while attricontinuity == "T":
        attributename = input("Please tell me the attribute name you want to revise in this file:")
        content = input("Please tell me the new content:")
        filetorevise.set_index('playerID',inplace=True)
        filetorevise.set_value(playerID,attributename,content)
        attricontinuity = input ("Do you want to revise another attribute form this file? Enter T to continue, otherwise enter any other letter.")
    continuity = input("Do you want find another file? Enter T to continue, otherwise enter any other letter.")

filetorevise.to_csv('C:/Users/sukey/PycharmProjects/final_project/yournewreviesdfile.csv')
