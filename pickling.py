import pickle
lii=[1,2,3,4,5,6, 7,8]
with open("C:/Users/admin/OneDrive\Desktop/test_pickle.txt",'wb') as fw:
    pickle.dump(lii,fw)

with open("C:/Users/admin/OneDrive\Desktop/test_pickle.txt",'rb') as fr:
    data=pickle.load(fr)
    print(data)

import pickle

d={'a':100,'b':200,'c':300}
pickled_on=pickle.dumps(d)
print(pickled_on)

pickled_off=pickle.loads(pickled_on)
print(pickled_off)