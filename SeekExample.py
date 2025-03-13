import os
os.chdir(r"C:\Users\CDAC\Desktop\PGDAI Feb 2025\Sample codes")
f=open("Test.txt","rb")
print(f.read(10))
print("Current Location :" ,f.tell())
f.seek(-10,2)
print("Current Location : ",f.tell())
print(f.read().decode("utf-8"))
f.close()

#seek(offset[,reference_point])
#seek(0): move the pointer at the begining of file
#tell(): present location of pointer

#0 - from the begining
#1 - from the current loaction
#2 - set the reference point to the nth position to the left form the end.
     # it works only in binary mode
