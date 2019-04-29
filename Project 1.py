import tkinter

def doBut1():
    label_1.configure(text = "You attack the Cat")
    
def doBut2():
    label_1.configure(text = "You run away from the Cat")

def doBut3():
    label_1.configure(text = "You inspect the Cat")

def doBut4():
    label_1.configure(text = "You block the Cat")


          
bob = tkinter.Tk()

label_1 = tkinter.Text(bob)
label_1.insert(tkinter.INSERT,"You walk down a road in the middle of the night. The air is chilling and you feel a cold rush go down your spine. You feel something behind, Yout turn around and noticing something, a fat orange and white cat staring at you. You notice tomato sauce around its mouth. What do you do?")
label_1.grid(row=0, column=0, columnspan=10)



but1 = tkinter.Button(bob, text="Attack", command=doBut1, width=10)
but1.grid(row=1, column=0)

but2 = tkinter.Button(bob, text="Run", command=doBut2, width=10)
but2.grid(row=1, column=1)

but3 = tkinter.Button(bob, text="Inspect", command=doBut3, width=10)
but3.grid(row=2, column=0)

but4 = tkinter.Button(bob, text="Block", command=doBut4, width=10)
but4.grid(row=2, column=1)
          
                    
bob.mainloop()
