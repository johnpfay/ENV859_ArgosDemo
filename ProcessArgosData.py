# ProcessArgosData.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: John Fay (jpfay@duke.edu)
# Created on: Oct 2016

# Create a variable pointing to the file with no header
fileName = "V:\\Scripting3\\SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineStrings = fileObj.readlines()
print "There are " + str(len(lineStrings)) + " records in the file"
    
# Close the file object
fileObj.close()

#Create empty dictionaries
dateDict= {}
locationDict = {}
omittedRecordCount = 0

# Use a for loop to read each line, one at a time, until the list is exhausted
for lineString in lineStrings:

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    if obsLC in ("1","2","3"):
        # Add values to dictionary
        dateDict[recordID] = obsDateTime.split()   
        locationDict[recordID] = (obsLat, obsLon)
    else:
        omittedRecordCount = omittedRecordCount + 1

# Indicate script is complete
print str(len(dateDict)) + " records added"
print str(omittedRecordCount) + " records omitted"