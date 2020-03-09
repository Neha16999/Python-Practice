def topten():
    yield 1
    yield 2
    yield 3
    yield 4

def topsquare():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1


values=topten()
valuessq=topsquare()

print(values.__next__())
print(values.__next__())


for i in values:
    print(i)

print("Squares")


for ii in valuessq:
    print(ii)
