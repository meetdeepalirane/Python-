li=[11,6,-7,-12,4,-23,55]
from collections import OrderedDict
'''
1.Python program to add two numbers
num1,num2=10,15
print(f"Addition of{num1} and {num2} is:",num1+num2)


2.Maximum of two numbers in Python
x,y=10,12
z=lambda x,y:print("x is greater") if x>y else ("y is greater")
print(z(x,y))





4. Python program to print all Prime numbers in an Interval
def prime_numbers():
    for num in range(1,10):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
                else:
                    print(num)
prime_numbers()


5.Python program to check whether a number is Prime or not
import functools
def check_for_prime(num):
    for i in range(2,num):
        if num%i==0:
            break
        else:
            print(f"{num} is prime number")
check_for_prime(5)




4.Program to print ASCII Value of a character
ch="A"
print(f"AsCII value of {ch} is",ord(ch))


5.Python Program for Sum of squares of first n natural numbers
print(sum([i *i for i in range(1,5)]))
print(sum([i*i*i for i in range(1,6)]))


6. Python Program to find sum of array
def sum_array(a):
    sum=0
    for element in a:
        sum=sum+element
    return sum

array_to_search=[1,3,5,7]
ans=sum_array(array_to_search)
print(ans)
Python Program to find largest element in an array
array_to_search=[1,13,5,7]
print(max(array_to_search))


7.Python Program for array rotation
array_to_search=[1,13,5,7]
print([i for i in array_to_search[::-1]])
def split_arr(a,lenn,position):
    b=a[:position]
    print(a[position:]+b[:])

array_to_search = [12, 10, 5, 6, 52, 36]
n=len(array_to_search)
position=2
split_arr(array_to_search,n,position)


8.Python program to interchange first and last elements in a list

li= [12, 10, 5, 6, 52, 36]
temp=li[0]
li[0] = li[-1]
li[-1] = temp
print(li)


9.Python program to swap two elements in a list
def swap(li,index_1,index_2):
    temp=li[index_1]
    li[index_1]=li[index_2]
    li[index_2]=temp
    print(li)

li=[2,13,42,44,12]
swap(li,0,2)


10. Python | Ways to check if element exists in list
li=[1,4,6,7,12,23,55]
n=15
if n in li:
    print("Exist in list")
else:
    print("Not exist")


11. Python | Reversing a List
li=[1,4,6,7,12,23,55]
print(list(x for x in li[::-1]))


12.Python program to find sum of elements in list
li=[1,4,6,7,12,23,55]
z=functools.reduce(lambda x,y:x+y,li)
print(z)


13. Python | Multiply all numbers in the list
li=[2,3,4,5,6]
mul=1
for i in li:
    mul=mul*i
print(mul)
li.clear()
print(li)


14. Python program to find smallest number in a list
li=[11,6,7,12,4,23,55]
min=li[0]
for i in li:
    if i<min:
        min=i
print("Minimum is:",min)


15. Python program to find largest number in a list
li=[11,6,7,12,4,23,55]
max=li[0]
for i in li:
    if i>max:
        max=i
print("Maximum is:",max)

16.Python program to find second largest number in a list
li=[11,6,7,12,4,23,55]
li.sort()
print(li[-2])


17. Python program to find N largest elements from a list

li=[11,6,7,12,4,23,55]
n=int(input("How many elements to fetch"))
li.sort()
print(li[-n:])

# OR

def n_largest(li,n):
    final_lis=[]
    for i in range(0,n):
        max=0
        for j in range(len(li)):
            if li[j] > max:
                max=li[j]
        final_lis.append(max)
        li.remove(max)

    print(final_lis)
li=[11,6,7,12,4,23,55]
n=3
n_largest(li,n)


18.Python program to print even numbers in a list

print([x for x in li if x%2==0])


19. Python program to print all even numbers in a range

for i in range(1,20):
    if i%2==0:
        print(i)

20. Python program to print positive numbers in a list
positive=[]
for i in li:
    if i < 0:
        pass
    else:
        positive.append(i)

print(positive)


21. Python | Sum of number digits in List
l=[12, 67, 98, 34]
res=[]
for each in l:
    sum=0
    for dig in str(each):
        sum=sum+int(dig)
    res.append(sum)
print(res)


22. Python | Sum of number digits in List Break a list into chunks of size N in Python
l=[1,2,3,4,5,6]
n=3
x=[l[i:i+n] for i in range(0,len(l),n)]
print(x)


23. Python | Sort the values of first list using second list

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
z=list(zip(y,x))
print(z)
print([x for _, x in sorted(z)])

24. Python – Extract Unique values dictionary values

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
print(set(sorted(([ele for val in test_dict.values() for ele in val]))))

25. Python program to find the sum of all items in a dictionary
d= {"a": 100, "b":200, "c":300}
print(sum({val for val in d.values()}))


26.Python | Ways to remove a key from dictionary
d= {"a": 100, "b":200, "c":300}
del d['a']
print(d)

27. Ways to sort list of dictionaries by values in Python – Using lambda function

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print(sorted(lis, key=lambda i:i["age"]))


28. Python | Merging two Dictionaries
d1= {"a": 100, "b":200, "c":300}
d2= {"d": 400, "e":500, "f":600}
temp=d1.copy()
temp.update(d2)
print(d1,d2,temp)


29. Python – Convert key-values list to flat dictionary 

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print(dict(zip(test_dict['month'],test_dict['name'])))


30.Python – Insertion at the beginning in OrderedDict

inordered_dict=OrderedDict([("a",1),("b",2)])
inordered_dict.update({"c":3})
inordered_dict.move_to_end("c",last=False)
print(inordered_dict)


31. Python – Least Frequent Character in String
str="HiiHelloo"
d={}
for char in str:
    d[char]=str.count(char)
print(d)
print(min({val for val in d.values()}))


32. Python | Maximum frequency character in String 

s="Hiihhhelloo".lower()
print(s)
d={}
for character in s:
        d[character]=s.count(character)
print(d)
print(max({val for val in d.values()}))


#33. Python | Program to check if a string contains any special character
import re
s="#$Deep)ali"
special=re.compile('\\W')
#print(special.search(s))
for each in s:
    if special.search(each) :
        print(each)

34. Remove multiple elements from a list in Python
l=[22,33,44,22,33]
for i in l:
    if l.count(i) > 1:
        l.remove(i)
print(l)

35.Python | Remove empty tuples from a list

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]
for element in tuples:
    if len(element)==0:
       tuples.remove(element)
print(tuples)


36. cumulative sum of elements of list

lis = [10, 20, 30, 40, 50]
for i in range(1,len(lis)):
    lis[i]=lis[i-1]+lis[i]
print(lis)
 or 
 
 lis = [1, 2, 3, 4, 5]
sum=[]
temp=0
for i in range(0,len(lis)):
    temp=temp+lis[i]
    sum.append(temp)
print(sum)


37. Python | Sum of number digits in List

test_list = [12, 67, 98, 34]
for element in test_list:
    sum=0
    for each in str(element):
        sum=sum+int(each)
    print(sum)
    
    
38. json/pickle practice

dict={"a":100,"b":200,"c":300,"d":400}
json_string=json.dumps(dict)
print(json_string,type(json_string))

loaded_json=json.loads(json_string)
print(loaded_json,type(loaded_json))

with open("C:/Users/admin/OneDrive/Desktop/sample.json","w") as fw:
    json.dump(dict,fw)

import json
class Student:
    def __init__(self):
        self.name=input("Enter Name")
        self.branch=input("Enter branch")
    def disp(self):
        print(f"Name is: {self.name}---------Branch is:{self.branch}")

json_data=[]
for iteration in range(1,3):
    s = Student()
    s.disp()
    #json_data.append(json.dumps(s.__dict__))
    json_data.append(s)


with open("C:/Users/admin/OneDrive/Desktop/sample.json","w") as fw:
    json.dump(json.dumps([i.__dict__ for i in json_data]),fw)
    print("Data successfully written to json file")

with open("C:/Users/admin/OneDrive/Desktop/sample.json") as fr:
    data=json.load(fr)
    print(data)



import pickle
class Student:
    def __init__(self):
        self.name=input("Enter Name")
        self.branch=input("Enter branch")
    def disp(self):
        print(f"Name is: {self.name}---------Branch is:{self.branch}")

s=Student()
pickled_string=pickle.dumps(s)
pickled_object=pickle.loads(pickled_string)
print(type(pickled_object))
pickled_object.disp()
'''
#
# phrase="It is also possible to create it. A function that can take any object, allowing function for polymorphism. In this example, let’s create a function called “func()” which will though in take an object which we will name “obj”. Though we are using the name ‘obj’, any instantiated object will be able to be called into this function."
# phrase=phrase.replace(".","").replace(",","")
# print(phrase)
# split_sentence=phrase.lower().split(" ")
# print(split_sentence)
#
# word_freq={}
# for word in split_sentence:
#     word_freq[word]=split_sentence.count(word)
# print(word_freq)
#


#
# #tuple is immutable but if elements are mutable they can be changed
# t=([1,2,3],["a","b"])
# print(t)
# t[0][1]=100
# print(t)
# t[0]=[4,5,6]
# print(t)


lis = [1, 2, 3, 4, 5]
sum=[]
temp=0
for i in range(0,len(lis)):
    temp=temp+lis[i]
    sum.append(temp)
print(sum)

