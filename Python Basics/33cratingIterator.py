#creating own iterator

class TopTen:
    def __init__(self):
        self.num=1          #counter var

    def __iter__(self):         #gives iterator
        return self

    def __next__(self):         #gives next object

        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration         #raises exception which will be handelled by for loop
            


values=TopTen()

for i in values:
    print(i) 

        
       
        
