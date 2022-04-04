from tkinter import *  # import all
root = Tk()

root.geometry('500x400')  # display area
root.title("Afnan Registration Form")  # title
a = Label(root, text="♡ Afnan Registration form ♡ ", fg='hotpink', width=25, font=("bold", 20))
a.place(x=90, y=53)  # place
f = Label(root, text="Email address", width=20, font=("bold", 10))
f.place(x=80, y=130)
e = Entry(root)
e.place(x=240, y=130)
n = Label(root, text="password", width=20, font=("bold", 10))
n.place(x=68, y=180)
t = Entry(root)
t.place(x=240, y=180)
var = IntVar()
Checkbutton(root, text="Remember me", padx=5, variable=var, onvalue=1).place(x=120, y=230)
Button(root, text='Submit', width=20, bg='hotpink', fg='white').place(x=180, y=280)
x = Label(root, text="Forgot ", width=15, font=("bold", 8))
x.place(x=300, y=320)
z = Label(root, text="password?", fg='lightblue', width=10, font=("bold", 8))
z.place(x=370, y=320)

root.mainloop()

print("Registration Form seccussfully Created")