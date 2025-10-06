# Imports a URL request library to download files
import urllib.request
# Usage: urllib.request.urlretrieve("URL", "filename.fileextension")
# Imports OS library for directory creation
import os
# Directory creation usage:
# try:
#   os.makedirs("directorypath")
# except FileExistsError
#   pass

# Beginning of guide, disclaimer agreement
def guidedisclaimer():
    print("Welcome to the console hacking guide! This is a simple python script with instructions for console modding!")
    print("Note: All resources are from the website https://hacks.guide")
    print("I claim no ownership over the guide, troubleshooting steps, or any information provided.")
    print("IMPORTANT DISCLAMER, MUST READ BEFORE CONTINUING")
    print("Modifying your console carries a risk or permanent damage. The guides provided are tested, and troubleshooting is available, but there is no guarantee you won't irreversably brick your system. The individual/individuals following this guide are entirely responsible for what happens, and may not hold the author of the guides nor the program writer(s) responsible for any damage")
    print("This guide will automatically download any needed files for your selected guide, by running this program you agree to this program downloading said files. File sources will be commented in the source code, available on GitHub")
    print("")
    print("By typing y below, you agree to the above. Any other inputs will close the program")
    answer = str(input("Do you agree? "))
    if answer == "y":
        guidecontinue()
    else:
        print("The program will now close.")
    pass

# Guide selection script, can be called after disclaimer, upon guide completion, or if a certain input is chosen within other sections
def guidecontinue():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Please select what guide you would like")
    print("Available guides:")
    print("1) 3ds 2) Wii 3) Wii U 4) Playstation Vita")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Enter selection: "))
        if answer == "1":
            guide3ds()
            activeinput = int(0)
        elif answer == "2":
            guidewii()
            activeinput = int(0)
        elif answer == "3":
            guidewiiu()
            activeinput = int(0)
        elif answer == "4":
            guidevita()
            activeinput = int(0)
        else:
            print("Invalid input, try again")
    pass

# Function to run the 3ds section of the guide
def guide3ds():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Welcome to the Nintendo 3ds homebrew guide. We will begin by going over key information.")
    answer = str(input("Press any key to continue"))
    print("")
    print("Compatible systems for this guide: Nintendo 3ds, 3ds XL/LL, 2ds, New 3ds, New 3ds XL/LL, New 2ds XL/LL")
    print("Supported regons: all")
    print("What you need: A computer, a way to read and write to your 3ds system's SD/Micro SD card")
    print("If you do not meet these requirements, or wish to go back, type n on the upcoming prompt. Any other input will continue the guide")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Continue?"))
        if answer == "n":
            print("The guide will now go back to the selection menu")
            guidecontinue()
            activeinput = int(0)
        else:
            activeinput = int(0)
    print("")
    print("The guide will now continue")
    print("Before starting this guide, we will check if your system already has CFW installed.")
    print("CFW CHECK STEPS")
    print("1. Power off your system")
    print("2. Hold select while powering on the system")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Does your console boot to the normal home menu? (y/n)"))
        if answer == "y":
            print("Your system does not have CFW installed, you may continue with the guide")
            activeinput = int(0)
        elif answer == "n":
            print("Your system may have custom firmware, we will continue to a further check.")
            guide3dscfwcheck()
            activeinput = int(0)
        else:
            print("Invalid input, try again")
    print("Before continuing, please make sure your console is on the latest official 3ds firmware")
    print("Latest firmware: Ver. 11.17.0-50")
    print("If your system is not on the latest firmware, please update before continuing")
    answer = str(input("Press any key to continue: "))
    print("")
    print("Please enter which type of 3ds system you have")
    print("1) Old (3ds, 3ds XL/LL, 2ds) 2) New (New 3ds, New 3ds XL/LL, New 2ds XL/LL)")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("System type: "))
        if answer == "1":
            print("Continuing with Old 3ds guide")
            guide3dsold()
            activeinput = int(0)
        elif answer == "2":
            print("Continuing with New 3ds guide")
            guide3dsnew()
            activeinput = int(0)
        else:
            print("Invalid input, try again.")
    pass

