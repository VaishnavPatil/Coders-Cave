import tkinter as tk

def on_click(button_value):
    current_text = entry_var.get()
    new_text = current_text + str(button_value)
    entry_var.set(new_text)

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception as e:
        entry_var.set("Error")

window = tk.Tk()
window.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2,
              command=lambda button=button: on_click(button) if button != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(window, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

window.mainloop()
