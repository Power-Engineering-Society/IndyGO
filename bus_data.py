################################################################################
# Author: Zeeshan Babar
# Date: 10/24/2020
# Data analysis on the electric buses provided by Indigo
################################################################################
import pandas as pd      #will be using pandas for data analysis
#import numpy as py
import glob as gb      #glob finds all the pathnames matching a specified pattern
import math
import matplotlib.pyplot as plt
# in order to store the 30 days data for each bus sperately
bus1 = []
bus2 = []
bus3 = []
bus4 = []
bus5 = []
bus6 = []
bus7 = []
bus8 = []
bus9 = []
bus10 = []
bus11 = []
bus12 = []
bus13 = []
bus14 = []
bus15 = []
bus16 = []
bus17 = []
bus18 = []
bus19 = []
bus20 = []
bus21 = []
bus22 = []
bus23 = []
bus24 = []
bus25 = []
bus26 = []
bus27 = []

li = [] #list that will contain all the data

path = r'C:\Indigo' #path of data files & r to address any special characters in the path
all_files = gb.glob(path + "/*.csv") # all files endiing with .csv will be accessed
bus_data = pd.DataFrame() # to store all th
avgDist = [] #to store the average distance travelled in 30 days by each bus
avgEused = [] #to store the average Energy used in 30 days by each bus
#busA = []
buses = [] #list sorted so that we have data of each bus in its own element
#col_to_show = 0
# for loop to extract the data form the csv files, sort the data according to buses
for filename in all_files:
    data = pd.read_csv(filename, index_col = None, header = 0) # store the data.
    li.append(data) # add data in the list in element
    bus_data = pd.concat(li)
    #each bus variable corresponds to the bus # IG)1***
    bus1.append(data[data['Bus No.'].apply(lambda state: state == "IG_1899")].head())
    bus2.append(data[data['Bus No.'].apply(lambda state: state == "IG_1999")].head())
    bus3.append(data[data['Bus No.'].apply(lambda state: state == "IG_1995")].head())
    bus4.append(data[data['Bus No.'].apply(lambda state: state == "IG_1994")].head())
    bus5.append(data[data['Bus No.'].apply(lambda state: state == "IG_1992")].head())
    bus6.append(data[data['Bus No.'].apply(lambda state: state == "IG_1991")].head())
    bus7.append(data[data['Bus No.'].apply(lambda state: state == "IG_1990")].head())
    bus8.append(data[data['Bus No.'].apply(lambda state: state == "IG_1989")].head())
    bus9.append(data[data['Bus No.'].apply(lambda state: state == "IG_1996")].head())
    bus10.append(data[data['Bus No.'].apply(lambda state: state == "IG_1997")].head())
    bus11.append(data[data['Bus No.'].apply(lambda state: state == "IG_1979")].head())
    bus12.append(data[data['Bus No.'].apply(lambda state: state == "IG_1981")].head())
    bus13.append(data[data['Bus No.'].apply(lambda state: state == "IG_1982")].head())
    bus14.append(data[data['Bus No.'].apply(lambda state: state == "IG_1984")].head())
    bus15.append(data[data['Bus No.'].apply(lambda state: state == "IG_1986")].head())
    bus16.append(data[data['Bus No.'].apply(lambda state: state == "IG_1988")].head())
    bus17.append(data[data['Bus No.'].apply(lambda state: state == "IG_1971")].head())
    bus18.append(data[data['Bus No.'].apply(lambda state: state == "IG_1974")].head())
    bus19.append(data[data['Bus No.'].apply(lambda state: state == "IG_1975")].head())
    bus20.append(data[data['Bus No.'].apply(lambda state: state == "IG_1976")].head())
    bus21.append(data[data['Bus No.'].apply(lambda state: state == "IG_1980")].head())
    bus22.append(data[data['Bus No.'].apply(lambda state: state == "IG_1983")].head())
    bus23.append(data[data['Bus No.'].apply(lambda state: state == "IG_1985")].head())
    bus24.append(data[data['Bus No.'].apply(lambda state: state == "IG_1970")].head())
    bus25.append(data[data['Bus No.'].apply(lambda state: state == "IG_1972")].head())
    bus26.append(data[data['Bus No.'].apply(lambda state: state == "IG_1973")].head())
    bus27.append(data[data['Bus No.'].apply(lambda state: state == "IG_1977")].head())
