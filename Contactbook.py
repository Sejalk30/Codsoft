import tkinter as tk
from tkinter import messagebox, simpledialog
import re

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}  
        
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=0, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Display Contacts", command=self.display_contacts).grid(row=0, column=4, padx=10, pady=10)
        tk.Button(self.root, text="Save Email", command=self.save_email).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Save Address", command=self.save_address).grid(row=1, column=1, padx=10, pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter contact phone number:")
            email = simpledialog.askstring("Input", "Enter contact email address:")
            address = simpledialog.askstring("Input", "Enter contact address:")
            if phone and email and address and self.validate_phone(phone) and self.validate_email(email):
                self.contacts[name] = (phone, email, address)
                messagebox.showinfo("Success", "Contact added successfully")
            else:
                messagebox.showwarning("Invalid Input", "Please enter valid phone number, email address, and address")

    def search_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to search:")
        if name:
            contact = self.contacts.get(name, None)
            if contact:
                phone, email, address = contact
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}")
            else:
                messagebox.showwarning("Not Found", "Contact not found")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to update:")
        if name:
            if name in self.contacts:
                phone = simpledialog.askstring("Input", "Enter new phone number:")
                email = simpledialog.askstring("Input", "Enter new email address:")
                address = simpledialog.askstring("Input", "Enter new address:")
                if phone and email and address and self.validate_phone(phone) and self.validate_email(email):
                    self.contacts[name] = (phone, email, address)
                    messagebox.showinfo("Success", "Contact updated successfully")
                else:
                    messagebox.showwarning("Invalid Input", "Please enter valid phone number, email address, and address")
            else:
                messagebox.showwarning("Not Found", "Contact not found")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to delete:")
        if name:
            if name in self.contacts:
                del self.contacts[name]
                messagebox.showinfo("Success", "Contact deleted successfully")
            else:
                messagebox.showwarning("Not Found", "Contact not found")

    def display_contacts(self):
        if self.contacts:
            sorted_contacts = sorted(self.contacts.items())
            contacts_list = "\n".join([f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}" for name, (phone, email, address) in sorted_contacts])
            messagebox.showinfo("Contacts", contacts_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available")

    def save_email(self):
        name = simpledialog.askstring("Input", "Enter contact name to update email:")
        if name:
            if name in self.contacts:
                new_email = simpledialog.askstring("Input", "Enter new email address:")
                if new_email and self.validate_email(new_email):
                    phone, _, address = self.contacts[name]
                    self.contacts[name] = (phone, new_email, address)
                    messagebox.showinfo("Success", "Email updated successfully")
                else:
                    messagebox.showwarning("Invalid Input", "Please enter a valid email address")
            else:
                messagebox.showwarning("Not Found", "Contact not found")

    def save_address(self):
        name = simpledialog.askstring("Input", "Enter contact name to update address:")
        if name:
            if name in self.contacts:
                new_address = simpledialog.askstring("Input", "Enter new address:")
                if new_address:
                    phone, email, _ = self.contacts[name]
                    self.contacts[name] = (phone, email, new_address)
                    messagebox.showinfo("Success", "Address updated successfully")
                else:
                    messagebox.showwarning("Invalid Input", "Please enter a valid address")
            else:
                messagebox.showwarning("Not Found", "Contact not found")

    def validate_phone(self, phone):
        return re.fullmatch(r'\d{10}', phone) is not None

    def validate_email(self, email):
        return re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email) is not None

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
