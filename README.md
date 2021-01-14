# Project Goal  
- Analyze **Indianapolis Public Transportation Corporation** (IndyGo) electric buses electric range.
- Key factors for relatively ineffiecient energy range.  
## Content
**IndyGo.zip**<br/>
- Contains .CVS files with telematic data collected by IndyGo for the buses of interest. <br/> - The .csv file names correspond to day of the collected data.<br/>    - Data provided: SOC, Energy usage, distance travelled, odometer reading, and passenger flow.<br/><br/>

**bus_data.py**<br/>
File contains the code in python.<br/> 
Note: After downloading this file, change the path in the code to where the zip folder will be stored in your system.<br/>

***Main***
- Data is stored from *ExtractAndsort_data()*. in a data drame.
  - *ExtractAndsort_data()*: sorts data according to bus ID.
- for bus_data in data:
  --Columns of no interest are removed in the for loop. 
- for item in bus_data:
  --Data is filtered using the 3-sigma methodology.<br/> 
<br/> 
The pass_flow function has been incorporated in order to analyze the effect of passenger flow.
### Contributions
Any contributions to the code should be done on the `slave` branch. Only the code lead may push the code in the `main` branch.