frame = pd.concat(li, axis = 0, ignore_index = True) #all data in one frame
# remove the headers in between.
bus1 = pd.concat(bus1, axis = 0, ignore_index = True)
bus2 = pd.concat(bus2, axis = 0, ignore_index = True)
bus3 = pd.concat(bus3, axis = 0, ignore_index = True)
bus4 = pd.concat(bus4, axis = 0, ignore_index = True)
bus5 = pd.concat(bus5, axis = 0, ignore_index = True)
bus6 = pd.concat(bus6, axis = 0, ignore_index = True)
bus7 = pd.concat(bus7, axis = 0, ignore_index = True)
bus8 = pd.concat(bus8, axis = 0, ignore_index = True)
bus9 = pd.concat(bus9, axis = 0, ignore_index = True)
bus10 = pd.concat(bus10, axis = 0, ignore_index = True)
bus11 = pd.concat(bus11, axis = 0, ignore_index = True)
bus12 = pd.concat(bus12, axis = 0, ignore_index = True)
bus13 = pd.concat(bus13, axis = 0, ignore_index = True)
bus14 = pd.concat(bus14, axis = 0, ignore_index = True)
bus15 = pd.concat(bus15, axis = 0, ignore_index = True)
bus16 = pd.concat(bus16, axis = 0, ignore_index = True)
bus17 = pd.concat(bus17, axis = 0, ignore_index = True)
bus18 = pd.concat(bus18, axis = 0, ignore_index = True)
bus19 = pd.concat(bus19, axis = 0, ignore_index = True)
bus20 = pd.concat(bus20, axis = 0, ignore_index = True)
bus21 = pd.concat(bus21, axis = 0, ignore_index = True)
bus22 = pd.concat(bus22, axis = 0, ignore_index = True)
bus23 = pd.concat(bus23, axis = 0, ignore_index = True)
bus24 = pd.concat(bus24, axis = 0, ignore_index = True)
bus25 = pd.concat(bus25, axis = 0, ignore_index = True)
bus26 = pd.concat(bus26, axis = 0, ignore_index = True)
bus27 = pd.concat(bus27, axis = 0, ignore_index = True)
#store data of 30 days of each bus into each element of buses
buses.append(bus1)
buses.append(bus2)
buses.append(bus3)
buses.append(bus4)
buses.append(bus5)
buses.append(bus6)
buses.append(bus7)
buses.append(bus8)
buses.append(bus9)
buses.append(bus10)
buses.append(bus11)
buses.append(bus12)
buses.append(bus13)
buses.append(bus14)
buses.append(bus15)
buses.append(bus16)
buses.append(bus17)
buses.append(bus18)
buses.append(bus19)
buses.append(bus20)
buses.append(bus21)
buses.append(bus22)
buses.append(bus23)
buses.append(bus24)
buses.append(bus25)
buses.append(bus26)
buses.append(bus27)


test2 = []
avrgeEnrgy =[]
avgEnergy = []
for b in range(27):
    test2 = buses[b]
    avrge = test2['Actual Distance'].mean()
    avgDist.append(avrge)

for b in range(27):
    test2 = buses[b]
    avrgeEnrgy = test2['Energy Used'].mean()
    avgEnergy.append(avrgeEnrgy)

