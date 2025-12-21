class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        srednia=sum(self.marks)/len(self.marks)
        return srednia >50
student1=Student("Ania", [50,60,70])
student2=Student("Marek",[30,40,20])

print(student1.name,"passed:",student1.is_passed())
print(student2.name,"passed:",student2.is_passed())