from tkinter import *
top = Tk()
def send():
    send="you:"+a.get()
    text.insert(END,"\n"+send)
    if(a.get() == 'hi'):
        text.insert(END,"\n" + "Bot:hello")
    elif(a.get() == 'hello'):
        text.insert(END, "\n" + "Bot:hi")
    elif(a.get() == 'how are you'):
        text.insert(END, "\n" + "Bot:i am fine. how are yoy?")
    elif (a.get() == 'i am fine'):
        text.insert(END, "\n" + "Bot:nice to hear that")
    else:
        text.insert(END, "\n" + "i didn't get it")
        text=Text(top, bg='white')
        text.grid(row=0,column=0,columnspan=2)
        a=entry(top.width=80)
        send = Button(root,text='Send', bg='white', width=20, command=send).grid(row=1,column=0)
        a.grid(row=1,column=1)
        top.title('simple chatbox')
        top.mainloop()
