class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1 
        m2=self.m2+other.m2 
        s3=Student(m1,m2)
        return s3

    def __gt__(self, value):
        r1=self.m1+value.m1
        r2=self.m2+value.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)    


s1=Student(78,89) 
s2=Student(98,76)         

s3=s1+s2            #Student.__add__(s1,s2)

print(s3.m1)
print(s3.m2)

if s1>s2 :
    print("S1 wins")
else:
    print("S2 Wins ")

a=9
print(a)
print(a.__str__())  #behind the scene this __str__() is called when we simply say print(a)

print(s1)           #Here we are calling the __str__() and we are overiding it by defining it in our class
print(s2)