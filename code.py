from tkinter import*
import random

def quit():
    main_window.destroy

def entry_print():
    Label(main_window,text= entry_full_name.get()).grid(column=0,row=2,sticky=E)

def generate_random():
    random_number = random.randint(1,10)
    Label(main_window,text=random_number).grid(column=0,row=2, sticky=E)

def main():
    Button(main_window, text="Quit",command= quit) .grid(column=0,row=1)
    Button(main_window, text="Print",command=entry_print).grid(column=1,row=1)
    Label(main_window,text="Full Name").grid(column=0,row=2)
    main_window.mainloop()