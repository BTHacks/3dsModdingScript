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
def buttonclick():
    localvar = int(instructionnumber)
    localvar = localvar + 1
    del instlist[0]
    txt.delete(1.0, "end")
    txt.insert(1.0, instlist[0])

    pass
instructionnumber = int(0) # Sets the instruction number variable
instlist = ["asdfnjasrnfkaenrflhaernf"] # Sets the instruction list 
mainwindow = tk.Tk() # Sets the command to the mainwindow variable
mainwindow.title("3DS Modding Script UI") # Sets title of the window
mainwindow.geometry("640x480") # Sets the resolution of the window
frame = tk.Frame(mainwindow) # Creates an in-window frame
frame['width'] = 600 # Sets pixel density of the frame
frame['height'] = 400
txt = tk.Text(frame, width=40, height=10) # Creates a text box within the frame
txt.insert(1.0, instlist[0]) # Inserts text from a defined list
frame.pack() # Pack functions are needed to actually insert elements
txt.pack()
button = tk.Button(mainwindow, text="Continue", command=buttonclick) # Creates a button (windowlocation, text on button, command for button to execute))
button.pack()
mainwindow.mainloop() # Starts the window loop