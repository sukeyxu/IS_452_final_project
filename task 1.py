import pandas as pd

continuity = "T"
findingresult = []

fileroutlist = ['C:/Users/sukey/PycharmProjects/final_project/AllstarFull.csv','C:/Users/sukey/PycharmProjects/final_project/Batting.csv','C:/Users/sukey/PycharmProjects/final_project/Fielding.csv','C:/Users/sukey/PycharmProjects/final_project/Pitching.csv','C:/Users/sukey/PycharmProjects/final_project/Salaries.csv','C:/Users/sukey/PycharmProjects/final_project/Schools.csv','C:/Users/sukey/PycharmProjects/final_project/softball_batting_records.csv']

while continuity == "T":
    givingfilerout = "Please tell me the rout of the file you want to check:"
    filerout = input(givingfilerout)
    while filerout not in fileroutlist:
        filerout = input("Rout doesn't exist, Please input again:")
    file = pd.read_csv(filerout)
    attricontinuity = input("Do you want to extra any attribute from this file? Enter T to continue, otherwise enter any other letter.")
    while attricontinuity == "T":
        attribute_name = input("Please tell me what is the attribute:")
        attribute = file[attribute_name]
        findingresult.append(attribute)
        attricontinuity = input ("Do you want to extra another attribute form this file? Enter T to continue, otherwise enter any other letter.")
    continuity = input("Do you want find another file? Enter T to continue, otherwise enter any other letter.")

outfile = open("Yourfinding",'w',encoding='utf-8')
print(findingresult,file = outfile)




