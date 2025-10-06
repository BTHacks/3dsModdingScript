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
            guide3dsmset9()
            activeinput = int(0)
        elif answer == "2":
            print("Continuing with New 3ds guide")
            guide3dssuperskaterhax()
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
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Updating A9LH to B9S")
    print("Notice: this section of the script cannot be used if you have a New 3ds system (New Nintendo 3ds, New Nintendo 3ds XL/LL, New Nintendo 2ds XL/LL)")
    print("You will have to go to https://3ds.hacks.guide/a9lh-to-b9s.html if you have one of those systems")
    print("Enter y below to continue with the guide, only if you do not have one of the above mentioned systems")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Continue?"))
        if answer == "y":
            activeinput = int(0)
        else:
            print("The program will now close.")
            quit
    print("Required files will now download to C:\ConsoleHackingScript\a9lh2b9s")
    try:
        os.makedirs("C:/ConsoleHackingScript/a9lh2b9s")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/download/v13.3.3/Luma3DSv13.3.3.zip", "C:\ConsoleHackingScript\a9lh2b9s\LumaLatest.zip")
    urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/download/v7.0.5/Luma3DSv7.0.5.zip", "C:\ConsoleHackingScript\a9lh2b9s\LumaOld.zip")
    urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "C:\ConsoleHackingScript\a9lh2b9s\SafeB9SInstaller.zip")
    urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/download/1.4/boot9strap-1.4.zip", "C:\ConsoleHackingScript\a9lh2b9s\boot9strap.zip")
    print("")
    print("Section I: Prep Work")
    print("-For all steps in this section, if any of the files already exist, overwrite them with the new files")
    answer = str(input("Step 1: Power off your console"))
    answer = str(input("Step 2: Insert your SD card into your computer"))
    answer = str(input("Step 3: Copy everything from LumaLatest.zip to the root of your SD card"))
    answer = str(input("Step 4: Copy arm9loaderhax.bin from LumaOld.zip to the root of your SD card"))
    print("Step 5: Copy SafeB9SInstaller.bin from SafeB9SInstaller.zip to /luma/payloads on your SD card")
    print("-If /luma or /luma/payloads doesn't exist, create them")
    answer = str(input("-Delete any other .bin payloads in the folder, if they exist"))
    answer = str(input("Step 6: Create a folder named boot9strap on the root of your SD card"))
    answer = str(input("Step 7: Copy boot9strap.firm and boot9strap.firm.sha from boot9strap.zip to the /boot9strap folder on your SD card"))
    answer = str(input("Step 8: Reinsert your SD card into your console"))
    print("")
    print("")
    print("Section II: Installing boot9strap")
    print("Step 1: Boot your console while holding start to launch SafeB9SInstaller")
    print("-If you see the Luma config menu, simply press start to restart your console and try again")
    answer = str(input("-If this gives you an error, backup your files and format the SD card, or try a new one"))
    answer = str(input("Step 2: Wait for all safety checks to complete"))
    answer = str(input("Step 3: When prompted, input the key combo given on the top screen to install boot9strap"))
    answer = str(input("Step 4: Your console should have booted into the Luma Config menu"))
    answer = str(input("Step 5: Press start to save and reboot"))
    guide3dsfinalsetup()

