import json
from tkinter import *
from tkinter import messagebox
import pyperclip
#---------------------------- PASSWORD GENERATOR -------------------------------
import random

EMAIL = 'your_email@email.com'

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    letter = [random.choice(letters) for _ in range(nr_letters)]
    number = [random.choice(numbers) for _ in range(nr_numbers)]
    symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letter + number + symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Don't left empty space")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)

def Search():
    website = entry1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    else:
        if website in data:
            em = data[f"{website}"]["email"]
            passw = data[f"{website}"]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Your email is {em}\n"
                                f"and your password is {passw}")
        else:
            messagebox.showinfo(title="error", message="no details for this data")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(sticky= W, column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(sticky= W, column=0, row=2)

label3 = Label(text="Password:")
label3.grid(sticky=W , column=0, row=3)

button1 = Button()
button1.config(text="Add", width= 46, command= save)
button1.grid(sticky= W, column=1, row=4, columnspan=2)

button2 = Button()
button2.config(text="Generate Password", justify=LEFT, command= generate_password)
button2.grid(sticky= E, column=2, row=3)

button3= Button()
button3.grid(sticky=E, column=2, row = 1)
button3.config(text="Search", justify=LEFT, width=14, command= Search)

entry1 = Entry(width= 36)
entry1.grid(sticky=W, column=1, row=1, columnspan=2)
entry1.focus()


entry2 = Entry(width= 54, justify=LEFT)
entry2.grid(sticky= W, column=1, row=2, columnspan=2)
entry2.insert(END, EMAIL)


entry3 = Entry(width= 36, justify=LEFT)
entry3.grid(sticky= W, column=1, row=3)

window.mainloop()
