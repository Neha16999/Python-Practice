def person(name,age):
    print(name)
    print(age)

person(age=5,name="lala")     #here position agrs are used even if the position gets changed it will work

def person1(name,age=18):       #takes default age=18
    print(name)
    print(age)

person1("krishna",15)     #15 will override 18     

#variable length
def sum(a,*b):

    c=a

    for i in b:
        c=c+i
    print(c)

sum(1,3,4,5)

#keyworded variable length args
def person2(name, **data):
    print(name)
    print(data)

person2("Kanha", city="Gokul", love= "Radha")    