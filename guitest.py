from tkinter import *

root = Tk()
def changeText(v):
    v.set("no")
    return v

def changeV():
    changeText(v)

topFrame = Frame(root)
v = StringVar()
Label(root, textvariable = v, bg= "black", fg = "red").pack()
v.set("one")
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text= "Button 1", fg = "red", command=changeV)

button1.pack()

root.mainloop()