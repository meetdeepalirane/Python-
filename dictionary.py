#
# def key_val_decorator(func):
#     def inner(d):
#         key_list=list(d.keys())
#         value_list=list(d.values())
#         return key_list,value_list
#     return inner
#
# @key_val_decorator
# def dict_func(di):
#     pass
#
# d={1:"A",2:"B",3:"C",4:"D"}
# dict_func(d)

#from two list creating dict
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
# res={}
# for key in test_keys:
#     for value in test_values:
#         res[key]=value
#         test_values.remove(value)
#         break
# print(res)
#
# #using zip
res=dict(zip(test_keys,test_values))
print(res)

# #using comprehension
# print({test_keys[i]:test_values[i] for i in range(len(test_keys))})
#using map
# print(dict(map(lambda i,j:(i,j),test_keys,test_values)))

#
# def returnSum(d):
#     sum=0
#     for val in d.values():
#         sum=sum+val
#     return sum
#
# dict = {'a': 100, 'b': 200, 'c': 300}
# print("Sum :", returnSum(dict))
# print("Dictionary size:",dict.__sizeof__())
#


# d={1:"A",2:"B",3:"C",4:"D"}
# d1=d.copy()
#
# d1.update({5:"E"})
# print(d)
# print(d1)
# del d
# print(d1)

l=[3,5,7,9,6,3]
d={l[i]:l[i+1] for i in range(0,len(l)-1,2)}
print({(k,v) for (k,v) in d.items()})
sum_key=0
for i in d.items():
    sum_key=sum_key+i[0]
print(sum_key)