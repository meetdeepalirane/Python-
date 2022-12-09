import json
class Student:
    class_count=0             #class variable
    def __init__(self,name):
        self.name=name      #instance variable
        Student.class_count=Student.class_count+1
        self.roll_number=Student.class_count

    def display(self):
        print(f"Name is {self.name} and Roll Number is {self.roll_number}")
        Student.Total_Count()
    @classmethod
    def Total_Count(cls):
        print(f"Total class count is {Student.class_count}")

final_json_str=[]
for i in range(3):
    obj=Student(input("Enter Name"))
    #obj.display()
    json_str=json.dumps(obj.__dict__)
    final_json_str.append(json_str)
print(final_json_str)

with open("C:/Users/admin/OneDrive\Desktop/test_json.txt",'w') as fw:
    json.dump(final_json_str,fw)

with open("C:/Users/admin/OneDrive\Desktop/test_json.txt",'r') as fr:
    data=json.load(fr)
    print(data)