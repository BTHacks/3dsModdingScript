
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
    print("This script will now download all needed files for the guide. All sources can be found on the script github")

guidedisclaimer()