# def sortdecorator(func):
#     def inner(lisst):
#         print("*******"*3)
#         new_dict={lisst[i]:lisst[i+1] for i in range(0,len(lisst),2)}
#         print(f"Converted dict is:{new_dict}")
#         sorted_dict = sorted(new_dict.items(), key=lambda x: x[1])
#         print(sorted_dict)
#         print("*******"*3)
#
#     return inner
#
# @sortdecorator
# def convert_li_to_dict(l):
#     pass
#
# l = [19, 41, 25, 8, 4,11]
# convert_li_to_dict(l)
#
#
# #
# # li=[15,4,12,52,32,9]
# # print(sorted(li))
# # print(sorted(sorted(li),key=lambda i:i%2==0,reverse=True ))
#
# def squaredecorator(func):
#     def wrapper(x,y):
#         return func(x**2,y**2)
#     return wrapper
#
# @squaredecorator
# def add(a,b):
#     c=a+b
#     return c
#
# print(add(5,6))
#
#
# def country_code_decorator(func):
#     def wrapper(li):
#         lii=list(map(lambda x:'+91-'+str(x),li))
#         return func(lii)
#     return wrapper
#
# @country_code_decorator
# def add_countrycode(l):
#     print(l)
#
#
# mobile=[9762760899,9762417667,9421172421]
# add_countrycode(mobile)

def key_value_decorator(funcc):
    def wrapper(d):
        l1=[]
        for key in d.keys():
            l1.append(key)
        for val in d.values():
            l1.append(val)
        return funcc(l1)
    return wrapper

@key_value_decorator
def funcc(di):
    print("Dictionary is:",di)


di={1:"ABC",2:"CDR",3:"wer"}
funcc(di)