#!/usr/bin/env python
#
#  rpiLapseCam.py
#

import os
import time
import logging
from datetime import datetime

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

# Define the location where you wish to save files. Set to HOME as default. 
# If you run a local web server on Apache you could set this to /var/www/ to make them 
# accessible via web browser.
folderToSave = "timelapse_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
os.mkdir(folderToSave)

# Set up a log file to store activities for any checks.
logging.basicConfig(filename=str(folderToSave) + "/timelapse.log",level=logging.DEBUG)

# Set the initial serial for saved images to 1
fileSerial = 1

# Run a WHILE Loop of infinitely
while True:
    d = datetime.now()
        
    # Set FileSerialNumber to 0000X using four digits
    fileSerialNumber = "%05d" % (fileSerial)

    # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
    hour = "%02d" % (d.hour)
    mins = "%02d" % (d.minute)
        
    # Define the size of the image you wish to capture. 
    imgWidth = 1920 # Max = 2592 
    imgHeight = 1080 # Max = 1944
        
    # Capture the image using raspistill. Set to capture with added sharpening, auto white balance and average metering mode
    # Change these settings where you see fit and to suit the conditions you are using the camera in
    os.system("raspistill -w " + str(imgWidth) + " -h " + str(imgHeight) + " -n -o " + str(folderToSave) + "/" + str(fileSerialNumber) +  ".jpg -ISO 400 -sh 20 -awb auto -mm matrix")

    # Write out to log file
    logging.debug(' Image saved: ' + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg")

    # Increment the fileSerial
    fileSerial += 1
    
    time.sleep(1)

