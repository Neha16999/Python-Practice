class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is", self.cpu,self.ram)

comp1=Computer('i5',16)            #object creation
comp2=Computer("Ryzen3",8)          # at the place of self comp2 goes


comp1.config()
comp2.config()