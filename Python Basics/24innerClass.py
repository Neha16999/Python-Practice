class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()      #creating the object of inner class inside outer class

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="Dell"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.cpu, self.brand, self.cpu)    



s1=Student("Ram",2)
s2=Student("Krishna",5)

lap1=s1.lap         #this uses inner class __init__() to create the object
lap2=s2.lap


lap3=Student.Laptop()       #creating object of inner class outside the outer class

s1.show()
s2.show()
lap3.show()   #calling show of laptop