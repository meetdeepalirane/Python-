'''
 A generator-function is defined like a normal function, but whenever it needs to generate a value,
 it does so with the yield keyword rather than return.
 If the body of a def contains yield, the function automatically becomes a generator function.
'''
#generator
def fib(n):
    p,q=0,1
    while p<n:
        yield p
        p,q=q,p+q

x=fib(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

#for i in x:
 #   print(i)



