# class Mother:
#     def disp(self):
#         print("I am Mother")
#
#
# class Father:
#     def disp(self):
#         print("I am Father")
#
# class Child(Mother,Father):
#         pass
#             #print("I am Child")
#
# #print(Child.mro())
# c=Child()
# c.disp()

s="deepali rane deepali"
l=s.split(" ")
print(l)
s1=s[0].upper()+s[1:]
print(s1)
# for i in l:
#     if l.count(i)>1:
#         continue
#     else:
#         print(i)

s=['1236','456','1789','345']
l=[int(i) for i in s]
n=len(l)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
print(map(lambda x:sorted(l),l))


# l=['a','b','b','c','c']
# d={}
# for char in l:
#    d[char]=l.count(char)
# print(d)