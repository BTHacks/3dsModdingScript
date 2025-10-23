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
# Imports the tkinter library for UI usage, adds error catching for if the user doesn't have this library, as it isn't default on Linux
try:
    import tkinter as tk
except:
    answer = str(input("The Tkinter library is required to run this program. If you see this error and you're on linux, run the command listed in the readme. If you're on Windows, please submit an issue report so we can look further into it. Press any key to close the script"))
    quit()
# Imports ttk library
from tkinter import ttk
# Imports the file dialog library
from tkinter import filedialog
# Imports the platform module to detect operating systems
import platform

def createinstlist():
    del instlist[0]
    instlist.append("Welcome to the Nintendo 3DS modding script! \nThis script will assist you in modding your\nNintendo 3DS family system! \n \nBy continuing, you agree to this script creating\nand modifying files on your SD Card")
    instlist.append("Please turn off your system and remove the SD/MicroSD card\nthen put it in your computer. You will indicate where it is mounted in the upcoming dialog")
    instlist.append("The script will now download needed files to the SD card")
    instlist.append("In the next step, you will interact with the MSET9 batch script \nAll needed steps will be displayed")
    instlist.append("####### \nMSET9 Script Instructions \n####### \n1. Press the number for your console and firmware version \n2. Press the number 1 to create the hacked ID1 \n3. When done, press enter to close the script")
    instlist.append("######################## \nNEXT STEPS \n######################## \n1. Reinsert your SD card into your console \n2. Power on your console and launch the Mii Maker application \n3. Wait until you reach the 'Welcome to Mii Maker' screen, then close the app \n4. Launch system settings and navigate to: \n   Data Management > Nintendo 3DS > Software > Reset \n5. Power off your console STAY HOVERED OVER SYSTEM SETTINGS, THIS IS IMPORTANT \n6. Insert your SD card into your computer \n######################## \nIn the next step, you will interact with \nthe MSET9 script again")
    instlist.append("######################## \nMSET9 Instructions \n######################## \n1. Input the number of your console and firmware version \n2. If the window says 'Ready', press 0 to close the script \n########################")
    instlist.append("######################## \nContinuing on the 3DS \n######################## \n1. Reinsert your sd card and power the system on \n   If system settings isn't selected on boot, hover over it and reboot the console \n2. Launch system settings \n3. Navigate to \nData Management > Nintendo 3DS > Extra Data \n4. PRESS NOTHING, DO NOT TOUCH THE SCREEN UNTIL TOLD TO DO SO \n5. With the console STILL ON, remove your SD card from the console \n6. Insert your SD card into your computer \n######################## \nIn the next step, you will interact with \nthe MSET9 script. Instructions will \nbe shown")
    instlist.append("######################## \nMSET9 Instructions \n######################## \n1. Input the number corresponding to your console model and firmware version \n2. Input 3 to inject MSET9 \n3. Press enter to close the MSET9 script \n########################")
    instlist.append("######################## \nContinuing on the 3DS \n######################## \n1. Reinsert your SD Card, still pressing NOTHING \n2. You should boot into SafeB9SInstaller \n3. When prompted, input the key combo given on the top screen to install boot9strap \n4. Once it is complete (all seven steps on bottom screen are green), press A to reboot your device \n5. You should boot into the Luma3DS config menu \n   Don't change anything, you don't need to \n6. Press start to save and reboot \n7. Power off your console \n8. Remove your SD Card and put it in your computer \n######################## \nIn the next step, you will interact with \nthe MSET9 script. Instructions will \nbe shown")
    instlist.append("######################## \nMSET9 Instructions \n######################## \n1. Input the number corresponding with your console model and firmware version \n2. Input 4 and press enter \n3. Input 5 and press enter \n4. Press enter to close the script \n########################")
    instlist.append("######################## \nImportant notes before final setup \n######################## \nYour console now boots Luma3DS by default. It doesn't look any different from the stock HOME menu. If your console has booted into the HOME menu, it is running custom firmware \nThe final steps of this script will be adding some useful homebrew applications. You CAN skip this, but it's recommended you continue. \n \nBy continuing, the files will automatically be placed where they need to go \n########################")
    instlist.append("######################## \nContinuing on the 3ds \n######################## \nSection I \n######################## \n1. Insert your SD card into the console and power it on \n2. Once booted, press L + D-pad down + select \n3. Select 'Miscellaneous options \n4. Select 'Dump DSP firmware' \n5. Press B to continue \n6. Select 'Nullify user time offset' \n7. Keep pressing B until the Rosalina menu closes \n########################")
    instlist.append("######################## \nSection II \n######################## \n1. Power off your console \n2. Hold X, and while holding X power on the console \n   This will launch the setup helper \n3. If the helper was successful, your console will boot into GodMode9 \n   From now on, you can access GM9 by holding start on boot \n4. If you are prompted to create an essential files backup, press A to do so, then press A to continue once it's completed \n5. If you are prompted to fix the RTC date & time, press A to do so, set the date and time, and press A to continue \n6. Press HOME to bring up the actions menu \n7. Select 'Scripts...' \n8. Select 'finalize' \n9. Follow the prompts in the script, answering any questions that you are asked \n10. Once the script says 'Setup complete!', press A to power off the device \n11. Insert your SD card into your computer \n########################")
    instlist.append("######################## \nFinal steps \n######################## \n1. Copy the /gm9/backups/ folder to a safe location \n   This folder contains your critical file backups, and can revert a bricked console back to a working state \n2. After copying, these backups will be deleted by the script to maintain SD card storage \n########################")
    instlist.append("######################## \nCONGRATULATIONS! \n######################## \nYour 3ds system is now fully homebrewed! Have fun with your freedom! \n######################## \nYou may now close the window")
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
            os.makedirs(drivemount + "HackingScriptFiles") # Creates a neccessary directory for the script
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
    elif instructionnumber == 8:
        os.chdir(drivemount)
        os.startfile("MSET9-Windows.bat")
    elif instructionnumber == 10:
        os.chdir(drivemount)
        os.startfile("MSET9-Windows.bat")
    elif instructionnumber == 12:
        urllib.request.urlretrieve("https://github.com/hacks-guide/finalize/releases/latest/download/finalize.romfs", drivemount + "finalize.romfs") # Downloads a needed file right to the specified directory
        try:
            os.makedirs(drivemount + "luma") # Makes this directory if it doesn't already exist
        except FileExistsError:
            pass
        try:
            os.makedirs(drivemount + "luma/payloads") # Makes this directory if it doesn't already exist
        except FileExistsError:
            pass
        urllib.request.urlretrieve("https://github.com/hacks-guide/finalize/releases/latest/download/x_finalize_helper.firm", drivemount + "luma/payloads/x_finalize_helper.firm") # Downloads a needed file right to the specified directory
    elif instructionnumber == 15:
        try:
            shutil.rmtree(drivemount + "gm9/backups") # Deletes the backups folder and all files inside
        except FileNotFoundError:
            pass
        try:
            shutil.rmtree(drivemount + "HackingScriptFiles") # Deletes the hackingscriptfiles folder and all files inside
        except FileNotFoundError:
            pass
