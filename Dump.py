import pickle
list1=[1," Abhishek","M",28]
f = open("mybinary.dat","wb")
pickle.dump(list1,f)
f.close()
