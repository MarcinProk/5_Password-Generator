import random
import tkinter as tk
from tkinter import messagebox

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT=("Cascadia Code", 10)
GREEN = "#4db6ac"
BG_LABEL = "#A1EEBD"
YELLOW = "#F6F7C4"


# ------------------- GENERATE PASSWORD ----------------------------- #
def generate_password():
    passwords = int(pass_entry.get())
    letters = int(letters_entry.get())
    symbols = int(symbols_entry.get())
    numbers = int(numbers_entry.get())
    generated_passwords = []

    for n in range(1, passwords+1):
        hard_pass = (random.sample(LETTERS, letters)) + (random.sample(NUMBERS,numbers)) + (random.sample(SYMBOLS,symbols))
        shuffled_hard_pass = random.shuffle(hard_pass)
        hard_pass = ''.join(hard_pass)
        generated_passwords.append(hard_pass)
    
    listbox.delete(0, 'end')
    for password in generated_passwords:
        listbox.insert('end', password)
    # passwords_text = '\n'.join(generated_passwords)
    # messagebox.showinfo(title='Passwords: ', message=f"Here are your passwords:\n {passwords_text}")



# ------------------- UI ----------------------------- #
window = tk.Tk()
window.title('Password generator')
window.config(bg=GREEN, padx=50, pady=50)

canvas = tk.Canvas(width=450, height=220)
lock_png = tk.PhotoImage(file=R"C:\Users\marci\Desktop\Programowanie\KURSY\100_exercise\exercises\days 1-10\day5_password\images\lock2.png")
canvas.create_image(250,120, image=lock_png)
canvas.config(bg=GREEN, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2, sticky='w')

canvas.create_text(250, 15, text='Password Generator', font=('Cascadia Code', 20, 'bold'))

nr_passwords = tk.Label(text='How many passwords do you want to generate?', font=FONT)
nr_passwords.config(bg=GREEN)
nr_passwords.grid(column=0, row=1, padx=5, pady=5, sticky='w')

pass_entry = tk.Entry()
pass_entry.config(width=20, bg=YELLOW)
pass_entry.grid(column=1, row=1)

nr_letters = tk.Label(text='How many letters in your password?', font=FONT)
nr_letters.config(bg=GREEN)
nr_letters.grid(column=0, row=2,padx=5, pady=5, sticky='w')

letters_entry = tk.Entry()
letters_entry.config(width=20, bg=YELLOW)
letters_entry.grid(column=1, row=2,padx=5, pady=5, sticky='w')

nr_symbols = tk.Label(text='How many symbols in your password?', font=FONT)
nr_symbols.config(bg=GREEN)
nr_symbols.grid(column=0, row=3,padx=5, pady=5, sticky='w')

symbols_entry = tk.Entry()
symbols_entry.config(width=20, bg=YELLOW)
symbols_entry.grid(column=1, row=3,padx=5, pady=5, sticky='w')

nr_numbers = tk.Label(text='How many numbers in your password?', font=FONT)
nr_numbers.config(bg=GREEN)
nr_numbers.grid(column=0, row=4,padx=5, pady=5, sticky='w')

numbers_entry = tk.Entry()
numbers_entry.config(width=20, bg=YELLOW)
numbers_entry.grid(column=1, row=4,padx=5, pady=5, sticky='w')

generate_button = tk.Button(text="Generate!", font=FONT, bg=BG_LABEL, command=generate_password)
generate_button.grid(column=0, row=5, columnspan=2, pady=15)

listbox = tk.Listbox(height=6, width=40)
listbox.config(font=FONT)
listbox.grid(column=0, row=6, columnspan=2)

scrollbar = tk.Scrollbar(orient='vertical', command=listbox.yview)
scrollbar.grid(row=6, column=1, sticky='ns')
listbox. configure(yscrollcommand=scrollbar.set)

window.mainloop()
