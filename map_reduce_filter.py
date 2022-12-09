'''lambda function----- are anonymous function means that the function is without a name.
This function can have any number of arguments but only one expression, which is evaluated and returned.

Filter()----- The filter() function in Python takes in a function and a list as arguments.
This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.'''

li=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,li )))


ages=[21,45,32,43,19,9]
#find all the people who r eligible for voting.
list(filter(lambda x:print(x,"Eligible") if x>=18 else print(x,"NOt Eligible"),ages))

''' The map() function in Python takes in a function and a list as an argument. 
The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item'''

num=[2,3,4,5,6]
print(list(map(lambda x:x*x*x,num)))


''' The reduce() function in Python takes in a function and a list as an argument. 
The function is called with a lambda function and an iterable and a new reduced result is returned.
 This performs a repetitive operation over the pairs of the iterable. 
The reduce() function belongs to the  functools module.'''

#sumof list

import functools
print(functools.reduce(lambda x,y:x+y,num),)