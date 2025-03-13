import os
os.chdir(r"C:\Users\CDAC\Desktop\PGDAI Feb 2025\Sample codes")
#f=open("Test.txt","r")
#print(f.read())
#f.close()


#f=open("Test.txt","r")
#for line in f:
    #print(line,end="")
#f.close()



#f=open("Test.txt","r")
#print(f.read(10))
#print(f.read(10))
#print(f.read())
#f.close()


f=open("Test.txt","r")
L1 = f.readlines()
for line in L1:
    #s=line.split()
    s=line.splitlines()
    print(s)

f.close()
























