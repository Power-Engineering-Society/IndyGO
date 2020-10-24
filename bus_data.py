################################################################################
# Author: Zeeshan Babar
# Date: 10/24/2020
# This program imports the data on the electric buses provided by Indigo
################################################################################
import pandas as pd      #will be using pandas for data analysis
import glob as gb      #glob finds all the pathnames matching a specified pattern
path = r'C:\Indigo' #path of data files & r to address any special characters in the path
all_files = gb.glob(path + "/*.csv") #file
li = [] #list of data files
for filename in all_files:
    data = pd.read_csv(filename, index_col = None, header = 0) # store the data in the file.
    li.append(data) # add data in the list in element
frame = pd.concat(li, axis = 0, ignore_index = True)
