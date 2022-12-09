'''
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method.
It uses the next() method for iteration.

__iter(iterable)__ method that is called for the initialization of an iterator.
This returns an iterator object

next ( __next__ in Python 3) The next method returns the next value for the iterable.
When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object which further uses next() method to iterate over.
This method raises a StopIteration to signal the end of the iteration.
'''

li=[1,2,3,4,5]
x=iter(li)
while True:
    try:
        print(x.__next__())
    except:
        break