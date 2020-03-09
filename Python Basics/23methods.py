class Student:

    School="HarvardX"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3    

    @classmethod
    def getSchool(cls):         #here cls is used as it is class method and works with class vars
        return cls.School

    @staticmethod
    def info():
        print("This is student class in the abc module")

s1=Student(89,95,67)
s2=Student(84,78,96)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()