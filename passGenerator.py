# Small python program to generate strong passwords.

# Written in Python by Vivek Pancholi. 

# Visit https://vivekpancholi.com for more details.
 
import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *
from ctypes import windll


# Function for calculation of password 
def low(): 
	entry.delete(0, END)
    
	# Get the length of passowrd 
	length = var1.get() 

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 

	# if strength selected is low 
	if var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password 

	# if strength selected is medium 
	elif var.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 

	# if strength selected is strong 
	elif var.get() == 3: 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password 
	else: 
		print("Please choose an option") 


# Function for generation of password 
def generate(): 
	password1 = low() 
	entry.insert(10, password1) 


# Function for copying password to clipboard 
def copy1(): 
	random_password = entry.get() 
	pyperclip.copy(random_password) 


# Function for deleting generated password
def delete1():
    random_password = entry.delete(0, END)

# Main Function 

# create GUI window 
root = Tk() 
var = IntVar() 
var1 = IntVar() 

# Title of your GUI window 
root.title("Password Generator by Vivek Pancholi (https://vivekpancholi.com)") 

# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password Length") 
Random_password.grid(row=0) 

# create label for Strength of password

s_label = Label(root, text="Password Strength")
s_label.grid(row=2) 


# create label for length of password 
c_label = Label(root, text="Generated Password") 
c_label.grid(row=4) 

entry = Entry(root) 
entry.grid(row=4, column=1) 



# create Buttons Copy which will copy 
# password to clipboard and Generate 
# which will generate the password 

generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=6, column=0)

copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=6, column=1) 

delete_button = Button(root, text="Delete", command=delete1)
delete_button.grid(row=6, column=2) 

# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=2, column=1, sticky='E') 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=2, column=2, sticky='E') 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=2, column=3, sticky='E') 
combo = Combobox(root, textvariable=var1) 

# Combo Box for length of your password 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1) 

# start the GUI 
root.mainloop() 
