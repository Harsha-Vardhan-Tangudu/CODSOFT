import tkinter as tk
from tkinter import messagebox

class MagicalCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🔮 EnigmaCalc: The Mystical Calculator 🔮")
        self.geometry("500x650")
        self.configure(bg="#0E121B")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter two numbers and choose an operation:", bg="#0E121B", fg="#C0D3D9", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        self.num1_entry = tk.Entry(self, font=("Arial", 12), bg="#1A2130", fg="#C0D3D9")
        self.num1_entry.pack(padx=20, pady=5, fill=tk.BOTH, ipadx=10, ipady=5)

        self.num2_entry = tk.Entry(self, font=("Arial", 12), bg="#1A2130", fg="#C0D3D9")
        self.num2_entry.pack(padx=20, pady=5, fill=tk.BOTH, ipadx=10, ipady=5)

        self.operation_var = tk.StringVar(self)
        self.operation_var.set("➕")
        operations = ["➕", "➖", "✖️", "➗"]
        self.operation_menu = tk.OptionMenu(self, self.operation_var, *operations)
        self.operation_menu.config(font=("Arial", 12), bg="#1A2130", fg="#C0D3D9")
        self.operation_menu.pack(pady=10)

        calculate_button = tk.Button(self, text="Calculate", command=self.calculate, bg="#346751", fg="white", font=("Arial", 12, "bold"))
        calculate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#0E121B", fg="#FFA33D", font=("Arial", 18, "bold"))
        self.result_label.pack(pady=20)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "➕":
                result = num1 + num2
            elif operation == "➖":
                result = num1 - num2
            elif operation == "✖️":
                result = num1 * num2
            elif operation == "➗":
                result = num1 / num2

            self.result_label.config(text=f"🔮 Result: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    app = MagicalCalculatorApp()
    app.mainloop()
