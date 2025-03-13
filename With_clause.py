import os
os.chdir(r"C:\Users\CDAC\Desktop\PGDAI Feb 2025\Sample codes")

#f=open("Test.txt","r")
#print(f.read())
#f.close()


#by using with clause
#with open("Test.txt","r") as f:
    #print(f.read())




#by using try-except-finally blocks

try:
    #Main code
    f=open("Test.txt","r")
    print(f.read())

except:
    #code to handle erro occuring in try block
    pass

finally:
    #code that will always be executed irrespective of errors
    f.close()
