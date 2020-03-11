from tkinter import * 

root = Tk()     #creating instance root which is the obj of class Tk in the module tkinter

#creating a label widget 
myLabel1= Label (root, text="Hello World")
myLabel2= Label (root, text="Lets Begin")
myLabel3= Label (root, text=" ")

#showing it on screen  
#grid position are relative to eachother
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=3)
myLabel3.grid(row=1, column=4)


root.mainloop()
