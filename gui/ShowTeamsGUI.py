import tkinter as tk
from tkinter import messagebox
import sqlite3  # or psycopg2 for PostgreSQL

def get_connection():
    # Change this according to your DB. This example uses SQLite:
    return sqlite3.connect("sports.db")

class ShowTeamsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Teams List")
        self.root.geometry("300x400")

        # Listbox to show teams
        self.team_listbox = tk.Listbox(root, width=40, height=20)
        self.team_listbox.pack(pady=20)

        # Button to refresh teams
        self.refresh_btn = tk.Button(root, text="Show Teams", command=self.show_teams)
        self.refresh_btn.pack()

        self.show_teams()  # load teams at start

    def show_teams(self):
        self.team_listbox.delete(0, tk.END)  # Clear listbox
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT team_name FROM teams ORDER BY team_name")
            teams = cursor.fetchall()
            if not teams:
                messagebox.showinfo("Info", "No teams found.")
            for team in teams:
                self.team_listbox.insert(tk.END, team[0])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch teams:\n{e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowTeamsGUI(root)
    root.mainloop()