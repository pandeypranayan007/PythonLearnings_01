import os
os.chdir(r"C:\Users\CDAC\Desktop\PGDAI Feb 2025\Sample codes")
#f=open("Test1.txt","w")
#f.write("This is first line.\nwe are using write() function.")
#f.close()

#mode"x"

#f=open("Test2.txt","x")
#f.write("This is first line.\nwe are using write() function.")
#f.close()

#mode "a" => append mode
f=open("Test.txt","a+")
f.write("\nThis is first line.\nwe are using write() function.")
f.seek(0)
print(f.read())
f.close()
