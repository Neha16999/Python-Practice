class Car:

    wheels=4            #wheels is a class (static) var

    def __init__(self):
        self.mil=10         #mil and comp are instance variables
        self.comp="BMW"

c1=Car()
c2=Car()

c1.mil=8        #To change the val of instance var, we need objname.varname

Car.wheels=6       #to change the value of class var that is static var , we need classname.varname

print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)