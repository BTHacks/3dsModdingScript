# Imports a URL request library to download files
import urllib.request
# Usage: urllib.request.urlretrieve("URL", "filename.fileextension")
# Imports OS library for directory creation
import os

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
        elif answer == 1:
            print("Continuing with New 3ds guide")
            guide3dsnew()
            activeinput = int(0)
        else:
            print("Invalid input, try again.")

# Functon for the "Old 3ds" section of the guide
def guide3dsold():
    loopvar = int(50)
    while loopvar >= 1:
        print("")
        loopvar = loopvar - 1
    print("We will now install CFW on your system using the MSET9 method")
    print("Any required files will be downloaded to C:\ConsoleHackingScript")
    try:
        os.makedirs("C:/ConsoleHackingScript/ ")
    except FileExistsError:
        pass
    urllib.request.urlretrieve("https://github.com/hacks-guide/MSET9/releases/download/v2.1/MSET9-v2.1.zip", "C:\ConsoleHackingScript\MSET9-v2.1.zip")
    print("")
    print("Section I: Prep work")
    answer = str(input("Step 1: Insert your SD card into your computer"))
    answer = str(input("Step 2: Copy all files from MSET9.zip to the root of your SD card. If any files already exist, override them."))
    answer = str(input("Step 3: Run the MSET9 script (MSET9-windows.bat)"))
    answer = str(input("Step 4: Input the number correspoding with your model of 3ds"))
    answer = str(input("Step 5: Type 1 to begin the process of creating your MSET9 ID1"))
    answer = str(input("Step 6: After reviewing the disclaimer, type 1 and hit enter to begin the process"))
    print("Step 7: If you see the message Created Hacked ID1, press Enter to close the MSET9 script")
    answer = str(input("Note: Your console will appear to lose most data / no user-installed apps on HOME Menu. This is expected. Your data will come back at a later step"))
    answer = str(input("Step 8: Reinsert your SD card and power on your console"))

guidedisclaimer()