import tkinter as tk
from tkinter import messagebox

contacts = []


# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully!")


# Display Contacts
def refresh_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']}"
        )


# Clear Fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# Search Contact
def search_contact():
    keyword = search_entry.get().lower()

    contact_listbox.delete(0, tk.END)

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            contact_listbox.insert(
                tk.END,
                f"{contact['name']} - {contact['phone']}"
            )


# Select Contact
def select_contact(event):
    try:
        index = contact_listbox.curselection()[0]
        selected_text = contact_listbox.get(index)

        for contact in contacts:
            if selected_text.startswith(contact["name"]):
                clear_fields()

                name_entry.insert(0, contact["name"])
                phone_entry.insert(0, contact["phone"])
                email_entry.insert(0, contact["email"])
                address_entry.insert(0, contact["address"])

                global selected_index
                selected_index = contacts.index(contact)
                break

    except:
        pass


# Update Contact
def update_contact():
    try:
        contacts[selected_index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }

        refresh_list()
        clear_fields()

        messagebox.showinfo("Success", "Contact Updated!")

    except:
        messagebox.showwarning("Warning", "Select a contact first!")


# Delete Contact
def delete_contact():
    try:
        del contacts[selected_index]

        refresh_list()
        clear_fields()

        messagebox.showinfo("Success", "Contact Deleted!")

    except:
        messagebox.showwarning("Warning", "Select a contact first!")


# Main Window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("700x550")
root.configure(bg="#f2f2f2")

title = tk.Label(
    root,
    text="Contact Management System",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=10)

# Search Section
search_frame = tk.Frame(root, bg="#f2f2f2")
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search:", bg="#f2f2f2").pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_contact,
    bg="lightblue"
).pack(side=tk.LEFT)

# Form Section
form_frame = tk.Frame(root, bg="#f2f2f2")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=40)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(form_frame, width=40)
phone_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=40)
email_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(form_frame, width=40)
address_entry.grid(row=3, column=1)

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Contact",
    command=add_contact,
    bg="lightgreen",
    width=15
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update Contact",
    command=update_contact,
    bg="orange",
    width=15
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete Contact",
    command=delete_contact,
    bg="tomato",
    width=15
).grid(row=0, column=2, padx=5)

# Contact List
contact_listbox = tk.Listbox(root, width=70, height=15)
contact_listbox.pack(pady=10)

contact_listbox.bind("<<ListboxSelect>>", select_contact)

root.mainloop()
