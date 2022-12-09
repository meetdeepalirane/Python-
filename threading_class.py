from threading import Thread

class Test(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        phy,chem,math=56,76,98
        avg=phy+chem+math/3
        print(f"Avg is{avg}")
t=Test("Deepali")
t.start()


class student:
    class_count = 0
    def generate_roll(self):
        self.roll=student.class_count+1
        print("Roll Number is:",self.roll)
        student.class_count+=1
    @classmethod
    def class_count_check(cls):
        print("Class strength is:", student.class_count)
s=student()

t1=Thread(target=s.generate_roll())
t2=Thread(target=student.class_count_check())
t1.start()
t2.start()


class Shape(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name=input("Entr name of patient")
        self.pid=input("ENter patient ID")
        self.address=input("Enetr address of patient")
    def run(self):
        self.symptoms = input("Enetr symptoms").split(",")
        print(f"Name is {self.name}")
        print(f"Patient ID is {self.pid}")
        print(f"Patient address is {self.address}")
        print(f"patient symptoms are {self.symptoms}")

s=Shape()
s.start()