# Function for updating B9S
def guide3dsupdateb9s():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar + 1
    print("Updating boot9strap")
    print("Required Reading")
    answer = str(input("This section is for existing boot9strap users to update their installation of boot9strap to the latest version"))
    print("Required files will be downloaded to C:\ConsoleHackingScript\updateb9s")
    try:
        os.makedirs("C:/ConsoleHackingScript/updateb9s")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "C:\ConsoleHackingScript\updateb9s\SafeB9SInstaller.zip")
    urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/download/1.4/boot9strap-1.4.zip", "C:\ConsoleHackingScript\updateb9s\boot9strap.zip")
    urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/download/v13.3.3/Luma3DSv13.3.3.zip", "C:\ConsoleHackingScript\updateb9s\LumaLatest.zip")
    print("")
    print("Section I: Prep work")
    answer = str(input("For all steps in this section, overwrite any existing files on your SD card."))
    answer = str(input("Step 1: Insert your SD Card into your computer"))
    answer = str(input("Step 2: Create a folder named boot9strap on the root of the SD Card"))
    answer = str(input("Step 3: Copy boot9strap.firm and boot9strap.firm.sha from boot9strap.zip to the boot9strap folder on your SD Card"))
    answer = str(input("Step 4: Copy SafeB9SInstaller.firm from SafeB9SInstaller.zip to the root of your SD Card, rename it to boot.firm"))
    answer = str(input("Step 5: Reinsert your SD Card into your console"))
    print("")
    print("Section II: Installing boot9strap")
    print("Step 1: Power on your console")
    answer = str(input("-This should automatically launch SafeB9SInstaller"))
    answer = str(input("Step 2: When prompted, input the key combo given on the top screen to install boot9strap"))
    print("Step 3: Once completed, force your console off by holding down the power button")
    answer = str(input("-Until the next section is complete, the console will only boot SafeB9SInstaller"))
    print("")
    print("Section III: Update Luma3DS")
    answer = str(input("Step 1: Insert your SD card into your computer"))
    answer = str(input("Step 2: Copy everything from LumaLatest.zip to the root of the SD Card, replacing any existing files"))
    answer = str(input("Step 3: Reinsert your SD Card into your console"))
    answer = str(input("Step 4: Power on your console"))
    print("Step 5: If your console has booted into the Luma3DS configuration menu, press start to save and reboot")
    answer = str(input("-Don't change any settings"))
    guide3dsfinalsetup()

# Function for restoring and updating CFW
def guide3dsupdateorrestorecfw():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Restoring / updating CFW")
    print("Required reading:")
    print("This sections prepares consoles with an existing modern boot9strap installation for reinstallation and/or updating of custom firmware applications. It can also be used in the event of a lost or corrupted SD Card")
    answer = str(input("Your SD card must be formatted as Fat32"))
    print("The script will now download needed files to C:\ConsoleHackingScript\updatecfw")
    try:
        os.makedirs("C:/ConsoleHackingScript/updatecfw/")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/download/v13.3.3/Luma3DSv13.3.3.zip", "C:\ConsoleHackingScript\updatecfw\LumaLatest.zip")
    answer = str(input("Step 1: Insert your SD card into your computer"))
    answer = str(input("Step 2: Copy everything from LumaLatest.zip to the root of your SD card. If any of these files exist, overwrite them"))
    answer = str(input("Step 3: Reinsert your SD Card int your console"))
    answer = str(input("Step 4: Power on your console"))
    guide3dsfinalsetup()

# Functon for the "MSET9" section of the guide
def guide3dsmset9():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Old 3DS Homebrew installation")
    print("We will now install CFW on your system using the MSET9 method")
    print("Any required files will be downloaded to C:\ConsoleHackingScript\mset9")
    try:
        os.makedirs("C:/ConsoleHackingScript/mset9/ ")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/hacks-guide/MSET9/releases/download/v2.1/MSET9-v2.1.zip", "C:\ConsoleHackingScript\mset9\MSET9-v2.1.zip")
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

