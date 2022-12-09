# li=[0,1,2,3]
# #print(li[-1]) - is index 3
#
# for li[-1] in li: # retrieve 1 value in each iteration and store at li[-1] i.e. li[3]
#     print(li[-1],end="")

 #explaination
#retrieve 1 value in each iteration and store at li[-1] i.e. li[3]

#1st iteration
#li[-1] = li[3] = 0
#li is now =[0,1,2,0]

#2nd iteration
#li[-1] = li[3] = 1
# li is now =[0,1,2,1]

# 3rd iteration
# li[-1] = li[3] = 2
# li is now =[0,1,2,2]

# 4th iteration - last
# li[-1] = li[3] = 2
# li is now =[0,1,2,2]
# a=10
# b=20
# def add():
#     global a
#     a=5
#     b=6
#     print(f"addition inside function is {a+b}")
#
# add()
# print(f"addition outside function is {a + b}")


# mails=['deepali@gmail.com',"rohit@hotmail.com","rudransh@gmail.com"]
# email_list=[id.split("@")[1] for id in mails]
# count_mails={i:email_list.count(i) for i in email_list}
# print(count_mails)

# def chk_largest(l,n):
#     final_li=[]
#     for i in range(n):
#         max = 0
#         for j in range(len(l)):
#             if l[j]>max:
#                 max=l[j]
#         final_li.append(max)
#         l.remove(j)
#     return final_li
# li=[1,2,3,4,5,4,8,9,7,2]
# print(chk_largest(li,3))
# li=[11,6,7,12,4,23,55]
# for i in range(0,len(li)):
#     for j in range(i,len(li)):
#         if li[i]<li[j]:
#            li[i],li[j]= li[j],li[i]
# print(li)

# li=[11,6,7,12,4,23,55]
# x=(lambda x:True if x in li else False)
# print(x(13))

# l = lambda _: True
#
# print(l(0))

# li=[11,6,7,12,4,23,55]
# min=li[0]
# for i in range(1,len(li)):
#     if li[i]<min:
#         min=li[i]
# print(min)
#
# st="Deepali Rane Rohit Ghorpade"
# reversed_str=""
# l_st=st.split()
# for i in l_st[::-1]:
#     reversed_str=reversed_str+i+" "
# print(reversed_str)
#

# st="Deepali"
# char_to_replace=input("Enter character")
# st1=st.replace(char_to_replace,'')
# print(st1)

# st="Deepali Rane Rohit Ghorpade"
# li=st.split()
# for i in li:
#     if len(i)%2==0:
#         print(i)+
# import functools
# s=(1,2,3,4,5)
# print(functools.reduce(lambda x,y:x+y,s))
#
# l=[1,2,3,3.3,4.5]
# print([i for i in l if type(i)!= float])
#
# #Find all of the numbers from 1-1000 that are divisible by 7
# print([i for i in range(1,1001) if i%7==0])

# Count the number of spaces in a string
#s=" Deepali Dattatray Rane "
#counter=0
# for i in s:
#     if i.isspace():
#         counter=counter+1
#     else:
#         pass
# print(counter)
#print(len([counter for i in s if i.isspace()]))

# #Create a list of all the consonants in the string .
# s="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# new_str=""
# for each in s:
#     if each in ['a','e','i','o','u']:
#         pass
#     else:
#         new_str=new_str+each
# print(new_str)

# #Get the index and the value as a tuple for items in the list.Result would look like (index, value), (index, value)
# l=["hi", 4, 8.99, 'apple', ('t','b','n')]
# for index,val in enumerate(l):
#     print((index,val))
#
#
# #Find the common numbers in two lists (without using a tuple or set)
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# print([i for i in list_a if i in list_b])
#
# #Get only the numbers in a sentence like
# s="In 1984 there were 13 instances of a protest with over 1000 people attending"
# print(len([i for i in s if i.isnumeric()]))

#print(['even' if i%2==0 else 'Odd' for i in  range(20)])

# Produce a list of tuples consisting of only the matching numbers in these lists
# list_a =[ 1, 2, 3,4,5,6,7,8,9]
# list_b = [2, 7, 1, 12] #Result would look like (4,4), (12,12)
# print([(a,b) for a in list_a for b in list_b if a==b])

# s=" Deepali Rudransh Ro Rane "
# for i in s.split(" "):
#     print(i,len(i))

#Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
#print([i for i in range(1,100) if True in [True for j in range(2,10) if i%j==0]])

