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
import tkinter

# Function to run a UI. Still learning how all this works so idk
def msui():
    tkinter._test()
    pass

msui()