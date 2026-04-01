from tkinter import *
from tkinter import messagebox

hire_details = []
total_entries = 0

def quit_app():
    main_window.destroy()

def append_name():
    global hire_details, total_entries

    name = entry_full_name.get()
    receipt = entry_receipt_number.get()
    item = entry_items_hired.get()
    quantity = entry_number_hired.get()
    date_hired = entry_date_hired.get()
    return_date = entry_date_return.get() 

def clear_fields():
    entry_full_name.delete(0, END)
    entry_receipt_number.delete(0, END)
    entry_items_hired.delete(0, END)
    entry_number_hired.delete(0, END)
    entry_date_hired.delete(0, END)
    entry_date_return.delete(0, END)

def delete_row():
    global hire_details, total_entries

    try:
        row = int(entry_row.get())
        hire_details.pop(row)
        total_entries -= 1
        refresh_table()
    except:
        messagebox.showerror("Error", "Invalid row number")

def refresh_table():
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) > 8:
            widget.destroy()

    for i, data in enumerate(hire_details):
        Label(main_window, text=i).grid(column=0, row=i+9)
        for j, value in enumerate(data):
            Label(main_window, text=value).grid(column=j+1, row=i+9)

