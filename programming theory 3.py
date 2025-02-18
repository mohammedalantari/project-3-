import tkinter as tk
from tkinter import messagebox
import math

# Allowed functions
allowed_functions = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "sqrt": math.sqrt
}

def safe_eval(expression):
    """Evaluates a mathematical expression safely."""
    try:
        # Replace function calls for eval compatibility
        for func in allowed_functions.keys():
            expression = expression.replace(f"{func}(", f"allowed_functions['{func}'](")
        
        result = eval(expression, {"__builtins__": None}, {"allowed_functions": allowed_functions, "math": math})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")
        return ""

def on_click(button_text):
    """Handles button clicks and updates the entry field."""
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        expression = entry_var.get()
        result = safe_eval(expression)
        if result != "":
            history_text.config(state=tk.NORMAL)  # Enable editing to insert
            history_text.insert(tk.END, f"{expression} = {result}\n")
            history_text.see(tk.END)
            history_text.config(state=tk.DISABLED)  # Disable editing after insert
        entry_var.set(result)
    else:
        # Auto-close function parentheses for better usability
        if button_text in ["sin(", "cos(", "tan(", "sqrt("]:
            entry_var.set(entry_var.get() + button_text + ")")
        else:
            entry_var.set(entry_var.get() + button_text)

# GUI setup
root = tk.Tk()
root.title("Calculator")

# Entry widget for input
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('sin(', 'cos(', 'tan(', 'sqrt('),
    ('=', '', '', '')
]

# Creating buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text:
            tk.Button(root, text=text, font=("Arial", 14), padx=20, pady=20, 
                      command=lambda t=text: on_click(t)).grid(row=i+1, column=j, sticky="nsew")

# Make the buttons expand with the window size
for i in range(len(buttons) + 2):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# History display
history_label = tk.Label(root, text="History:", font=("Arial", 12))
history_label.grid(row=len(buttons)+1, column=0, columnspan=4, sticky='w')

history_text = tk.Text(root, height=5, width=30, font=("Arial", 12), state=tk.DISABLED)
history_text.grid(row=len(buttons)+2, column=0, columnspan=4, sticky="nsew")

root.mainloop()
