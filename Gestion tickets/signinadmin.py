from tkinter import *
from tkinter import messagebox
from ouvrieslibrary import Ouvrier
from loginadminbackend import login

def signup():
    root.destroy()
    import Signup

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

def on_enter_password(e):
    code.delete(0, 'end')

def on_leave_password(e):
    if code.get() == '':
        code.insert(0, 'Password')

def loginlogic():
    ouvrierdata = Ouvrier(nom=user.get(), password=code.get())
    result = login(ouvrierdata)
    if result is not None:
        if user.get()=='Username':
            messagebox.showerror("Ouvrier", "Incorrect Nom and password")
        
        elif user.get()!='Username':
            messagebox.showinfo("Ouvrier", "Welcome {}".format(user.get()))
        admin()
    else:
        messagebox.showerror("Ouvrier", "Incorrect Nom and password")
def admin():
    root.destroy()
    import adminfirstpage
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='assets/login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

fram = Frame(root, width=350, height=350, bg="white")
fram.place(x=480, y=70)

heading = Label(fram, text="Sign in", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(fram, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(fram, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(fram, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)
Frame(fram, width=295, height=2, bg='black').place(x=25, y=177)

Button(fram, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=loginlogic).place(x=35, y=204)



root.mainloop()
