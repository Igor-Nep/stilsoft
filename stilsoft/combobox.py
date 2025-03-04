import paramiko
from time import sleep
from tkinter import *
from tkinter import ttk
ch_host = ''
root = Tk()
root.title("/hosts")

root.geometry("250x200")

def selected(event):
  
    selection = combobox.get()
    with open('c:/windows/system32/drivers/etc/hosts', 'w') as file:
        file.write(selection)
    root.title(selection)
    ch_host = selection[:15].strip()
    print(ch_host)
 
languages = ['192.168.202.82 gate.synerget.ru', '192.168.202.10 gate.synerget.ru', '192.168.202.161 gate.synerget.ru', '192.168.202.30 gate.synerget.ru', '192.168.202.18 gate.synerget.ru', '192.168.202.238 gate.synerget.ru']
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)
 
combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)
 
root.mainloop()