################################################################################
# Author: Zeeshan Babar
# Date: 10/24/2020
# Data analysis on the electric buses provided by Indigo
################################################################################
#importing modules
import numpy as np
import pandas as pd
import csv
import glob as gb
import math
import matplotlib.pyplot as plt

# stores the busIDS
def busID(reader): #this function holds the bus list with just the bus IDs.
    global bus
    bus = [] #bus IDs will be stored in this list.
    for row in reader: #for loop to extract the first row
        bus_id = row[0]
        bus.append(bus_id)
    return(bus)
#sort the data accoring to each busID
def sort():
    a = 0
    b = 0
    c = 0
    bus_df = []
    all_data = extract_data()
    bus_data = pd.concat(all_data)  # all data in one data frame
    #for id_num in bus:
        #for j in all_data:
            #if j.index[a] == id_num:
            #    bus_df.append(j[j['Bus No.'].apply(lambda state: state == id_num)].head())
    #print(all_data[0].iloc[0])
    #bus1.append(data[data['Bus No.'].apply(lambda state: state == "IG_1899")].head())
    return()

def sortData(data, bus): # Sorting the data over 30 days according to the bus number
    global i
    bus_ID = ['IG_1899', 'IG_1970', 'IG_1971', 'IG_1971', 'IG_1972', 'IG_1973', 'IG_1974', 'IG_1975', 'IG_1976', 'IG_1977'
              'IG_1979', 'IG_1980', 'IG_1981', 'IG_1982', 'IG_1983', 'IG_1984', 'IG_1985', 'IG_1986', 'IG_1988', 'IG_1989'
              'IG_1991', 'IG_1992', 'IG_1994', 'IG_1995', 'IG_1996', 'IG_1997', 'IG_1999']
    bus.append(data[data['Bus No.'].apply(lambda state: state == bus_ID)].head())
    bus = pd.concat(bus, axis = 0, ignore_index = True)
    buses.append(bus)
    i += 1
    return(buses)
def plot_bus(bus, ax):

    #fig, ax = plt.subplots()
    ax.scatter(bus['Actual Distance'], bus['Energy Used'])
     #Add title and axis names
    plt.title('Energy Used Vs. Actual Distance')
    plt.xlabel('Distance Travelled (miles)')
    plt.ylabel('Energy Used (kWh)')
    #print(bus)
    #plt.show() #show plot
    return()

def ExtractAndsort_data():
    #Extracting data from csv files
    path = r'C:\Indigo' #path of data files & r to address any special characters in the path
    all_files = gb.glob(path + "/*.csv") # all files endiing with .csv will be accessed
    bus_data = pd.DataFrame() # 2D->cols & rows (bus_data contains all the data)
#defining lists
    li = [] #list that will contain all the data
    buses = []
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
#for loop to extract the data form the csv files, sort the data according to buses
    for filename in all_files:
        data = pd.read_csv(filename, index_col = None, header = 0) # store the data.
        li.append(data)
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
#frame = pd.concat(li, axis = 0, ignore_index = True) #all data in one frame
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

    li = pd.concat(li, axis = 0, ignore_index = True)
    return(buses)

def filterData(bus,df): #elimate outliers using 3-sigma
    i = 0
    mean = bus["kWh/Miles"].mean()
    std = bus["kWh/Miles"].std()
    filtbus = []
    for item in bus["kWh/Miles"]:
        if (item >= (mean - 3 * std) and item <= (mean + 3 * std)):
            filtbus.append(item)
        else:
            return(df.append(bus.drop([i])))
        i += 1
    return()
def main():
    #plt.rcParams.update({'figure.max_open_warning': 0})
    fig, ax = plt.subplots()
    df = pd.DataFrame()
    data = []
    sorted_data = []
    data = ExtractAndsort_data()
    test = 0
    filtbus = []
    for bus_data in data:
        #removing irrelevant columns
        del bus_data['Miles/SOC']
        del bus_data['Miles/kWh']
        del bus_data['Start Odometer']
        del bus_data['End Odometer']

        #####################################filterData
        #this will incorporated into the function above filterdata
        mean = bus_data["kWh/Miles"].mean()
        std = bus_data["kWh/Miles"].std()
        i = 0
        for item in bus_data["kWh/Miles"]:
            if item >= (mean - 3 * std) and item <= (mean + 3 * std):
                filtbus.append(item)
            else:
                bus_data.drop([i], axis = 0, inplace = True) #axis = 0 : row & inplace : makes permenant
            i += 1
        bus_data.reset_index(drop=True, inplace = True)
        test += 1
        i = 0
        for item in bus_data["Actual Distance"]:
            if item == 0.0:
                bus_data.drop([i], axis = 0, inplace = True)
            i += 1
        bus_data.reset_index(drop=True, inplace = True)
        plot_bus(bus_data, ax)
    #print(data[0])
    data = pd.concat(data, axis = 0, ignore_index = True)
        #########################
    plt.show() #show plot
    return()
main()
