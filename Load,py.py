import pickle
f=open("mybinary.dat","rb")
s=pickle.load(f)
f.close()
print(s)