# Function for the custom firmware check of the initial guide
def guide3dscfwcheck():
    loopvar = int(50)
    while loopvar >= 50:
        print("")
        loopvar = loopvar - 1
    print("Required reading")
    print("This is an add-on section to check if your console already has a modern custom firmware")
    print("If your console already has an arm9loaderhax or boot9strap based custom firmware, you will need to follow the instructions indicated to upgrade your setup to a modern one")
    print("")
    print("Instructions:")
    answer = str(input("Step 1: Power off your console"))
    answer = str(input("Step 2: Hold the select button"))
    answer = str(input("Step 3: Power on your console while still holding the select button"))
    answer = str(input("Step 4: You should now see a configuration menu of some sort"))
    print("")
    print("What happened?")
    print("1. Console just booted to the home menu")
    print("2. A config menu popped up")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Input:"))
        if answer == "1":
            print("You do not have custom firmware, returning to the beginning of the guide")
            guide3ds()
            activeinput = int(0)
        elif answer == "2":
            activeinput = int(0)
            pass
        else:
            print("Invalid input, please try again")
    print("")
    print("You should see a version of Luma3DS on the screen.")
    print("1. Version 7.0.5 or lower")
    print("2. Version 7.1")
    print("3. Version 8.0 or newer")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Please enter the number corresponding with the version shown"))
        if answer == "1":
            print("Continuing to the section of updating A9LH to B9S")
            guide3dsa9lh2b9s()
            activeinput = int(0)
        elif answer == "2":
            print("Continuing to updating B9S")
            guide3dsupdateb9s()
            activeinput = int(0)
        elif answer == "3":
            print("Continuing to restoring/updating CFW")
            guide3dsupdateorrestorecfw()
            activeinput = int(0)
        else:
            print("Invalid input, please try again")
    pass

# Function for updating A9LH to B9S
def guide3dsa9lh2b9s():
    pass

# Function for updating B9S
def guide3dsupdateb9s():
    pass

# Function for restoring and updating CFW
def guide3dsupdateorrestorecfw():
    pass

