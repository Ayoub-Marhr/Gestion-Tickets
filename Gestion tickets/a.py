import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

LIGHT_GRAY = "#F0F0F0"
DARK_GRAY = "#333333"
BUTTON_COLORS = {
    "Show Ticket": "#3498db",
    "Delete Ticket": "#E74C3C",
    "Go Back": "#2ECC71"
}

class TicketViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Viewer")
        self.root.geometry("950x650")
        self.root.configure(bg=DARK_GRAY)

        self.conn = self.connect_to_database()
        self.tickets = self.fetch_tickets()
        self.filtered_tickets = []

        self.create_widgets()

    def connect_to_database(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='gestion_tickets'
            )
            return conn
        except mysql.connector.Error as e:
            print("Error:", e)
            return None

    def fetch_tickets(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT id, Nom, category, problem, description FROM tickets")
                tickets = cursor.fetchall()
                cursor.close()
                return tickets
            except mysql.connector.Error as e:
                print("Error:", e)
        return []

    def delete_ticket(self):
        selected_index = self.ticket_listbox.curselection()
        if selected_index:
            selected_ticket = self.tickets[selected_index[0]]
            ticket_id = selected_ticket[0]

            self.delete_ticket_db(ticket_id)
            self.ticket_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a ticket to delete.")

    def delete_ticket_db(self, ticket_id):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
                self.conn.commit()
                cursor.close()
            except mysql.connector.Error as e:
                print("Error:", e)

    def show_ticket_details(self):
        selected_index = self.ticket_listbox.curselection()
        if selected_index:
            selected_ticket = self.tickets[selected_index[0]]
            self.ticket_treeview.delete(*self.ticket_treeview.get_children())

            self.ticket_treeview.insert("", "end", values=(selected_ticket[1], selected_ticket[2], selected_ticket[3], selected_ticket[4]))
        else:
            messagebox.showwarning("Warning", "Please select a ticket to show its details.")

    def go_back(self):
        self.ticket_treeview.delete(*self.ticket_treeview.get_children())
        self.ticket_listbox.selection_clear(0, tk.END)

    def search_tickets(self):
        search_term = self.search_entry.get().strip().lower()
        if search_term:
            self.filtered_tickets = [ticket for ticket in self.tickets if search_term in ticket[1].lower() or search_term == str(ticket[0])]
        else:
            self.filtered_tickets = self.tickets

        self.update_ticket_listbox()

    def update_ticket_listbox(self):
        self.ticket_listbox.delete(0, tk.END)
        for ticket in self.filtered_tickets:
            self.ticket_listbox.insert(tk.END, f"Ticket {ticket[0]} - {ticket[1]}")

    def create_widgets(self):
        app_font = ("Arial", 12)
        self.root.option_add("*TButton*font", app_font)
        self.root.option_add("*TLabel*font", app_font)
        self.root.option_add("*TListbox*font", app_font)
        self.root.option_add("*TText*font", app_font)
        self.root.option_add("*Title.TLabel*font", ("Helvetica", 16, "bold"))

        title_label = tk.Label(self.root, text="Ticket Viewer", font=("Helvetica", 36, "bold"), bg=DARK_GRAY, fg=LIGHT_GRAY)
        title_label.pack(pady=(30, 10))

        search_label = tk.Label(self.root, text="Search Ticket ", font=("Arial", 12), bg=DARK_GRAY, fg=LIGHT_GRAY)
        search_label.pack(pady=(0, 5))

        self.search_entry = tk.Entry(self.root, font=("Arial", 12))
        self.search_entry.pack(pady=(0, 10), padx=200)

        search_button = tk.Button(self.root, text="Search", command=self.search_tickets, font=("Arial", 12), bg=BUTTON_COLORS["Show Ticket"], fg=LIGHT_GRAY, activebackground=BUTTON_COLORS["Show Ticket"], activeforeground=LIGHT_GRAY, bd=0, padx=15, pady=5)
        search_button.pack(padx=200)

        self.ticket_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=("Helvetica", 14), bd=0, highlightthickness=0)
        self.ticket_listbox.pack(padx=200, pady=5)

        for ticket in self.tickets:
            self.ticket_listbox.insert(tk.END, f"Ticket {ticket[0]} - {ticket[1]}")
            self.filtered_tickets.append(ticket)

        buttons_frame = tk.Frame(self.root, bg=DARK_GRAY)
        buttons_frame.pack(pady=10)

        for btn_text, btn_command in [("Show Ticket", self.show_ticket_details), ("Delete Ticket", self.delete_ticket), ("Go Back", self.go_back)]:
            button = tk.Button(
                buttons_frame,
                text=btn_text,
                command=btn_command,
                font=("Arial", 12),
                bg=BUTTON_COLORS[btn_text],
                fg=LIGHT_GRAY,
                activebackground=BUTTON_COLORS[btn_text],
                activeforeground=LIGHT_GRAY,
                bd=0,
                padx=15,
                pady=5,
            )
            button.pack(side=tk.LEFT, padx=5)

        details_frame = tk.LabelFrame(self.root, text="Ticket Details", font=("Helvetica", 14, "bold"), bg=DARK_GRAY, fg=LIGHT_GRAY)
        details_frame.pack(padx=20, pady=10, fill="both", expand="yes")

        self.ticket_treeview = ttk.Treeview(details_frame, columns=("Name", "Category", "Problem", "Description"), show="headings")
        self.ticket_treeview.heading("Name", text="Name")
        self.ticket_treeview.heading("Category", text="Category")
        self.ticket_treeview.heading("Problem", text="Problem")
        self.ticket_treeview.heading("Description", text="Description")
        self.ticket_treeview.pack(padx=10, pady=(0, 1), fill="both", expand="yes")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketViewerApp(root)
    root.mainloop()

