# li=[1,12,10,4,25,6]
# print(list(filter(lambda x:x%2==1,li)))
#
# #sort list
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]<li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)
#
#
# #reverse list
# n=len(li)
# for i in range(int(n/2)):
#     li[i],li[n-i-1]=li[n-i-1],li[i]
# print(li)

def find_second_max(li):
    for i in range(2):
        res=[]
        max = li[0]
        for i in range(len(li)-1):
            for j in range(i+1,len(li)):
                if li[i]>li[j]:
                    max = li[i]
                    print("Found",max)
                    res.append(max)
                    li.remove(max)
        print(res)





l=[3,21,20,8,11,4]
find_second_max(l)
