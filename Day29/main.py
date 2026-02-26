from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json




def search_site():
    site = website_entry.get().title()

    try:
        with open("data.json", "r") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file Found.")
    else:
        try:
            website_data = data[site]
        except KeyError:
            messagebox.showerror(title="Error", message="No data for this website")
        else:
            site_name = site
            site_email = website_data["email"]
            site_password = website_data["password"]
            messagebox.showinfo(title=site_name, message=f"Email: {site_email}\nPassword: {site_password}")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2,4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = char_list  + symbol_list + numbers_list

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title= "Oops", message = "Please donn't leave any field empty")
    else:
        is_ok  = messagebox.askokcancel(message=f"website: {website}\nEmail: {email}\nPassword: {password}\nIs this okay to save?")
    
    if is_ok:

        try:
            file = open("data.json", "r")
        except FileNotFoundError:
            file = open("data.json", "w")
            json.dump(new_data, file, indent=4)
            file.close()
        else:
            data = json.load(file)
            data.update(new_data)
            file.close()
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            # email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#website area
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="ew")
search_button = Button(text="Search", command=search_site)
search_button.grid(column=2,  row=1, sticky="ew")

#email and username area
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(padx=10)
email_entry = Entry(width=30)
email_entry.insert("end", "teleturbies@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")


#password area
password_label = Label(text="Password:")
password_label.grid(column=0,  row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew")

#add button area
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()