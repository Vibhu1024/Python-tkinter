import tkinter
import tkinter.filedialog

root = tkinter.Tk()

def display_image():
    f = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='C:/Tutorial',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif')]
        )

    new_window = tkinter.Toplevel(root)

    image = tkinter.PhotoImage(file=f)
    l1 = tkinter.Label(new_window, image=image)
    l1.image = image
    l1.pack()

b1 = tkinter.Button(root, text='Display image', command=display_image)
b1.pack(fill='x')

root.mainloop()