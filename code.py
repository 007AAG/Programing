from tkinter import*
import random

def quit():
    main_window.destroy


def entry_print():
    Label(main_window,text= entry_full_name.get()).grid(column=0,row=6,sticky=E)
    Label(main_window,text=entry_receipt_number.get()).grid(column=1,row=6)
    Label(main_window,text=entry_item_hired.get()).grid(column=2,row=6)
    Label(main_window,text=entry_number_hired.get()).grid(column=3,row=6)

def append_name ():
    if len(entry_name.get()) != 0 :
        j_names.append(entry_name.get())
        number['total_entries'] += 1

def generate_random():
    random_number = random.randint(1,10)
    Label(main_window,text=random_number).grid(column=0,row=2, sticky=E)


def main():
    Button(main_window, text="Append Details",command=append_name).grid(column=3,row=1)
    Button(main_window, text="Quit",command= quit) .grid(column=5,row=1)
    Button(main_window, text="Print Details",command=entry_print).grid(column=4,row=1)
    Label(main_window,text="Customer Name").grid(column=0,row=2)
    Label(main_window,text="Receipt Number").grid(column=0,row=3)
    Label(main_window,text="Item Hired").grid(column=0,row=4)
    Label(main_window,text="Number Hired").grid(column=0,row=5)
    Label(main_window,font='bold',text="Row").grid(column=0,row=6)
    Label(main_window,font='bold',text="Customer Name").grid(column=1,row=6)
    Label(main_window,font='bold',text="Receipt Number").grid(column=2,row=6)
    Label(main_window,font='bold',text="Hire Item").grid(column=3,row=6,padx=10)
    Label(main_window,font='bold',text="Number Hired").grid(column=4,row=6,padx=15)
    Label(main_window,text="Row ").grid(column=4,row=2)
    main_window.mainloop()

main_window =Tk()
entry_full_name= Entry(main_window)
entry_full_name.grid(column=2,row=2,padx=10,pady=5)
entry_receipt_number = Entry(main_window)
entry_receipt_number.grid(column=2,row=3,padx=10,pady=5)
entry_item_hired = Entry(main_window)
entry_item_hired.grid(column=2,row=4,padx=10,pady=5)
entry_number_hired = Entry(main_window)
entry_number_hired.grid(column=2,row=5,padx=10,pady=5)
main()