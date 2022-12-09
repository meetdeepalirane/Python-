from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, idd):
        self.name = name
        self.idd = idd

    def get_address(self):
        self.adress = input("Enter address")
        assert self.adress != "", "No address entered"     #assert expects condition is true if false assertion error
        print(f"Address is:{self.adress}")

    @abstractmethod
    def display(self):
        pass


class Engineer(Person):
    def __init__(self,name,idd,class_name,stream):
        Person.__init__(self,name,idd)
        self.class_name=class_name
        self.stream=stream
    def display(self):
        Person.get_address(self)
        print(f"Name is:{self.name}-----ID id:{self.idd}--------")
        print(f"Class is:{self.class_name}-------Stream is:{self.stream}")
E_obj=Engineer("Deepali", 21,"BE","IT")
E_obj.display()



class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def disp(self):
        print(f" A is:{self.a}------ B is:{self.b}")
class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
    def disp(self):
        A.disp(self)
        print(f"C is:{self.c}------ D is:{self.d}")
obj=B(1,2,3,4)
obj.disp()


