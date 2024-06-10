import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        calculation = ""  # Reset calculation after evaluation
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Creating buttons
buttons = [
    ('1', 2, 1, 1), ('2', 2, 2, 1), ('3', 2, 3, 1),
    ('4', 3, 1, 1), ('5', 3, 2, 1), ('6', 3, 3, 1),
    ('7', 4, 1, 1), ('8', 4, 2, 1), ('9', 4, 3, 1),
    ('0', 5, 2, 1),
    ('+', 2, 4, 1), ('-', 3, 4, 1), ('*', 4, 4, 1), ('/', 5, 4, 1),
    ('(', 5, 1, 1), (')', 5, 3, 1),
    ('C', 6, 1, 2), ('=', 6, 3, 2)
]

for button_text, row, col, col_span in buttons:
    btn = tk.Button(root, text=button_text, width=5, font=("Arial", 14))
    btn.grid(row=row, column=col, columnspan=col_span)
    if button_text in ('C', '=', ''):
        if button_text == '=':
            btn.config(command=evaluate_calculation)
        elif button_text == 'C':
            btn.config(command=clear_field)
    else:
        btn.config(command=lambda b=button_text: add_to_calculation(b))

root.mainloop()
