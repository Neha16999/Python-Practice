class Computer:
    
    def __init__(self):
        self.name="Krishna"
        self.age=16

    def update(self):
        self.age=20

    def compare(self,other):  #comapairing objects
        if self.age==other.age:
            return True
        else:
            return False            



c1=Computer()       #here Computer() is Constructor and c1 , c2 are objects
c1.update()
c2=Computer()


if c1.compare(c2):          #c1 becomes self and c2 becomes other
    print("They are Same")
else:
    print("They are different")    


print(c1.name)
print(c2.name)