# Function for the "super-skaterhax" Section of the guide
def guide3dssuperskaterhax():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Note: this guide takes less time, but is known to be inconsistent. If you wish to use a more consistent exploit, type n below to be rerouted to the MSET9 section")
    activeinput = int(1)
    while activeinput == 1:
        answer = str(input("Do you wish to continue? (y/n) "))
        if answer == "y":
            activeinput = int(0)
        elif answer == "n":
            guide3dsmset9()
            activeinput = int(0)
        else:
            print("Invalid input, try again")
    print("")
    print("Compatibility notes:")
    answer = str(input("This exploit, known as super-skaterhax, is compatible with New models on version 11.15.0 and above in all regions"))
    print("Needed files will now be downloaded to C:\ConsoleHackingScript\superskaterhax")
    try:
        os.makedirs("C:/ConsoleHackingScript/superskaterhax")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/zoogie/super-skaterhax/releases/download/v1.1/release_new3ds_v1.1.zip", "C:\ConsoleHackingScript\superskaterhax\skaterhax.zip")
    print("")
    print("Section I: Prep work")
    answer = str(input("In this section, you will copy the files needed to trigger both super-skaterhax and the Homebrew Launcher"))
    answer = str(input("Step 1: Power off your console"))
    answer = str(input("Step 2: Insert your SD card into your computer"))
    answer = str(input("Step 3: Extract skaterhax.zip, and open the folder with your region and version number"))
    answer = str(input("Step 4: Copy everything from that folder onto the root of your SD card"))
    answer = str(input("Step 5: Reinsert your SD card into your console and power it on"))
    answer = str(input("Step 6: Launch system settings"))
    answer = str(input("Step 7: Select 'other settings'"))
    answer = str(input("Step 8: Navigate to profile > region settings"))
    answer = str(input("Step 9: Select your region, then select Do Not Set"))
    answer = str(input("Step 10: Navigate to 'Date & Time'"))
    answer = str(input("Step 11: Set the date and time to your current date and time"))
    answer = str(input("Step 12: Exit system settings"))
    print("")
    print("Section II: super-skaterhax")
    answer = str(input("In this section, you will visit the browser exploit webpage, which will launch the Homebrew Launcher"))
    print("")
    answer = str(input("Step 1: Open the internet browser"))
    answer = str(input("Step 2: Tap the 3-line menu in the bottom right corner of the screen"))
    answer = str(input("Step 3: tap settings, scroll down, then reset save data > clear all > clear > ok"))
    answer = str(input("Step 4: Reopen the web browser"))
    answer = str(input("Step 5: tap next > google > ok > ok"))
    answer = str(input("Step 6: tap the address bar on the bottom screen"))
    print("Step 7: Enter the URL corresponding to your console's region")
    print("-USA/EUR/JPN: https://skater.686178.xyz/go/super")
    answer = str(input("-KOR: https://skater.686178.xyz/go/korea"))
    print("Step 8: Tap 'open'")
    answer = str(input("-You should see the text 'GO! GO!' Do not click it yet"))
    answer = str(input("Step 9: Open the 3-line menu on the bottom-right corner of the screen"))
    answer = str(input("Step 10: Tap on 'Add to bookmarks'"))
    answer = str(input("Step 11: Tap on the 3-line menu again"))
    answer = str(input("Step 12: Tap on settings > delete cookies > yes"))
    answer = str(input("Step 13: Press home to return to the home menu, then immediately reopen the internet browser"))
    answer = str(input("Step 14: Wait for the page to fully load, then tap the 'GO! GO!' button on the top of the bottom screen"))
    answer = str(input("Step 15: Wait for the page to fully load, then press A to dismiss the popup"))
    print("Step 16: If your console displays:")
    print("-'The Homebrew Launcher' screen: Continue to the next step")
    print("-A white 'error has occurred' message box: The exploit has failed due to random chance. Open system settings, change language (if possible), close system settings, then retry the steps in this section")
    print("--On JPN/KOR region consoles, there is only one language setting. On those consoles, open then close system settings, then retry this section")
    print("--If the exploit is still unsuccessful after 5 attempts, there may be a problem with your files or prep work. Ensure region and date and time are correct, and that you have been following this section EXACTLY")
    print("--If the exploit is still unsuccessful after 10 steps, input 1 on the next prompt in this script to be redirected to MSET9")
    print("-A black screen that says 'an error has occurred': Your file placement is incorrect. Ensure the files are on the root of the SD card")
    print("-A yellow screen: The Homebrew Launcher failed to open due to random chance. Hold the power button to force shut off the console, then retry this section")
    print("-The word 'text': You have an old 3ds. This exploit will not work on the old 3ds. Type 1 in the prompt in this script to be redirected to MSET9")
    answer = str(input("Prompt: "))
    if answer == "1":
        guide3dsmset9()
    answer = str(input("Step 17: Launch nimdsphax from the list of homebrew"))
    print("Step 18: If the exploit was successful, you will have booted into safeB9Sinstaller")
    answer = str(input("-If your console freezes on a red or green screen, hold the power button to shut off the console, then retry this section"))
    print("")
    print("Section III: Installing boot9strap")
    answer = str(input("In this section, you will install custom firmware onto your console"))
    answer = str(input("Step 1: When prompted, input the key combo given on the top screen to install boot9strap"))
    answer = str(input("Step 2: Once it is complete, press A to reboot your console"))
    print("Step 3: Your console should have booted into the Luma3DS configuration menu")
    answer = str(input("-Do not change any settings!"))
    answer = str(input("Step 4: Press start to save and reboot"))
    print("")
    print("At this point, your console will boot to Luma3DS by default")
    print("-Luma3DS does not look any different from the normal HOME Menu. If your console has booted into the HOME Menu, it is running custom firmware")
    answer = str(input("-In the next section, you will install useful homebrew applications to complete your setup"))
    guide3dsfinalsetup()


# Function for the finalize setup section of the guide
def guide3dsfinalsetup():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("Required Reading")
    print("In the previous section")

guidedisclaimer()