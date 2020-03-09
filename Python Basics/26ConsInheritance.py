class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")    

class B():             #class B inherits A
    
    def __init__(self):
        super().__init__()      #calls init of super class
        print("In B init")
 
    def feature1(self):
        print("feature 3")

    def feature4(self):
        print("feature 4") 

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C init")

    def feat(self):
        super().feature2()     #super calling super class method

b=C()        
b.feat()