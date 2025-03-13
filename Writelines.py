import os
os.chdir(r"C:\Users\CDAC\Desktop\PGDAI Feb 2025\Sample codes")
L1 = ["Hello Everyone\n","writing Multile strings\n","This is the third line"]
f= open("myfile.txt","w+")
f.writelines(L1)
f.seek(0)
print(f.read())
f.close()
