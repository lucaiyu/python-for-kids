import pickle
map1={'a':'A','b':'B'}
save_file=open('save.dat','wb')
pickle.dump(map1,save_file)
save_file.close()
load_file=open('save.dat','rb')
loaded_map1=pickle.load(load_file)
load_file.close()
print(loaded_map1)
