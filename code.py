from tkinter import *

def quit_app():
    main_window.destroy()

def entry_print():
    global hire_details, total_entries

    hire_details.append([
        entry_full_name.get(),
        entry_receipt_number.get(),
        entry_items_hired.get(),
        entry_number_hired.get(),
        entry_date_hired.get(),
        entry_date_return.get(),
    ])
    total_entries += 1