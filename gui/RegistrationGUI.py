import tkinter as tk
from tkinter import messagebox
from models.ManagerRegister import ManagerRegister
from models.UserRegister import UserRegister

class RegistrationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Register Manager")
        self.master.geometry("400x500")

        self.entries = {}

        fields = ["First Name", "Last Name", "Username", "Phone", "Gender", "Password", "Confirm Password"]
        for field in fields:
            tk.Label(master, text=field).pack(pady=2)
            show = "*" if "Password" in field else ""
            entry = tk.Entry(master, show=show)
            entry.pack()
            self.entries[field] = entry

        # the one who wants to register if he is a manager or user
        self.role_var = tk.StringVar(value="User")
        tk.Label(master, text="Select Role:").pack(pady=5)
        roles = [("User", "User"), ("Manager", "Manager")]
        for text, value in roles:
            tk.Radiobutton(master, text=text, variable=self.role_var, value=value, command=self.toggle_manager_code).pack()

        # the secret code for manager, not any one can be manager
        self.manager_code_label = tk.Label(master, text="Manager Secret Code")
        self.manager_code_entry = tk.Entry(master, show="*")

        tk.Button(master, text="Register", command=self.register).pack(pady=10)

    def toggle_manager_code(self):
        if self.role_var.get() == "Manager":
            self.manager_code_label.pack(pady=2)
            self.manager_code_entry.pack()
        else:
            self.manager_code_label.pack_forget()
            self.manager_code_entry.pack_forget()

    def register(self):
        data = {field: self.entries[field].get() for field in self.entries}
        role = self.role_var.get()

        # check if password match
        # if data["Password"] != data["confirm_password"]:
        #     messagebox.showerror("Error", "Passwords don't match.")
        #     return

        if role == "Manager":
            secret_code = self.manager_code_entry.get()
            if secret_code != "FSM25":
                messagebox.showerror("Error", "Invalid manager secret code.")
                return
            manager = ManagerRegister(
                data["First Name"],
                data["Last Name"],
                data["Username"],
                data["Phone"],
                data["Gender"],
                data["Password"],
                data["Confirm Password"]
            )
            manager.register_manager()
            messagebox.showinfo("Success", "Manager registered successfully.")
        else:
            # Call UserRegister to register user (we'll implement it next)
            user = UserRegister(
                data["First Name"],
                data["Last Name"],
                data["Username"],
                data["Phone"],
                data["Gender"],
                data["Password"],
                data["Confirm Password"]
            )
            user.register_user()
            messagebox.showinfo("Success", "User registered successfully.")

        self.master.destroy()