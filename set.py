s={2,3,4,5,7}
z={2,3,8,9}
s.add(9)
print(s)


#copy
s1=s.copy()
s1.add(10)
print("copied set",s1)
print("original set",s)


#differnce
print(s.difference(z))
print(s.difference_update(z))