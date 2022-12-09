'''
you can change class variable like classname.class_variable_name then it will reflect in all objects
if you change class variable value with object like  s1.class_variable it ll refect
for that instance only
'''

class Student:
    college_name="IIT Mumbai"   #class variable
    student_count=0

    def __init__(self,name):
        self.stud_class="FE"    #instance variable
        self.name=name
        self.id=Student.student_count+1
        Student.student_count+=1
    def disp(self):
        print("name of student is", self.name)
        print("College Name is",self.college_name)
        print("class is",self.stud_class)
        print("Student id is:",self.id)
    @classmethod
    def class_count(cls):
       print("Class count is:",Student.student_count)



s1=Student("Deepali")
s2=Student("rohit")

#changing class_variabel using object
s2.college_name="MIT,Delhi"
s3=Student("RUd")   #NIIT wont reflect here bcoz obj.collge_name
s3.disp()
s2.disp()
#s1.disp()

print("changing clg name by class name")
Student.college_name="ZZZZZZZZ"
s2.disp()
s3.disp()

'''
s=Student("Deep")
s.disp()

s1=Student("Rohu")
s1.disp()

s2=Student("Ruds")
s2.disp()
Student.class_count()
'''