# Functon for the "Old 3ds" section of the guide
def guide3dsold():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("We will now install CFW on your system using the MSET9 method")
    print("Any required files will be downloaded to C:\ConsoleHackingScript\phaseone")
    try:
        os.makedirs("C:/ConsoleHackingScript/phaseone/ ")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/hacks-guide/MSET9/releases/download/v2.1/MSET9-v2.1.zip", "C:\ConsoleHackingScript\phaseone\MSET9-v2.1.zip")
    print("")
    print("Section I: Prep work") # Instructions in sections will use input check functions rather than print functions so you can stop and read each step. This is not a mistake, but an intended function
    print("")
    answer = str(input("Step 1: Insert your SD card into your computer"))
    answer = str(input("Step 2: Copy all files from MSET9.zip to the root of your SD card. If any files already exist, override them."))
    answer = str(input("Step 3: Run the MSET9 script (MSET9-windows.bat)"))
    answer = str(input("Step 4: Input the number correspoding with your model of 3ds"))
    answer = str(input("Step 5: Type 1 to begin the process of creating your MSET9 ID1"))
    answer = str(input("Step 6: After reviewing the disclaimer, type 1 and hit enter to begin the process"))
    print("Step 7: If you see the message Created Hacked ID1, press Enter to close the MSET9 script")
    answer = str(input("-Your console will appear to lose most data / no user-installed apps on HOME Menu. This is expected. Your data will come back at a later step"))
    answer = str(input("Step 8: Reinsert your SD card and power on your console"))
    answer = str(input("Step 9: Open the Mii maker application"))
    answer = str(input("Step 10: Wait for your console to reach the Welcome to Mii Maker screen, then exit Mii Maker and return to the HOME menu"))
    print("Step 11: Launch system settings and navigate to Data management > Nintendo 3DS > Software > reset")
    answer = str(input("-This will NOT wipe any of your data"))
    answer = str(input("Step 12: Power off your console and insert your SD card back into your computer"))
    answer = str(input("Step 13: Run the MSET9 script (MSET9-Windows.bat)"))
    answer = str(input("Step 14: Type the number corresponding with your console model and version, then press enter. You should see the word ready in green text"))
    answer = str(input("Step 15: Type 0 and press enter to close the script"))
    answer = str(input("Step 16: Re insert your SD card into your console"))
    print("")
    print("")
    print("Section II: MSET9")
    print("In this section, you will trigger MSET9 to launch SafeB9SInstaller (the custom firmware installer)")
    answer = str(input("These instructions must be followed EXACTLY, so double check EVERYTHING you are doing to avoid errors!"))
    print("")
    print("Step 1: Power on your console, ensuring System Settings is selected")
    answer = str(input("-If System Settings is not selected, hover over the System Settings icon using the D-Pad, power your console off, then back on"))
    answer = str(input("Step 2: Press (A) to launch system settings"))
    answer = str(input("Step 3: Navigate to Data Management > Nintendo 3DS > Extra Data"))
    answer = str(input("Step 4: DO NOT PRESS ANY BUTTONS OR TOUCH THE SCREEN ON YOUR CONSOLE"))
    print("Step 5: With the console STILL ON, and without pressing any buttons or touching the screen, remove your SD card from the console")
    answer = str(input("-The menu will refresh and say that no SD card is inserted, which is expected"))
    answer = str(input("Step 6: Insert your SD card into your computer"))
    answer = str(input("Step 7: Run the MSET9 script (MSET9-Windows.bat)"))
    answer = str(input("Step 8: Type the number corresponding to your console model and version, then press enter"))
    print("Step 9: In the MSET9 windows, type 3, then press enter to inject MSET9")
    answer = str(input("-You should see 'MSET9 successfully injected!'"))
    answer = str(input("Step 10: Press enter to close the MSET9 script"))
    answer = str(input("Step 11: Reinsert your SD card into your console STILL NOT PRESSING ANY BUTTONS OR TOUCHING THE SCREEN"))
    answer = str(input("Step 12: If the exploit was successful, you will have booted into SafeB9SInstaller"))
    print("")
    print("")
    print("Section III: Installing boot9strap")
    print("")
    answer = str(input("In this section, you will install custom firmware onto your console"))
    print("Step 1: When prompted, input the key combo given on the top screen to install boot9strap")
    print("-If the top screen is blank and you see 'Crypto Status - all checks passed' on the bottom screen, you will have to input the key combo blindly. Press the following buttons on your console in the given order")
    answer = str(input("  Left, Down, Right, Up, A"))
    answer = str(input("Step 2: Once it is complete (all seven steps on the bottom screen are green), press (A) to reboot your console"))
    print("Step 3: Your console should have booted into the Luma3DS config menu")
    print("-This menu contains settings for the Luma3DS Custom Firmware")
    answer = str(input("-For the purposes of this guide, leave these settings as is"))
    answer = str(input("Step 4: Press start to save and reboot"))
    print("")
    print("")
    print("Section IV: Removing MSET9")
    print("In this section, you will remove MSET9 to prevent further issues and to restore your user data. This will not remove the custom firmware just installed")
    answer = str(input("DO NOT SKIP THIS SECTION!!! IF YOU SKIP IT, YOU WILL ENCOUNTER MANY ISSUES"))
    print("")
    answer = str(input("Step 1: Power off your console"))
    answer = str(input("Step 2: Insert your SD card into your computer"))
    answer = str(input("Step 3: Run the MSET9 script (MSET9-Windows.bat"))
    print("Step 4: Type the number corresponding to your console model and version, then press enter")
    answer = str(input("-The current state should display infected"))
    print("Step 5: Type 4, then press enter to remove the trigger file")
    answer = str(input("-You should see 'removed trigger file'"))
    print("Step 6: Type 5, then press enter to remove MSET9")
    answer = str(input("-You should see 'Successfully removed MSET9!'"))
    answer = str(input("Step 7: Press enter to close the MSET9 script"))
    print("")
    print("At this point, your console will boot Luma3DS by default")
    print("-Luma3DS does not look any different from the normal home menu. If your console has booted into the home mnu, it is running custom firmware")
    answer = str(input("In the next section, you will install useful homebrew applications to complete your setup"))
    guide3dsfinalsetup()

# Function for the "New 3ds" Section of the guide
def guide3dsnew():
    pass

# Function for the finalize setup section of the guide
def guide3dsfinalsetup():
    pass

guidedisclaimer()