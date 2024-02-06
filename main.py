from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

MYEMAIL = "rahulparmar1978@gmail.com"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    new_entry = {
        website_entry.get(): {
            'email': email_entry.get(),
            'password': password_entry.get()
        }
    }
    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: {email_entry.get()} \nPassword: {password_entry.get()} \nIs it ok to save?")
        if is_ok:
            try:
                with open(".\\data.json", mode='r') as data_file:
                    data_dict = json.load(data_file)
            except FileNotFoundError:
                data_dict = new_entry
            else:
                data_dict.update(new_entry)
            finally:
                with open(".\\data.json", mode='w') as data_file:
                    json.dump(data_dict, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    try:
        with open(".\\data.json", mode='r') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    else:
        if website_entry.get() in data_dict:
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {data_dict[website_entry.get()]['email']}\nPassword: {data_dict[website_entry.get()]['password']}")
        else:
            messagebox.showinfo(title="Warning", message=f"No details for {website_entry.get()} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# Setup canvas with background image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo)

# Setup widgets
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_entry = Entry(width=20)
email_entry = Entry(width=40)
password_entry = Entry(width=20)
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_password, width=34)
search_button = Button(text="Search", command=find_password, width=16)
email_entry.insert(0, MYEMAIL)
website_entry.focus()

# Align widgets on window
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
search_button.grid(column=2, row=1)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

# Keep window visible
window.mainloop()
