from tkinter import *
#import myfunc as myfunc
root = Tk()
root.geometry("600x600")
# creating a function
def myfunc():
    Label(toot, text="saving...").pack()
 # creating a menu
mymenubar = Menu(root)
m1 = Menu(mymenubar, tearoff=0)
# givng a label
m1.add_command(label="Save", command=myfunc)
# seperating two labels of menu
m1.add_separator()
m1.add_command(label="Exit", command=quit)
mymenubar.add_cascade(label="File", menu=m1)
# adding one more dropdown menu to main menu
m2 = Menu(mymenubar, tearoff=0)
# adding a label
m2.add_command(label="Find", command=myfunc)
#adding a seperator
m2.add_separator()
m2.add_command(label="Exit", command=quit)
mymenubar.add_cascade(label="edit", menu=m2)
root.config(menu=mymenubar)
root.mainloop()
