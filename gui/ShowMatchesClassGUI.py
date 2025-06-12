import tkinter as tk
from tkinter import ttk

from db_connection import get_connection

from models.MatchManager import MatchManager  # import your MatchManager here

class ShowMatchesClassGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Matches List")
        self.master.geometry("700x400")

        self.match_manager = MatchManager()
        # Title label
        title = tk.Label(master, text="All Matches", font=("Arial", 16))
        title.pack(pady=10)

        # Define treeview widget BEFORE packing it
        columns = ("ID", "Team 1", "Team 2", "Date", "Score 1", "Score 2")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)

        # Now pack it
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load matches to show in treeview


    def load_matches(self):
        try:
            matches = self.match_manager.get_all_matches()
            print("Fetched matches:", matches)  # Debug output

            if not matches:
                print("No matches found in the database.")
                return  # Exit early — don’t try to insert anything

            for match in matches:
                self.tree.insert("", tk.END, values=match)

        except Exception as e:
            print("Error while loading matches:", e)


if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("Show Matches GUI Test")
    root.geometry("600x400")  # Adjust size as you want
    app = ShowMatchesClassGUI(root)
    root.mainloop()