from  tkinter import *

root= Tk()

def myClick():
    myLabel=Label(root, text= "You Clicked Button")
    myLabel.pack()


myButton = Button(root, text="Click me", pady= 15, padx=25, command=myClick , fg="blue" , bg="green" )  #state=DISABLED, to disable the button 
myButton.pack()

root.mainloop()