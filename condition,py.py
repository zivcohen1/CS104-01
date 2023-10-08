#CS104
#Ziv Cohen
#conditions.py
temp=0
while temp!=999:
    temp=int(input("Please enter the current temperature (type '999' to end the program): "))
    if temp>90:
        print("Wear Shorts")
    elif temp>70:
        print("Short sleeves are fine")
    elif temp>50:
        print("Wear a jacket")
    elif temp>32:
        print("Wear a heavy coat") 
    else:
        print("stay inside")
print("End of program thank you")
