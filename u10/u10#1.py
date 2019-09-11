import pickle
list1=['1','2']
save_file=open('save2.dat','wb')
pickle.dump(list1,save_file)
save_file.close()
load_file=open('save2.dat','rb')
loaded_list1=pickle.load(load_file)
load_file.close
print(loaded_list1)