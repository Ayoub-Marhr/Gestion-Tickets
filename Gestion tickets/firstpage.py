from tkinter import *
from tkinter import messagebox



root = Tk()
root.title('First Page')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='assets/1 (1).png')
Label(root, image=img, bg='white').place(x=0, y=100)

fram = Frame(root, width=350, height=350, bg="#fff")
fram.place(x=590, y=80)
heading = Label(fram, text="Gestion de tickets", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=40, y=5)
def signup():
    root.destroy()
    import Signup
def signinadmin():
    root.destroy()
    import signinadmin
Button(fram, width=39, pady=7, text='Admin', bg='#57a1f8', fg='white', border=0,activebackground= '#2c81f0',command=signinadmin) .place(x=35, y=134)
Button(fram, width=39, pady=7, text='User', bg='#57a1f8', fg='white', border=0,activebackground= '#2c81f0',command=signup).place(x=35, y=204)
root.mainloop()