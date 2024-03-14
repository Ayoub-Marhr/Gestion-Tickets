from tkinter import *
from tkinter import messagebox
from ouvrieslibrary import Ouvrier
from singupbackend import singup

def signin():
    window.destroy()
    import singin

def singuplogic():
    ouvrierdata = Ouvrier(nom=user.get(), password=code.get())
    result = singup(ouvrierdata)
    if result is None:
       if user.get()=='Username':
            messagebox.showerror("Ouvrier", "Incorrect Nom and password")
        
    elif user.get()!='Username':
            messagebox.showinfo("Ouvrier", " {} Bien ajouter".format(user.get()))
    else:
        messagebox.showerror("Ouvrier", "Incorrect Nom and password")

window = Tk()
window.title("SignUP")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

image = PhotoImage(file='assets/Sign up.png')
Label(window, image=image, border=0, bg='white').place(x=50, y=90)
fram = Frame(window, width=350, height=390, bg='white')
fram.place(x=480, y=50)

heading = Label(fram, text='Sing up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(fram, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(fram, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(fram, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(fram, width=295, height=2, bg='black').place(x=25, y=177)

def on_enter(e):
    conform.delete(0, 'end')

def on_leave(e):
    if conform.get() == '':
        conform.insert(0, 'Conform Password')

conform = Entry(fram, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
conform.place(x=30, y=220)
conform.insert(0, 'Conform Password')
conform.bind("<FocusIn>", on_enter)
conform.bind("<FocusOut>", on_leave)

Frame(fram, width=295, height=2, bg='black').place(x=25, y=247)

signup_button = Button(fram, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=singuplogic)
signup_button.place(x=35, y=280)

signin_label = Label(fram, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
signin_label.place(x=90, y=340)

signin = Button(fram, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signin)
signin.place(x=200, y=340)

window.mainloop()
