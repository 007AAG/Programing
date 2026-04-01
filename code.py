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

    hire_details.append([name, receipt, item, quantity, date_hired, return_date])
    total_entries += 1

    entry_full_name.delete(0, END)
    entry_receipt_number.delete(0, END)
    entry_items_hired.delete(0, END)
    entry_number_hired.delete(0, END)
    entry_date_hired.delete(0, END)
    entry_date_return.delete(0, END)


def entry_print():
    refresh_table()

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

def setup_buttons():
    global entry_full_name, entry_receipt_number, entry_items_hired
    global entry_number_hired, entry_row, entry_date_hired, entry_date_return

    Label(main_window, text="Customer Name").grid(column=0, row=2)
    entry_full_name = Entry(main_window)
    entry_full_name.grid(column=2, row=2)

    Label(main_window, text="Receipt Number").grid(column=0, row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=2, row=3)

    Label(main_window, text="Items Hired").grid(column=0, row=4)
    entry_items_hired = Entry(main_window)
    entry_items_hired.grid(column=2, row=4)

    Label(main_window, text="Number Hired").grid(column=0, row=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=2, row=5)

    Label(main_window, text="Date Hired").grid(column=0, row=6)
    entry_date_hired = Entry(main_window)
    entry_date_hired.grid(column=2, row=6)

    Label(main_window, text="Return Date").grid(column=0, row=7)
    entry_date_return = Entry(main_window)
    entry_date_return.grid(column=2, row=7)

    Label(main_window, text="Row ").grid(column=4, row=2)
    entry_row = Entry(main_window)
    entry_row.grid(column=5, row=2)

    Button(main_window, text="Print", command=entry_print).grid(column=0, row=0)
    Button(main_window, text="Append Details", command=append_name).grid(column=1, row=0)
    Button(main_window, text="Delete Row", command=delete_row).grid(column=5, row=3)
    Button(main_window, text="Quit", command=quit_app).grid(column=7, row=7)

    headers = ["Row", "Customer Name", "Receipt", "Item", "Qty", "Hired", "Return"]
    for i, h in enumerate(headers):
        Label(main_window, text=h, font='bold').grid(column=i, row=8)

def main():
    global main_window

    main_window = Tk()
    main_window.title("Hire System")

    setup_buttons()

    main_window.mainloop()

main()