def fact(num):
    if num==1:
        return num
    else:
        return num * fact(num-1)

no=5
print(fact(no))




def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num-=1
    return fact
print(factorial(5))
