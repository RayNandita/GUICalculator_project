from tkinter import *

# Operations in calculator
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
             
        scvalue.set(value)
    elif text == 'C':
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)

window = Tk()
window.geometry("600x650") 
window.minsize(600,650)
window.maxsize(600,650)
window.config(bg="gray")
window.title("Calculator")
icon = PhotoImage(file=r"C:\Users\ADARSHA\Downloads\cgec_logo_white-removebg-preview.png")
window.iconphoto(False, icon)

scvalue = StringVar()
scvalue.set("")
f = Frame(window, padx=20, pady=20)
screen = Entry(f, textvar=scvalue, font="lucida 50 bold", bg="light blue")
screen.pack(fill=X, padx=20, pady=15)
f.pack()

# Options Rows
option1 = ["7", "8", "9", "+"]
option2 = ["4", "5", "6", "-"]
option3 = ["1", "2", "3", "*"]
option4 = ["0", "C", "=", "/"]

# For option 1
f = Frame(window, bg="gray", padx=30, pady=10)
for i in option1:
    b = Button(f, text=i, padx=10, pady=10, font="lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

# For option 2
f = Frame(window, bg="gray", padx=30, pady=10)
for i in option2:
    b = Button(f, text=i, padx=10, pady=10, font="lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

# For option 3
f = Frame(window, bg="gray", padx=30, pady=10)
for i in option3:
    b = Button(f, text=i, padx=10, pady=10, font="lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

# For option 4
f = Frame(window, bg="gray", padx=30, pady=10)
for i in option4:
    b = Button(f, text=i, padx=10, pady=10, font="lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

window.mainloop()
