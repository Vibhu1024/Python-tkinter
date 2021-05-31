import tkinter
import tkinter.colorchooser

root = tkinter.Tk()

def color_button():
    color = tkinter.colorchooser.askcolor(parent=root)
    print(color)
    b1.configure(bg=color[1])

b1 = tkinter.Button(root, text='Select Color', command=color_button)
b1.pack(fill='x')

root.mainloop()