class A:
    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")    

class B(A):             #class B inherits A
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")    

class C(B):             #multilevel inheritance  
    def feature5(self):
        print("feature 5")

    def feature6(self):
        print("feature 6")    

b1=B()
b1.feature3()

c1=C()
c1.feature1()

