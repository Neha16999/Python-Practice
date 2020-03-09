#polymorphism
class Vscode:
    def execute(self):
        print("Compiling")
        print("Running")

class MyIde:
    def execute(self):
        print("Spell Checking")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute() 

ide1=Vscode()       #if it has method execute it will work   
ide2=MyIde()
lap1=Laptop() 
lap2=Laptop()
lap1.code(ide1)       
lap2.code(ide2)