import tkinter as tk
from tkinter import font

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x450")
        self.root.configure(bg="#f0f0f0")  # Background color

        self.result_var = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        entry_font = font.Font(family="Helvetica", size=18, weight="bold")
        button_font = font.Font(family="Helvetica", size=14, weight="bold")

        entry = tk.Entry(self.root, textvariable=self.result_var, font=entry_font, bd=15, insertwidth=4, width=20, justify="right")
        entry.grid(row=0, column=0, columnspan=4, pady=(30, 0))  # Added vertical padding
        entry.config(bg="#333333", fg="#ffffff")  # Display box background and text color

        # Define button styles
        button_styles = {
            'bg': "#a0a0a0",           # Button background color
            'fg': "#ffffff",           # Button text color
            'activebackground': "#606060",  # Button background color when pressed
            'activeforeground': "#ffffff",  # Button text color when pressed
            'font': button_font,
            'padx': 20,
            'pady': 20,
            'bd': 0,
            'relief': "flat"          # No button border
        }

        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in button_texts:
            button_bg_color = "#4CAF50" if text.isdigit() else "#FF5733"  # Different colors for digits and operators
            button_styles['bg'] = button_bg_color
            button = tk.Button(self.root, text=text, command=lambda t=text: self.button_click(t), **button_styles)
            button.grid(row=row, column=col, padx=5, pady=5)  # Added horizontal and vertical padding
            button.bind("<Button-1>", lambda event, b=button: self.animate_button(b))

    def button_click(self, number):
        current = self.result_var.get()
        if number == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif number == 'C':
            self.result_var.set('')
        else:
            self.result_var.set(current + str(number))

    def animate_button(self, button):
        button.config(relief=tk.SUNKEN)
        self.root.after(100, lambda: button.config(relief=tk.RAISED))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)

#Parent window's background color:
root.configure(background = 'yellow');

root.mainloop()
