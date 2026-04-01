from tkinter import*
import random

def quit():
    main_window.destroy

def entry_print():
    Label(main_window,text= entry_full_name.get()).grid(column=0,row=6,sticky=E)
    Label(main_window,text=entry_Receipt_number.get()).grid(column=1,row=6)
    Label(main_window,text=entry_item_hired.get()).grid(column=2,row=6)
    Label(main_window,text=entry_number_hired.get()).grid(column=3,row=6)


def main():
    Button(main_window, text="Quit",command= quit) .grid(column=0,row=1)
    Button(main_window, text="Print",command=entry_print).grid(column=1,row=1)
    Label(main_window,text="Customer Name").grid(column=0,row=2)
    Label(main_window,text="Receipt Number").grid(column=0,row=3)
    Label(main_window,text="Item Hired").grid(column=0,row=4)
    Label(main_window,text="Number Hired").grid(column=0,row=5)
    main_window.mainloop()

main_window =Tk()
entry_full_name= Entry(main_window)
entry_full_name.grid(column=2,row=2,padx=10,pady=5)

main()