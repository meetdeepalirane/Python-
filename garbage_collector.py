'''
Destructors are called when an object gets destroyed.
In Python, destructors are not needed as much as in C++ because Python has a garbage collector
that handles memory management automatically.
The __del__() method is a known as a destructor method in Python.
It is called when all references to the object have been deleted i.e when an object is garbage collected.
'''

class Test:
    def __init__(self):
        self.A=10
        self.B=20
        print(f"Constructor called: A={self.A} and B={self.B}")
    def __del__(self):
        print('Destructor called, Employee deleted.')
    def disp(self):
        print("Hello")
def newfunc(var):
    var=100


v1=Test()
newfunc(v1)
print(v1.A,v1.B)






