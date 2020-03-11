from  tkinter import *

root= Tk()
e = Entry(root, width= 100, borderwidth= 5 , fg="Black" , bg="white")
e.pack()
e.insert(0,"Your name please")  #puts the text in input box by default 

def myClick():
    hello="Hello "+e.get()
    myLabel=Label(root, text=hello)       #e.get() - gives us text entered
    myLabel.pack()


myButton = Button(root, text="Enter your name", pady= 15, padx=25, command=myClick , fg="blue" , bg="lightgreen" )  #state=DISABLED, to disable the button 
myButton.pack()

root.mainloop()