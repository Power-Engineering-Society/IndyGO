import numpy as np
import pandas as pd
import csv
import glob as gb
import math
import matplotlib.pyplot as plt

def busID(reader):
    global bus
    bus = []
    for row in reader:
        bus_id = row[0]
        bus.append(bus_id)
    return(bus)

def sortData(data, bus):
    bus_ID = ['IG_1899', 'IG_1970', 'IG_1971', 'IG_1971', 'IG_1972', 'IG_1973', 'IG_1974', 'IG_1975', 'IG_1976', 'IG_1977'
              'IG_1979', 'IG_1980', 'IG_1981', 'IG_1982', 'IG_1983', 'IG_1984', 'IG_1985', 'IG_1986', 'IG_1988', 'IG_1989'
              'IG_1991', 'IG_1992', 'IG_1994', 'IG_1995', 'IG_1996', 'IG_1997', 'IG_1999']
    bus.append(data[data['Bus No.'].apply(lambda state: state == bus_ID)].head())
    bus = pd.concat(bus, axis = 0, ignore_index = True)

def plot_bus(bus, ax):
    ax.scatter(bus['Actual Distance'], bus['Energy Used'])
    plt.title('Energy Used Vs. Actual Distance')
    plt.xlabel('Distance Travelled (miles)')
    plt.ylabel('Energy Used (kWh)')

def ExtractAndsort_data():
    path = r'Indigo'
    all_files = gb.glob(path + "/*.csv")
    li = []
    buses = []
    buses_arr = [[] for i in range(27)]
    
    for filename in all_files:
        data = pd.read_csv(filename, index_col = None, header = 0)
        li.append(data)
        state_arr = ["IG_1899", "IG_1999", "IG_1995", "IG_1994", "IG_1992", "IG_1991", "IG_1990",
        "IG_1989", "IG_1996", "IG_1997", "IG_1979", "IG_1981", "IG_1982", "IG_1984", "IG_1986",
        "IG_1988", "IG_1971", "IG_1974", "IG_1975", "IG_1976", "IG_1980", "IG_1983", "IG_1985",
        "IG_1970", "IG_1972", "IG_1973", "IG_1977"]
        for i in range(27):
            buses_arr[i].append(data[data['Bus No.'].apply(lambda state: state == state_arr[i])].head())

    for i in range(27):
        buses_arr[i] = pd.concat(buses_arr[i], axis = 0, ignore_index = True)
        buses.append(buses_arr[i])

    li = pd.concat(li, axis = 0, ignore_index = True)
    return(buses)

def filterData(bus,df):
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

def main():
    ax = plt.subplots()[1]
    data = []
    data = ExtractAndsort_data()
    test = 0
    filtbus = []
    for bus_data in data:
        del bus_data['Miles/SOC']
        del bus_data['Miles/kWh']
        del bus_data['Start Odometer']
        del bus_data['End Odometer']
        mean = bus_data["kWh/Miles"].mean()
        std = bus_data["kWh/Miles"].std()
        i = 0
        for item in bus_data["kWh/Miles"]:
            if item >= (mean - 3 * std) and item <= (mean + 3 * std):
                filtbus.append(item)
            else:
                bus_data.drop([i], axis = 0, inplace = True)
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
    data = pd.concat(data, axis = 0, ignore_index = True)
    plt.show()

if __name__ == "__main__":
    main()