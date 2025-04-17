import tkinter as tk


def greet(name):
    print(f"Привет, {name}!")

root = tk.Tk()
button = tk.Button(root, text="Поприветствовать", command=lambda: greet("Алиса"))
button.pack()

root.mainloop()