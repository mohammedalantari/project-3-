# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:31:39 2025

@author: ashby
"""

import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.entry_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        """Creates the calculator UI."""
        entry = tk.Entry(self.root, textvariable=self.entry_var, font=("Arial", 18), justify="right")
        entry.grid(row=0, column=1, columnspan=3, sticky="nsew")
        
        clear_btn = tk.Button(self.root, text = 'C', font=("Arial", 15), width=8, height=2, command=lambda t = 'C': self.on_button_click(t))
        clear_btn.grid(row=0, column=0, columnspan=1)
        
        buttons = [
            ['^', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['.', '0', '=', 'sqrt('],
            ['log(', 'log10(', 'sin(', 'cos('],
            ['tan(', 'arcsin(', 'arccos(', 'arctan('],
        ]

        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                tk.Button(
                    self.root, text=text, font=("Arial", 14), width=8, height=2,
                    command=lambda t=text: self.on_button_click(t)
                ).grid(row=i+1, column=j, sticky="nsew")

        for i in range(len(buttons) + 1):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

        self.history_text = tk.Text(self.root, height=10, width=40, font=("Arial", 12), state=tk.DISABLED)
        self.history_text.grid(row=len(buttons) + 1, column=0, columnspan=4, sticky="nsew")
    
    def evaluate_expression(self, expression):
        """Evaluates the given mathematical expression safely."""
        try:
            expression = expression.replace("^", "**")
            safe_functions = {
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
                "arcsin": math.asin, "arccos": math.acos, "arctan": math.atan
            }
            result = eval(expression, {"__builtins__": None}, safe_functions)
            return result
        except Exception:
            return "Error"
    
    def on_button_click(self, value):
        """Handles button clicks."""
        if value == "C":
            self.entry_var.set("")
        elif value == "=":
            result = self.evaluate_expression(self.entry_var.get())
            self.update_history(self.entry_var.get(), result)
            self.entry_var.set(result)
        else:
            self.entry_var.set(self.entry_var.get() + value)
    
    def update_history(self, expression, result):
        """Updates calculation history."""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, f"{expression} = {result}\n")
        self.history_text.see(tk.END)
        self.history_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
