from tkinter import * 

root = Tk()     #creating instance root which is the obj of class Tk in the module tkinter

#creating a label widget 
myLabel= Label (root, text="Hello World")

#showing it on screen
myLabel.pack()  


root.mainloop()
