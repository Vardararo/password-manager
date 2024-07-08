from tkinter import *
# from tkinter import messagebox, ttk
import random
import pyperclip
import json
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image


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
        #messagebox.showerror(title="Error", message="Please don't leave empty fields!") - tkinter messagebox
        CTkMessagebox(title="Warning", message="Please don't leave empty fields!", icon="warning") # CTk messagebox
    
    # Review inserted data before saving to a file
    else:
        details = CTkMessagebox(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?", icon="question", 
                                                      option_1="Cancel", option_2="Yes")
        response = details.get()
        
        # Save input data to the vault (json file)
        if response == "Yes":
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
        
        # Cancel if the data is incorrect
        else:
            details.destroy()

# Find a password for given website
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        CTkMessagebox(title="Error", message="No data file found!", icon="cancel")
    
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            CTkMessagebox(title=website, message=f"Email: {email}\nPassword: {password}", icon="info")
            pyperclip.copy(password) # Automatically copies the password of searched website
        else:
            CTkMessagebox(title="Error", message=f"No details exist for {website}!", icon="cancel")

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


# CTk UI setup
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

window = ctk.CTk()
window.minsize(580, 500)
window.title("Password Manager")

window.grid_rowconfigure((0 , 1, 2, 3, 4), weight=1)
window.grid_columnconfigure((0, 1, 2), weight=1)

# Create the separate tabs for managing and storing data
tabview = ctk.CTkTabview(master=window)
tabview.pack(padx=60, pady=20, fill="both", expand=True)

tab_1 = tabview.add("Manager")
tab_2 = tabview.add("Vault")

# Tab 1 UI
# Insert new data and search for stored passwords
logo = ctk.CTkImage(dark_image=Image.open("logo_resized.png"),
                                  size=(350, 300))
image_label = ctk.CTkLabel(tab_1, image=logo, text="")
image_label.grid(column=0, row=0, columnspan=3)

website_label = ctk.CTkLabel(tab_1, text="Website:", font=("Stencil Std", 12, "normal"))
website_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
website_entry = ctk.CTkEntry(master=tab_1, width=250)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

user_label = ctk.CTkLabel(tab_1, text="Email/Username:", font=("Stencil Std", 12, "normal"))
user_label.grid(column=0, row=2, sticky="W", padx=5, pady=5)
user_entry = ctk.CTkEntry(tab_1, width=35, placeholder_text="your@mail.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
#user_entry.insert(0, "test@mail.com") # use this instead of placeholder_text if the email is always the same

pw_label = ctk.CTkLabel(tab_1, text="Password:", font=("Stencil Std", 12, "normal"))
pw_label.grid(column=0, row=3, sticky="W", padx=5, pady=5)
pw_entry = ctk.CTkEntry(tab_1, width=17)
pw_entry.grid(column=1, row=3, sticky="EW")

generate_pw = ctk.CTkButton(tab_1, text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3, sticky="EW")

add_btn = ctk.CTkButton(tab_1, text="Add", command=save)
add_btn.grid(column=1,row=4, columnspan=2, sticky="EW", pady=5)

search_btn = ctk.CTkButton(tab_1, text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")

# Tab 2 UI
# Display stored data
stored_data_text = ctk.CTkTextbox(tab_2, width=490, height=422, font=("Stencil Std", 16, "normal"))
stored_data_text.grid(column=0, row=0)
display_btn = ctk.CTkButton(tab_2, text="Refresh Data", command=display_stored_data)
display_btn.grid(column=0, row=1)

window.mainloop()