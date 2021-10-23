#!/env/Python3.8.10
#Super basic and kinda trash windows 95 retail product key check by MobCat
#Based on info from stacksmashing's video

#I moved a lot of the fluf comments to the ReadMe.md
#so read that for a hole ted talk on how this all works.

def EnterKey():
    while True:
        try:
            print ("Product Identification")
            print ("""
Please enter your 10 digit windows 95 CD Key in the space below.
You will find this number on the yellow sticker on the back of your CD case.
Then press enter to continue.
Please note you must enter all the - in the Product key aswell""")
            keyin = input("CD Key: ")
        
            #Check key for length and type (OEM key or retail key).
            #My code differs a little from MS as I am sorta checking for the -
            #But also not realy yol-1111111 and yolo1111111 are both valid
            if len(keyin) == 11:
                #print("Retail key")
                RetailKey(keyin)
                break
            #TODO: Check if the - between RetailKey-NotCheck is checked.
            #eg. 19996-OEM-7215850f12345
            # or 19996-OEM-721585012345
            elif len(keyin) == 23:
                if "-OEM-" in  keyin:
                    #print ("OEM KEY")
                    OEMKey(keyin)
                    break
                else:    
                    print("\nError: Invalid OEM key\n")
            else:
                print ("\nError: Invalid key length\n")
                
        except KeyboardInterrupt:
            print("\nProgramme Was Interrupted!")
            print("Goodbye ^__^/")
            exit()

def RetailKey(keyin):
    #Unpack key into individual numbers to sum
    digi1, digi2, digi3, digi4, digi5, digi6, digi7, digi8, digi9, digi10, digi11 = keyin
    
    #Check the first 3 numbers for obvious fakes / blacklisted.
    #Missing 111 and 222 for some reason.
    try:
        checkFirst = int(digi1+digi2+digi3)
        if checkFirst in (333, 444, 555, 666, 777, 888, 999):
            print("\nError: Invalid key prefix\n")
            EnterKey()
    except ValueError:
        print("")
        
    
    #as we enterd a string, convert it to a int to we can math it.
    digi5  = int(digi5)
    digi6  = int(digi6)
    digi7  = int(digi7)
    digi8  = int(digi8)
    digi9  = int(digi9)
    digi10 = int(digi10)
    digi11 = int(digi11)
    
    #Sum the number together
    keyin    = digi5+digi6+digi7+digi8+digi9+digi10+digi11
    #devide the sum by the char length. as we can only enter 7 then its just 7.
    keyweight  = keyin/7
    keycheck = keyin%7
    
    print (f"key weight: {keyweight}\n")
    
    #if the modulo opt of keycheck returns a whole number, no remainders then its a legit key.
    if keycheck == 0:
        installer("0")
    else:
        print ("\nError: Invalid key.\n")
        EnterKey()
        
def OEMKey(keyin):
    #Unpack the key into veribiles.
    #Yes, this looks and is retrated.
    digi1, digi2, digi3, digi4, digi5, digi6, digi7, digi8, digi9, digi10, digi11, digi12, digi13, digi14, digi15, digi16, digi17, digi18, digi19, digi20, digi21, digi22, digi23 = keyin
    #1     9      9      9      6      -      O      E      M      -       0       3       1       3       9       8       4       -       1       2       3       4       5
    
    #date check
    checkday  = int(digi1+digi2+digi3)
    checkyear = int(digi4+digi5)
    #print (f"DDD = {checkday} YY = {checkyear}")
    dayrange  = range(1, 367)
    yearlist  = [95, 96, 97, 98, 99, 0, 1, 2]
    
    #Crappy date check. Should be done with one function but its bugging out.
    if not checkday in dayrange:
        print("\nError: Fail date check, out of range day")
        EnterKey()
        
    if not checkyear in yearlist:
        print("\nError: Fail date check, out of range year\n")
        EnterKey()
        
    #Mod7 check on the 3rd bank of the key
    digi11 = int(digi11)
    digi12 = int(digi12)
    digi13 = int(digi13)
    digi14 = int(digi14)
    digi15 = int(digi15)
    digi16 = int(digi16)
    digi17 = int(digi17)
    
    #Leading 0 check
    if not digi11 == 0 or digi18 != '-':
        print("\nKey formatting error: No Leading zero or missing the 3rd -\n")
        EnterKey()
    
    sum7 = digi11+digi12+digi13+digi14+digi15+digi16+digi17
    
    if sum7 == 0000000:
        print("Error: OEM Key can not be all 0's, sadly.")
    
    keyweight = sum7/7
    mod7    = sum7%7
    
    #check if the last random part of the key is numbers and not letters
    try:
        checkint = int(digi19+digi20+digi21+digi22+digi23)
    except ValueError:
        print("\nError: Product key must be a number.\n")
        EnterKey()
    
    print (f"Keyweight: {keyweight}\n")
    
    if mod7 == 0:
        installer("1")
    else:
        print ("\nError: Invalid key.\n")
        EnterKey()

def installer(type):
    if type == "0":
        print("Retail Product key is valid, Continuing to install product")
        #Now only install retail things.
        exit()
        
    if type == "1":
        print("OEM Product key is valid, Installing OEM packadges now")
        #So you would install like normal
        #but when you come across a OEM packadge like wallpapers and such
        #check if you passed the OEM key, if so install OEM wallpapers.
        exit()
    

#SCRIPT STARTS HERE
EnterKey()