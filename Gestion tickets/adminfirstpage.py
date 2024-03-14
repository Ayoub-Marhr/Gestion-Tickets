from tkinter import * 
import admininterface  
def open_admininterface():
    root.destroy()  
    admin_app = admininterface.TicketViewerApp(Tk()) 
    


def crud():
    root.destroy()
    import admincrud

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

Button(fram, width=39, pady=7, text='crud', bg='#57a1f8', fg='white', border=0, activebackground='#2c81f0', command=crud).place(x=35, y=134)
Button(fram, width=39, pady=7, text='gestion tickets', bg='#57a1f8', fg='white', border=0, activebackground='#2c81f0', command=open_admininterface).place(x=35, y=204)

root.mainloop()
