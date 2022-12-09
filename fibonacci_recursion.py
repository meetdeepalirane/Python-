def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


num=10
for i in range(0,num):
    print(fibonacci(i))



def fib(limit):
    p,q=0,1
    while p<limit:
        yield p
        p,q=q,p+q
x=fib(10)
for i in x:
    print(i)



def fib(n):
    a,b=0,1
    print(a)
    while b<n:
        a,b=b,a+b
        print(b)
fib(10)
