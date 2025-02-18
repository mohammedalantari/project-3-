# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:43:13 2025

@author: ashby
"""


import tkinter as tk

#setting up the window with a title and size
root = tk.Tk()
root.title("Claculator")
root.geometry("488x600")

#adding a history button at the top left corner    
history_button = tk.Button(root, text = "H", width = 16, height = 5)
history_button.grid(row = 0, column = 0)

equation_text = ""

#adding a label to display user inputs
equation_label = tk.Label(root, text = equation_text, width = 51, height = 5)
equation_label.grid(row = 0, column = 1, columnspan = 3)

#list of text for each button
button = ["C","(", ")", "+",
          "7", "8", "9","-",
          "4", "5", "6", "x",
          "1","2", "3", "%",
          ".", "0", "=","square",
          "square root", "sin", "cos", "tan"]

#creating a loop to add each button
for index, label in enumerate(button):
    #starting with row 2 and column 0, dividing indexes by 4 to determine placement of button
    btn_row = index // 4 + 2
    btn_column = index % 4
    #adding the button based on above results
    calc_btn=tk.Button(root, text = label, width = 16, height = 5) #, command=lambda symbol = label: button_press(equation_text))
    calc_btn.grid(row = btn_row, column = btn_column)

root.mainloop()


    

