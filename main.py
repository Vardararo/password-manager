from tkinter import *
from tkinter import messagebox, ttk
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pw_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    pw_list = password_letters + password_symbols + password_numbers
    random.shuffle(pw_list)

    passw = "".join(pw_list)
    pw_entry.insert(END, passw)
    
    # Use pyperclip to automatically copy the new pasword to the clipboard for ease of access
    pyperclip.copy(passw)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = user_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }}
    
    # Check if the correct credentials are entered
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave empty fields!")
    # Review inserted data before saving to a file
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")  
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file) # Read data from json
                    data.update(new_data) # Update data from json
                with open("data.json", "w") as file:   
                    json.dump(data, file, indent=4) # Save updated data 
            
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            
            finally:    
                website_entry.delete(0, END)
                pw_entry.delete(0, END)

# Find a password for given website
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found!")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details exist for {website}!")

# Display all the passwords saved to the data.json file
def display_stored_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            stored_data_text.delete(1.0, END)
            for website, details in data.items():
                stored_data_text.insert(END, f"Website: {website}\nEmail: {details['email']}\nPassword: {details['password']}\n\n")
    except FileNotFoundError:
        stored_data_text.delete(1.0, END)
        stored_data_text.insert(END, "No stored data found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create Notebook
notebook = ttk.Notebook(window)
notebook.grid(column=0, row=0, sticky='NSEW')

# Create Frames for tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Manager")
notebook.add(tab2, text="Vault")

# Tab 1 UI
# Create a password for a new website or search for an existing password
canvas = Canvas(tab1, width=320, height=200, highlightthickness=0)
logo = PhotoImage(file="logo_resized.png")
canvas.create_image(160, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(tab1, text="Website:", font=("Stencil Std", 12, "normal"))
website_label.grid(column=0, row=1, sticky="W")
website_entry = Entry(tab1, width=35)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

user_label = Label(tab1, text="Email/Username:", font=("Stencil Std", 12, "normal"))
user_label.grid(column=0, row=2, sticky="W")
user_entry = Entry(tab1, width=35)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(0, "test@mail.com") # use END to insert text at the end of an existing string value

pw_label = Label(tab1, text="Password:", font=("Stencil Std", 12, "normal"))
pw_label.grid(column=0, row=3, sticky="W")
pw_entry = Entry(tab1, width=17)
pw_entry.grid(column=1, row=3, sticky="EW")

generate_pw = Button(tab1, text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3, sticky="EW")

add_btn = Button(tab1, text="Add", command=save)
add_btn.grid(column=1,row=4, columnspan=2, sticky="EW")

search_btn = Button(tab1, text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")


# Tab 2 UI
# Display stored data
stored_data_text = Text(tab2, width=60, height=20)
stored_data_text.grid(column=0, row=0)
display_btn = Button(tab2, text="Refresh Data", command=display_stored_data)
display_btn.grid(column=0, row=1)

window.mainloop()