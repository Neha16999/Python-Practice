a=10

def some():
    a=9
    print("in",a)
    x=globals()['a']
    print(x)

print("out",a)    
some()