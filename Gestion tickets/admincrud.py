import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Admin Interface")
root.geometry("925x500+300+200")
root.configure(bg="#F0F0F0")
root.resizable(False, False)
my_tree = ttk.Treeview(root, style="Custom.Treeview")
style = ttk.Style()

style.configure("Custom.Treeview.Heading", font=('Arial bold', 15))
style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=('Arial', 12), background="#F0F0F0")

style.layout("Custom.Treeview", [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

storeName = "Gestion d'ouvrier"

def insert(ID, Nom, Password, Fonction):
    conn = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="", 
        database="gestion_tickets"
    )
    cursor = conn.cursor()

    query = "INSERT INTO ouvrier (ID, Nom, Password, Fonction) VALUES (%s, %s, %s, %s)"
    values = (ID, Nom, Password, Fonction)
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def delete(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="", 
        database="gestion_tickets"
    )
    cursor = conn.cursor()

    query = "DELETE FROM ouvrier WHERE ID = %s"
    value = (data,)
    cursor.execute(query, value)
    conn.commit()
    conn.close()

def update(ID, Nom, Password, Fonction, idName):
    conn = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="", 
        database="gestion_tickets"
    )
    cursor = conn.cursor()

    query = "UPDATE ouvrier SET ID = %s, Nom = %s, Password = %s, Fonction = %s WHERE ID = %s"
    values = (ID, Nom, Password, Fonction, idName)
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def read():
    conn = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="", 
        database="gestion_tickets"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM ouvrier"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def insert_data():
    itemId = entryId.get()
    itemName = entryName.get()
    itemPassword = entryPassword.get()
    itemFonction = entryFonction.get()

    if not itemId or not itemName or not itemPassword or not itemFonction:
        print("Error Inserting Data")
    else:
        insert(itemId, itemName, itemPassword, itemFonction)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in read():
        my_tree.insert(parent='', index='end', values=result, tag="orow")

    my_tree.tag_configure('orow', background='#C8D9E3')
    my_tree.place(x=350, y=120, anchor="nw")

def delete_data():
    selected_item = my_tree.selection()[0]
    delete_id = my_tree.item(selected_item)['values'][0]

    confirmed = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this record?")

    if confirmed:
        delete(delete_id)

        for data in my_tree.get_children():
            my_tree.delete(data)

        for result in read():
            my_tree.insert(parent='', index='end', values=result, tag="orow")

        my_tree.tag_configure('orow', background='#C8D9E3')
        my_tree.place(x=350, y=120, anchor="nw")

def update_data():
    selected_item = my_tree.selection()[0]
    update_id = my_tree.item(selected_item)['values'][0]

    confirmed = messagebox.askyesno("Update Confirmation", "Are you sure you want to update this record?")

    if confirmed:
        update(entryId.get(), entryName.get(), entryPassword.get(), entryFonction.get(), update_id)

        for data in my_tree.get_children():
            my_tree.delete(data)

        for result in read():
            my_tree.insert(parent='', index='end', values=result, tag="orow")

        my_tree.tag_configure('orow', background='#C8D9E3')
        my_tree.place(x=350, y=120, anchor="nw")



def search_data():
    search_text = entrySearch.get().strip().lower()

    for data in my_tree.get_children():
        my_tree.delete(data)

    results = read()

    filtered_results = []
    if search_text:
        for result in results:
            if (str(result[0]) == search_text) or \
               (search_text in result[1].lower()) or \
               (search_text in result[3].lower()):
                filtered_results.append(result)
    else:
        filtered_results = results

    for result in filtered_results:
        my_tree.insert(parent='', index='end', values=result, tag="orow")

    my_tree.tag_configure('orow', background='#C8D9E3', font=('Arial bold', 15))
    my_tree.place(x=350, y=120, anchor="nw")



titleLabel = Label(
    root,
    text=storeName,
    font=('Arial bold', 30),
    bg="#1B7BB6",  
    fg="white",   
    bd=2,         
    relief="solid",  
    padx=20,      
    pady=10,      
)
titleLabel.place(x=20,y=20)

idLabel = Label(root, text="ID", font=('Arial bold', 15), bg="#F0F0F0", fg='#1B7BB6')
nameLabel = Label(root, text="Name", font=('Arial bold', 15), bg="#F0F0F0", fg='#1B7BB6')
passwordLabel = Label(root, text="Password", font=('Arial bold', 15), bg="#F0F0F0", fg='#1B7BB6')
fonctionLabel = Label(root, text="Fonction", font=('Arial bold', 15), bg="#F0F0F0", fg='#1B7BB6')
idLabel.place(x=40, y=130)
nameLabel.place(x=40, y=200)
passwordLabel.place(x=40, y=270)
fonctionLabel.place(x=40, y=350)

entryId = Entry(root, width=15, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
entryId.place(x=140, y=130)  
Frame(root, width=150, height=2, bg='black').place(x=140, y=153)

entryName = Entry(root, width=15, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
entryName.place(x=140, y=200)
Frame(root, width=150, height=2, bg='black').place(x=140, y=223)

entryPassword = Entry(root, width=15, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
entryPassword.place(x=140, y=270)
Frame(root, width=150, height=2, bg='black').place(x=140, y=293)

entryFonction = Entry(root, width=15, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
entryFonction.place(x=140, y=355)
Frame(root, width=150, height=2, bg='black').place(x=140, y=378)

entrySearch = Entry(root, width=35, fg='black', border=0.5, bg='white', font=('Microsoft Yahei UI Light', 11))
entrySearch.place(x=465, y=80, anchor="w")

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=9,
    bd=3, font=('Arial', 15), bg="#57a1f8", command=insert_data)
buttonEnter.place(x=5, y=450, anchor="w")

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=9,
    bd=3, font=('Arial', 15), bg="#57a1f8", command=update_data)
buttonUpdate.place(x=115, y=450, anchor="w")

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=7,
    bd=3, font=('Arial', 15), bg="#57a1f8", command=delete_data)
buttonDelete.place(x=225, y=450, anchor="w")

buttonSearch = Button(root, text="Search", width=12, height=1, bd=2, font=('Arial', 15), bg="#57a1f8", command=search_data)
buttonSearch.place(x=750, y=80, anchor="w")

my_tree = ttk.Treeview(root, style="Custom.Treeview")
style = ttk.Style()

style.configure("Custom.Treeview.Heading", font=('Arial bold', 15))
style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=('Arial', 12), background="#F0F0F0")

style.layout("Custom.Treeview", [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

my_tree['columns'] = ("ID", "Name", "Password", "Fonction")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Password", anchor=W, width=150)
my_tree.column("Fonction", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Password", text="Password", anchor=W)
my_tree.heading("Fonction", text="Fonction", anchor=W)

my_tree.delete(*my_tree.get_children())
for result in read():
    my_tree.insert(parent='', index='end', values=result, tag="orow")

my_tree.tag_configure('orow', background='#C8D9E3', font=('Arial bold', 15))
my_tree.place(x=335, y=120, anchor="nw", height=383, width=590)

root.mainloop()
