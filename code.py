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
