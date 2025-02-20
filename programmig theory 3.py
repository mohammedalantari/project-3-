# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:31:39 2025

@author: ashby
"""

import tkinter as tk  # Importing Tkinter for GUI
import math    # Importing math module for mathematical functions

# Function to evaluate mathematical expressions safely
def evaluate_expression(expression):
    """Evaluates a mathematical expression entered by the user."""
    try:
        expression = expression.replace("^", "**")  # Allow '^' for exponentiation
        
        # Define allowed mathematical functions
        safe_functions = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "sqrt": math.sqrt, "log": math.log, "log10": math.log10, "arcsin": math.asin, "arccos": math.acos, "arctan": math.atan
        }
        
        result = eval(expression, {"__builtins__": None}, safe_functions)  # Safely evaluate
        return result
    except Exception:
        return "Error"

# Function to handle button clicks
def on_button_click(value):
    """Handles user input from button clicks."""
    if value == "C":
        entry_var.set("")  # Clear the input field
    elif value == "=":
        entry_var.set(evaluate_expression(entry_var.get()))  # Compute result
    else:
        entry_var.set(entry_var.get() + value)  # Append input to entry field

# Function to update calculation history
def update_history(expression, result):
    """Logs past calculations for user reference."""
    history_text.config(state=tk.NORMAL)
    history_text.insert(tk.END, f"{expression} = {result}\n")
    history_text.see(tk.END)
    history_text.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display user input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['sin(', 'cos(', 'tan(', 'sqrt('],  # Scientific function buttons
    ['log(', 'log10(', '^', 'arcsin('],  # Power button '^'
    ['=','(',')', 'arccos('],# Equals button and parentheses
    ['arctan(']
]

# Create buttons dynamically
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        tk.Button(
            root, text=text, font=("Arial", 14), width=5, height=2,
            command=lambda t=text: on_button_click(t)
        ).grid(row=i+1, column=j, sticky="nsew")

# Enable window resizing
for i in range(len(buttons)+1):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Create a history display area
history_text = tk.Text(root, height=10, width=40, font=("Arial", 12), state=tk.DISABLED)
history_text.grid(row=len(buttons)+1, column=0, columnspan=4, sticky="nsew")

# Run the application
root.mainloop()