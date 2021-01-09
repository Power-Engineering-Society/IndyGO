# Purpose  
The goal of this project is to provide **Indianapolis Public Transportation Corporation** (IndyGo) with analysis on how much energy of their electric buses is affected by external factors, i.e. passenger flow, weather conditions, bus's velocity. 
## Content
**IndyGo.zip**<br/>
The **zip folder** contains a folder with telematic data collected by IndyGo for the buses of interest in .csv files. <br/>The .csv file names correspond to day of the collected data.<br/> Data provided in these files include information on SOC, Energy usage, distance travelled, the odometer reading of the buses, and passenger flow.<br/><br/>
**bus_data.py**<br/>
This file contains the code in python for data analysis.<br/> 
After downloading this file, change the path in the code to where the zip folder will be stored in your system.<br/>
Functions have been incorporated so that any user may easily follow the code.<br/> 
Data has been sorted according to the bus_ID's, filtered using the 3-sigma model to remove the outliers present, and further refined by taking out the points of no interest.<br/> 
The pass_flow function has been incorporated in order to analyze the effect of passenger flow.
### Contributions
Any contributions to the code should be done on the `slave` branch. Only the code lead may push the code in the `main` branch.
