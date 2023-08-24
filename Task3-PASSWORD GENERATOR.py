import tkinter as tk
from tkinter import messagebox
import random
import string

class EnchantedPasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🔒 EnigmaPass: The Enchanted Password Generator 🔒")
        self.geometry("400x300")
        self.configure(bg="#0E121B")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Specify the desired password length:", bg="#0E121B", fg="#C0D3D9", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        self.length_entry = tk.Entry(self, font=("Arial", 12), bg="#1A2130", fg="#C0D3D9")
        self.length_entry.pack(padx=20, pady=5, fill=tk.BOTH, ipadx=10, ipady=5)

        generate_button = tk.Button(self, text="Generate Password", command=self.generate_password, bg="#346751", fg="white", font=("Arial", 12, "bold"))
        generate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#0E121B", fg="#FFA33D", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a valid length.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            self.result_label.config(text=f"🔐 Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    app = EnchantedPasswordGenerator()
    app.mainloop()
