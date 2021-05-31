import tkinter
import tkinter.messagebox

root = tkinter.Tk()

def display_and_print():
    tkinter.messagebox.showinfo("Info","Just so you know")
    tkinter.messagebox.showwarning("Warning","Better be careful")
    tkinter.messagebox.showerror("Error","Something went wrong")

    okcancel = tkinter.messagebox.askokcancel("What do you think?","Should we go ahead?")
    print(okcancel)

    yesno = tkinter.messagebox.askyesno("What do you think?","Please decide")
    print(yesno)

    retrycancel = tkinter.messagebox.askretrycancel("What do you think?","Should we try again?")
    print(retrycancel)

    answer = tkinter.messagebox.askquestion("What do you think?","What's your answer?")
    print(answer)

b1 = tkinter.Button(root, text='Display dialogs', command=display_and_print)
b1.pack(fill='x')

root.mainloop()