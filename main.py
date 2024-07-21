from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate_password():
    length = int(length_entry.get())
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    if length < 8:
        messagebox.showinfo(title="Error", message="Password length should be at least 8 characters.")
        return

    password_characters = random.choices(letters, k=length - 4) + random.choices(numbers, k=2) + random.choices(symbols, k=2)
    random.shuffle(password_characters)

    password = "".join(password_characters)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Some fields were left empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {email}\nPassword: {password}\nDo you want to save these?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = {}
            except FileNotFoundError:
                data = {}

            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            length_entry.delete(0, END)

            website_entry.focus()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website Name:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)

length_label = Label(text="Length of password:")
length_label.grid(row=3, column=0)
length_entry = Entry(width=45)
length_entry.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)
password_entry = Entry(width=45)
password_entry.grid(column=1, row=4, columnspan=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=4, columnspan=1)

add_button = Button(text="Add", width=22, command=save)
add_button.grid(column=1, row=5, columnspan=1)

window.mainloop()
