from tkinter import *
import pyshorteners

def Gen_password():
    url=var.get()
    shoturl=pyshorteners.Shortener()

    global  shorturl
    shorturl=shoturl.tinyurl.short(url)


    var2.set(shorturl)


def copy():
    root.clipboard_clear()
    root.clipboard_append(shorturl)



root=Tk()
root.geometry("400x170")
root.resizable(0,0)
root.title("Url Shorter")


var=StringVar()
var2=StringVar()

inputLable=Label(root,text="Enter the URL",pady=5).pack()
inputEntry=Entry(root,textvariable=var).pack(ipadx=100)

button1=Button(root,text="Get short url", relief=RAISED,pady=0,command=Gen_password).pack()


output=Label(root,text="output",pady=10,fg="red",font="bold").pack()
outputEntry=Entry(root,textvariable=var2).pack(ipadx=100)
button2=Button(root,text="Copy", relief=RAISED,pady=0,command=copy).pack()



root.mainloop()


