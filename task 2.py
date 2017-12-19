import pandas as pd


allstarfull = pd.read_csv('C:/Users/sukey/PycharmProjects/final_project/AllstarFull.csv')

batting = pd.read_csv('C:/Users/sukey/PycharmProjects/final_project/Batting.csv')

batting.fillna(0, inplace=True)

# calculate the OBP in baseball data
obp_baseball = (batting.H + batting['2B'] + batting['3B'] + batting.BB)/ (batting.AB + batting.BB + batting.SF + batting.SH)

list_obp_baseball = []

for eachdata in obp_baseball:
    if eachdata != '':
        list_obp_baseball.append(eachdata)


# calculate top 20% of the softball OBP
softball = pd.read_csv('C:/Users/sukey/PycharmProjects/final_project/softball_batting_records.csv',header=0)

softballOBP = ((softball.H + softball.BB + softball.HBP)/(softball.AB + softball.BB + softball.HBP + softball.SF + softball.SH))

list=[]
for eachOBP in softballOBP:
    list.append(eachOBP)

# Extract top 20% value
list.sort(key = int)
toptwentyper = list[-round(len(list)*0.2):-1]

totalnumber = 0

for eachelement in toptwentyper:
    totalnumber += eachelement

topaverage = totalnumber/len(toptwentyper)


# extract the baseball data by comparing the average top 20% OBP of softball data with each OBP baseball data.

goodbasebat = []

for eachbat in list_obp_baseball:
    if eachbat > topaverage:
        goodbasebat.append(eachbat)

print("There are "+str(len(goodbasebat))+" baseball players who are better than top 20% of the fast-pitch softball players.")