instructionnumber = int(0) # Sets the instruction number variable
instlist = ["Nothing here lmao"] # Creates an empty list
createinstlist() # Function to add to that list. I was doing it in line here, but it was just getting unwieldy honestly.
drivemount = str("N/A") # Creates an empty global variable (okay not actually empty but for all intents and purposes, it is empty)
mainwindow = tk.Tk() # Sets the command to the mainwindow variable
mainwindow.title("3DS Modding Script UI") # Sets title of the window
mainwindow.geometry("640x480") # Sets the resolution of the window
if platform.system() == "Windows":
    s = ttk.Style() # Sets the variable s to the style command
    s.theme_use("winnative") # Sets the theme to the native windows theming
elif platform.system() == "Linux":
    s = ttk.Style() # Sets the variable s to the style command
    s.theme_use("classic") # Sets the theme to the default Linux theme
txt = tk.Text(mainwindow, width=70, height=20) # Creates a text box within the frame
txt.insert(1.0, instlist[0]) # Inserts text from a defined list
txt.pack() # Dunno what this command really does, but without it the text doesn't appear, and the documentation for the tk library says it's needed so idk
button = ttk.Button(mainwindow, text="Continue", command=buttonclick) # Creates a button (windowlocation, text on button, command for button to execute))
button.pack() # Same here as with the txt.pack command, it's needed but I dunno why
mainwindow.mainloop() # Starts the window loop