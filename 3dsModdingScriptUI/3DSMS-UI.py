# Imports a URL request library to download files
import urllib.request
# Usage: urllib.request.urlretrieve("URL", "filename.fileextension")
#
# Imports OS library for directory creation
import os
# Directory creation usage:
# try:
#   os.makedirs(r"directorypath")
# except FileExistsError
#   pass
#
# Imports the random library, just so I can randomize the ASCII art at startup
import random
#
# Imports the ZipFile library, used to unzip files
from zipfile import ZipFile
# Usage:
# For unzipping all files from a zip:
# with Zipfile(r"PathToFile", 'r') as zObject
#   zObject.extractall(path=r"PathToExtractTo")
#
# For unzipping a specific file:
# with ZipFile(r"PathToFile", 'r') as zObject
#   zObject.extract("NameOfFile", path=r"PathToExtractTo")
# zObject.close
#
# Imports the shutil library for directory management (specifically directory removal)
import shutil
# Usage for removal:
# shutil.rmtree(path)
#
# Imports time library for wait functions
import time
# Usage:
# time.sleep(time in seconds)
#
# Imports the tkinter library for UI usage
import tkinter as tk
# Imports the file dialog library
from tkinter import filedialog
def buttonclick():
    global instructionnumber # Declares intent to modify a global variable
    global drivemount # Declares intent to modify THIS global variable as well
    instructionnumber = instructionnumber + 1 # Increases it by one
    del instlist[0] # Deletes the initial entry in the main list
    txt.delete(1.0, "end") # Deletes the entire text window
    txt.insert(1.0, instlist[0]) # Inserts the new first entry in the list
    if instructionnumber == 2:
        dirname = filedialog.askdirectory() # Pops up a directory input
        drivemount = dirname # Sets the global drivemount variable to the specified directory
        pass
    elif instructionnumber == 3:
        try:
            os.makedirs(drivemount + "HackingScriptFiles/") # Creates a neccessary directory for the script
        except FileExistsError:
            pass
        urllib.request.urlretrieve("https://github.com/hacks-guide/MSET9/releases/download/v2.1/MSET9-v2.1.zip", drivemount + "HackingScriptFiles/MSET9.zip") # Downloads the files for MSET9
        with ZipFile(drivemount + "HackingScriptFiles/MSET9.zip", 'r') as zObject: # Sets the needed variables for ZipFIle to work
            zObject.extractall(path=drivemount) # Unzips the files at the specified location
    elif instructionnumber == 4:
        os.chdir(drivemount) # Sets the target directory to the mounted drive
        os.startfile("MSET9-Windows.bat") # Launches the target .bat file
    elif instructionnumber == 6:
        os.chdir(drivemount)
        os.startfile("MSET9-Windows.bat")
instructionnumber = int(0) # Sets the instruction number variable
# Arduously long list of every instruction
instlist = ["Welcome to the Nintendo 3DS modding script! \nThis script will assist you in modding your\nNintendo 3DS family system! \n \nBy continuing, you agree to this script creating\nand modifying files on your SD Card", "Please turn off your system and remove the SD/MicroSD card\nthen put it in your computer. You will indicate where it is mounted in the upcoming dialog", "The script will now download needed files to the SD card", "In the next step, you will interact with the MSET9 batch script \nAll needed steps will be displayed", "####### \nMSET9 Script Instructions \n####### \n1. Press the number for your console and firmware version \n2. Press the number 1 to create the hacked ID1 \n3. When done, press enter to close the script", "######################## \nNEXT STEPS \n######################## \n1. Reinsert your SD card into your console \n2. Power on your console and launch the Mii Maker application \n3. Wait until you reach the 'Welcome to Mii Maker' screen, then close the app \n4. Launch system settings and navigate to: \n   Data Management > Nintendo 3DS > Software > Reset \n5. Power off your console STAY HOVERED OVER SYSTEM SETTINGS, THIS IS IMPORTANT \n6. Insert your SD card into your computer \n######################## \nIn the next step, you will interact with \nthe MSET9 script again", "######################## \nMSET9 Instructions \n######################## \n1. Input the number of your console and firmware version \n2. If the window says 'Ready', press 0 to close the script \n########################"]
drivemount = str("N/A")
mainwindow = tk.Tk() # Sets the command to the mainwindow variable
mainwindow.title("3DS Modding Script UI") # Sets title of the window
mainwindow.geometry("640x480") # Sets the resolution of the window
frame = tk.Frame(mainwindow) # Creates an in-window frame
frame['width'] = 600 # Sets pixel density of the frame
frame['height'] = 400
txt = tk.Text(frame, width=70, height=20) # Creates a text box within the frame
txt.insert(1.0, instlist[0]) # Inserts text from a defined list
frame.pack() # Pack functions are needed to actually insert elements
txt.pack()
button = tk.Button(mainwindow, text="Continue", command=buttonclick) # Creates a button (windowlocation, text on button, command for button to execute))
button.pack()
mainwindow.mainloop() # Starts the window loop