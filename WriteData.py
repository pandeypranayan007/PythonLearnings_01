import os
os.chdir(r"C:\Users\CDAC\Desktop\PGDAI Feb 2025\Sample codes")
f=open("practice.txt","a+")
while True:
    data= input("Enter data to save in the text file :")
    f.write(data)
    ans =input("Do you want to enter more data? (yes/no) : ")
    if ans=='no':
        break
print("\nReading Data from file...")
f.seek(0)
print(f.read())
f.close()
