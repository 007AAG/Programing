from tkinter import *

def quit():
    main_window.destroy()

def entry_print():
    Label(main_window,text= entry_first_name.get()).grid(column=0,row=3,sticky=E)
    Label(main)