#test = frame
#bus = pd.concat(busA, axis = 0, ignore_index = True) #all data in one frame w/o headers
#col_to_show = ['Energy Used', 'Start Odometer', 'End Odometer']
##bus['Total Miles'] = bus['End Odometer'] - bus['Start Odometer']
#test['Total Miles'] = test['End Odometer'] - test['Start Odometer']
#Energy = (bus.iloc[0:29,'Energy Used'])
#bus.drop(['kWh/Miles', 'Miles/kWh', 'Start Odometer', 'End Odometer'], axis = 1, inplace = True)
#bus.drop(['kWh/Miles', 'Miles/kWh', 'Start Odometer', 'End Odometer', 'SOC charged', 'SOC used', 'Total Miles', 'SOC/Miles', 'Energy Charge', 'Miles/SOC'], axis = 1, inplace = True)
#print(data.head(1)) #looking at first 2 lines
#print(data.shape) #for num of rows & cols
#print(data.info())
#print(data.describe(include = ['object', 'float64']))
#print(bus.loc[0:29,'Energy Used': 'Total Miles'])
#plotting
fig, ax = plt.subplots()
#ax.scatter(bus['Total Miles'],bus['Energy Used'])

ax.scatter(buses[0]['Actual Distance'],buses[0]['Energy Used'])
ax.scatter(buses[1]['Actual Distance'],buses[1]['Energy Used'])
ax.scatter(buses[2]['Actual Distance'],buses[2]['Energy Used'])
ax.scatter(buses[3]['Actual Distance'],buses[3]['Energy Used'])
ax.scatter(buses[4]['Actual Distance'],buses[4]['Energy Used'])
ax.scatter(buses[5]['Actual Distance'],buses[5]['Energy Used'])
ax.scatter(buses[6]['Actual Distance'],buses[6]['Energy Used'])
ax.scatter(buses[7]['Actual Distance'],buses[7]['Energy Used'])
ax.scatter(buses[8]['Actual Distance'],buses[8]['Energy Used'])
ax.scatter(buses[9]['Actual Distance'],buses[9]['Energy Used'])
ax.scatter(buses[10]['Actual Distance'],buses[10]['Energy Used'])
ax.scatter(buses[11]['Actual Distance'],buses[11]['Energy Used'])
ax.scatter(buses[12]['Actual Distance'],buses[12]['Energy Used'])
ax.scatter(buses[13]['Actual Distance'],buses[13]['Energy Used'])
ax.scatter(buses[14]['Actual Distance'],buses[14]['Energy Used'])
ax.scatter(buses[15]['Actual Distance'],buses[15]['Energy Used'])
ax.scatter(buses[16]['Actual Distance'],buses[16]['Energy Used'])
ax.scatter(buses[17]['Actual Distance'],buses[17]['Energy Used'])
ax.scatter(buses[18]['Actual Distance'],buses[18]['Energy Used'])
ax.scatter(buses[19]['Actual Distance'],buses[19]['Energy Used'])
ax.scatter(buses[20]['Actual Distance'],buses[20]['Energy Used'])
ax.scatter(buses[21]['Actual Distance'],buses[21]['Energy Used'])
ax.scatter(buses[22]['Actual Distance'],buses[22]['Energy Used'])
ax.scatter(buses[23]['Actual Distance'],buses[23]['Energy Used'])
ax.scatter(buses[24]['Actual Distance'],buses[24]['Energy Used'])
ax.scatter(buses[25]['Actual Distance'],buses[25]['Energy Used'])
ax.scatter(buses[26]['Actual Distance'],buses[26]['Energy Used'])
# Add title and axis names
plt.title('Energy Used Vs. Actual Distance')
plt.xlabel('Distance Travelled (miles)')
plt.ylabel('Energy Used (kWh)')
plt.show() #show plot
#print(buses)

#Distavg = (bus['Actual Distance'].mean())
#enrgyAvg = (bus['Energy Used'].mean())
#print(f'distanceAvg = {Distavg:.2f} & EnrgyAvg = {enrgyAvg}')
