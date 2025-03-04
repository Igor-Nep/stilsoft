import subprocess
from tkinter import *
from tkinter import ttk
from threading import Timer
import os

def repeater(interval, function):
    Timer(interval, repeater, [interval, function]).start()
    function()

def selected(event):
   selection = combobox.get()
   with open('c:/windows/system32/drivers/etc/hosts', 'w') as file:
      file.write(selection)
   window.title(selection)
   ch_host = selection[:15].strip()
   print(ch_host)

def click_ref():
   subprocess.call('c:/windows/dis.bat', shell=True)
   #os.remove('c:/windows/system32/drivers/etc/hosts')
   host_file = open('c:/work/hosts','r')
   host_file = open('c:/windows/system32/drivers/etc/hosts', 'r')
   active_host=[]
   len_host = int(len(host_file.readlines()))
   host_file.seek(0,0)
   for _ in range(0, len_host):
      s = host_file.readline()
      if '#' not in s:
         active_host.append(s)
   newti=str(active_host[0])
   window.title(newti)   
   host_file.close()   

window = Tk()
window.title("Active host")
window.attributes("-topmost",True)
window.attributes('-toolwindow', True)
window.geometry('210x0')

hosts = []
with open('c:/windows/appr_hosts', 'r') as file:
   for line in file:
      hosts.append(line )


combobox = ttk.Combobox(values=hosts, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)

repeater(5, click_ref)

window.mainloop()