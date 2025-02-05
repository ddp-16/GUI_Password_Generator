import random
import tkinter as tk
from tkinter import messagebox

# Original Password Character Set
Pass = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890abcdefghijklmnopqrstuvwxyz@#₹_&-+()/*\"':;!?$¢©%[]"

# Function to generate password
def generate_password():
    try:
        Len = int(entry_length.get())  # Get user input for password length
        if Len < 1:
            messagebox.showerror("Error", "Length must be greater than 0")
            return
        a = "".join(random.sample(Pass, Len))  # Generate password
        password_label.config(text=f"Your Password: {a}")  # Display password
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Creating main GUI window
root = tk.Tk()
root.title("Password Generator")  # Title of window
root.geometry("400x250")  # Window size
root.config(bg="black")  # Background color

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 14, "bold"), fg="orange", bg="black")
title_label.pack(pady=10)

# Frame for Entry Box and Label
frame = tk.Frame(root, bg="black")
frame.pack(pady=5)

length_label = tk.Label(frame, text="Length of Password:", font=("Arial", 12), fg="orange", bg="black")
length_label.pack(side=tk.LEFT, padx=5)

entry_length = tk.Entry(frame, font=("Arial", 12), width=5, fg="black", bg="orange")
entry_length.pack(side=tk.LEFT)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), fg="black", bg="orange", command=generate_password)
generate_button.pack(pady=10)

# Password Display Label
password_label = tk.Label(root, text="Your Password: ", font=("Arial", 12, "bold"), fg="orange", bg="black")
password_label.pack(pady=10)

# Run the GUI Application
root.mainloop()
