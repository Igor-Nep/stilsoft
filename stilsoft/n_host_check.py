from tkinter import *
from threading import Timer

def repeat():
    Timer(5, repeat, [5, click_ref]).start()
    click_ref()

def click_ref():
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

repeat()

window.mainloop()