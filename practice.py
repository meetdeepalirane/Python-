# import  functools
# print(functools.reduce(lambda x,y:x+y, (i for i in range(1,10))))
#
# result=lambda x:x*x
# print(result(5))
#
#
# phrase="An Idiot"
# vowel_count=0
# consonant_count=0
# for i in phrase:
#     if i.lower() in ['a','e','i','o','u']:
#         vowel_count+=1
#     else:
#         consonant_count+=1
# print("Vowels: ",vowel_count)
# print("Consonant: ",consonant_count)
#
# phrase="  An   Idiot   "
# li=phrase.split(" ")
# print(li)
# print(list(filter(str.strip, li)))
#
# a=3
# b=1
# c=0
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# else:
#     print(c)

# test_dict = {'gfg': [7, 6, 3],
#              'is': [2, 10, 3],
#              'best': [19, 4]}
# # res={}
#
# # for ele in sorted(test_dict):
# #     res[ele]=sorted(test_dict[ele])
# # print(res)
#
# print({ele:sorted(test_dict[ele])for ele in test_dict})

# inp1 = "listen"
# inp2 = "silent"
#
# l1=list(inp1)
# l1.sort()
# l2=list(inp2)
# l2.sort()
# if l1==l2:
#     print("Anagram")
# else:
#     print("Not")


#
# def evenodd_seggregate(arr):
#         left,right=0,len(arr)-1
#         while left<right:
#             while arr[left]%2==0 and left<right:
#                 left=left+1
#             while arr[right]%2!=0 and left<right:
#                 right=right-1
#             if arr[left]<arr[right]:
#                 arr[left],arr[right]=arr[right],arr[left]
#                 right=right-1
#                 left=left+1
#             return arr
# li=[2,5,6,9,11,12]
# print(evenodd_seggregate(li))
#
# li=[2,5,2,6,9,11,12,2]
# x=2
# if x in li:
#     print(f"count of {x} is {li.count(x)}")
#
l1=[12,34,56,71]
result=[]
for each in l1:
    sum=0
    for i in str(each):
        sum=sum+int(i)
    result.append(sum)
print(result)

#
# l1=[12,34,56,71]
# for i in range(0,len(l1)-1):
#     print(l1[i]+l1[i+1])

# def reversee(num):
#     remainder=0
#     while num>0:
#         digit=num%10
#         remainder=remainder*10+digit
#         num=num//10
# #     return remainder
#
# num=345
# print(reversee(num))