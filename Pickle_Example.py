import pickle
print("Working with Binary Files: ")
bfile = open("empfile.dat","ab")
recno=1
print("Enter records of employee: ")
print()
#take data from user and dumping it in the file as list objects

while True:
    print("Record No.: ",recno)
    eno=int(input("\tEmployee number : "))
    ename=input("\tEmployee name : ")
    ebasic=int(input("\tBasic Salary : "))
    allow=int(input("\tAllowances : "))
    totsal=ebasic+allow
    print("\tTotal Salary: ",totsal)
    edata=[eno,ename,ebasic,allow,totsal]
    pickle.dump(edata,bfile)
    ans=input("Do you wish to enter more records (y/n)? ")
    recno=recno+1
    if ans.lower()=='n':
        print("Record entry over ")
        print()
        break
#retrieve the size of file
print("Size of binary file (in bytes) :",bfile.tell())
bfile.close()

#Reading the employee records from the file using load()

print("Now reading the employee records from the file: ")
print()
readrec=1
try:
    with open("empfile.dat","rb") as bfile:
        while True:
            edata=pickle.load(bfile)
            print("Record No. : ",readrec)
            print(edata)
            readrec=readrec+1
except EOFError:
    pass
bfile.close()
    
        









          









      
    
    
