from tkinter import *
from tkinter import messagebox
from issuelibrary import issue
from database import Connect

def save(issue):
    conn = None
    sql = """INSERT INTO tickets (Nom, category, problem, description) VALUES (%s, %s, %s, %s) """
    values = (issue.getNom(), issue.getcategory(), issue.getproblem(), issue.getdescription())
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        messagebox.showinfo('Ticket Submitted', 'Your ticket has been submitted successfully!')
    except Exception as e:
        print('Error:', e)
        messagebox.showerror('Error', 'An error occurred while submitting the ticket.')
    finally:
        if conn:
            conn.close()

root = Tk()
root.title("Helpdesk Worker Interface")
root.geometry('925x500+300+200')
root.configure(bg='#f2f2f2')
root.resizable(False, False)

img = PhotoImage(file='assets/help.png')
Label(root, image=img, bg='#f2f2f2').place(x=50, y=80)

title = Label(root, text='Helpdesk Worker Interface', font=('Helvetica', 24, 'bold'), bg='#f2f2f2', fg='#335592')
title.place(relx=0.35, y=20, anchor='center')

worker = Frame(root, bg='#f2f2f2')
worker.place(relx=0.8, rely=0.5, anchor='center')

# Style for labels
label_style = {
    'font': ('Helvetica', 12),
    'bg': '#f2f2f2',
    'fg': '#335592',
}

# Style for entry widgets
entry_style = {
    'font': ('Helvetica', 11),
    'bd': 2,
    'relief': 'groove',
}

nom_label = Label(worker, text='Username', **label_style)
nom_label.pack(pady=5)

nom_entry = Entry(worker, **entry_style, width=25)
nom_entry.pack(pady=5, ipady=3)

problem_categories = {
    'Hardware Issue': ['Monitor', 'Keyboard', 'Mouse', 'Other Hardware Problems'],
    'Software Issue': ['Application Errors', 'Operating System Problems', 'Software Installation', 'Other Software Problems'],
    'Network Issue': ['Internet Connection', 'Network Configuration', 'Wi-Fi Problems', 'Other Network Problems'],
    'Other': ['Other Problems']
}
category = StringVar()
category.set('Hardware Issue')

category_label = Label(worker, text='Select Problem Category', **label_style)
category_label.pack(pady=(20, 5))

category_menu = OptionMenu(worker, category, *problem_categories.keys())
category_menu.config(font=('Helvetica', 11), bg='white', highlightthickness=0, width=25)
category_menu.pack(pady=5, ipady=3)

specific_problem_label = Label(worker, text='Specific Problem', **label_style)
specific_problem_label.pack(pady=5)

specific_problem_entry = Entry(worker, **entry_style, width=25)
specific_problem_entry.pack(pady=5, ipady=3)

description_label = Label(worker, text='Describe the Problem', **label_style)
description_label.pack(pady=(10, 5))

description = Text(worker, height=5, width=40, borderwidth=2, relief="groove", font=('Helvetica', 11))
description.pack(pady=5)

def submit_ticket_details():
    issue_obj = issue(nom=nom_entry.get(), category=category.get(), problem=specific_problem_entry.get(), descrition=description.get("1.0", "end-1c"))
    save(issue_obj)

submit_button = Button(worker, text='Submit Ticket',width=20,  border=0, bg='#335592', fg='white',  cursor='hand2', activebackground='#263849', activeforeground='white', command=submit_ticket_details)
submit_button.config(font=('Helvetica', 11), padx=15, pady=5)
submit_button.pack(pady=10, ipadx=10)

logout_button = Button(worker,width=3,  border=0, text='Logout', bg='#335592', fg='white',  cursor='hand2',activebackground='#263849', activeforeground='white', command=root.destroy)
logout_button.config(font=('Helvetica', 11), padx=15, pady=5)
logout_button.pack(pady=10, ipadx=10)

root.mainloop()
