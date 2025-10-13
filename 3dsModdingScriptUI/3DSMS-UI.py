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

def continue_script(): # Just a button test script, nothing more
    os.makedirs("C:\\Poopass\\")
    pass
def main_window(): # Script to create the main window of the program
    mainwindow = tk.Tk()
    mainwindow.title("3DS Modding Script UI") # Sets title of the window
    mainwindow.geometry("640x480") # Sets the resolution of the window
    label = tk.Label(mainwindow, text="We are so fucking back") # Sets the main label text of the window
    label.pack(pady=20) # Sets the distance of the label from the top of the screen
    button = tk.Button(mainwindow, text="Continue", command=continue_script) # Creates a button (windowlocation, text on button, command for button to execute)
    button.pack() # Sets distance of button from the last object in the window
    mainwindow.mainloop() # Starts the window loop

main_window()