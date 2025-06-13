import tkinter as tk
from tkinter import messagebox
from models.ManagerLogin import ManagerLogin
from models.UserLogin import UserLogin
from gui.RegistrationGUI import RegistrationGUI
from gui.HomePageGUI import HomePageGUI
from models.SessionManager import SessionManager


class LoginGUI:
    def __init__(self, master, home_window=None):
        self.master = master
        self.home_window = home_window
        self.master.title("Login")
        self.master.geometry("300x300")

        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        # the one who wants to register if he is a manager or user
        self.role_var = tk.StringVar(value="User")  # Default role
        tk.Label(master, text="Select Role").pack(pady=5)
        roles = [("User", "User"), ("Manager", "Manager")]
        for text, value in roles:
            tk.Radiobutton(master, text=text, variable=self.role_var, value=value).pack()

        tk.Button(master, text="Login", command=self.login).pack(pady=10)

        self.register_label = tk.Label(master, text="Don't have an account? Register here.", fg="blue", cursor="hand2")
        self.register_label.pack(pady=5)
        self.register_label.bind("<Button-1>", self.open_register_window)

        tk.Button(master, text="Register", command=self.open_register_window).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        if role == "Manager":
            manager = ManagerLogin(username, password)
            if manager.login():
                SessionManager.set_logged_in_manager(username)
                # ask the database what is the role of this username
                role = manager.get_role() # this method is to check the role in the DB

                messagebox.showinfo("Success", f"Login Successful as {role}")
                self.master.destroy()  # Optionally move to another screen

                if self.home_window:
                    self.home_window.destroy()

                home_root = tk.Tk()
                HomePageGUI(home_root, logged_in=True, role=role)
                home_root.mainloop()
            else:
                messagebox.showerror("Error", "Manager Login Failed")
        else:
            user = UserLogin(username, password)
            if user.login():
                SessionManager.set_logged_in_manager(username)
                messagebox.showinfo("Success", "User Login Successful")
                self.master.destroy()
                if self.home_window:
                    self.home_window.destroy()
                home_root = tk.Tk()
                HomePageGUI(home_root, logged_in=True, role="User")
                home_root.mainloop()
            else:
                messagebox.showerror("Error", "User Login Failed")

    def open_register_window(self, event=None):
        """Open the Register window. 'event=None' allows both button click to call this"""
        register_window = tk.Toplevel(self.master)
        RegistrationGUI(register_window)