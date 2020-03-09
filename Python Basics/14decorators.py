def div(a,b):
    print( a/b)

def smart(func):        #decorator
    def change(a,b):
        if(a<b):
            a,b =b,a
        return func(a,b) 

    return change   


div1=smart(div)

div1(8,808)