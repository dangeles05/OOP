from tkinter import *
from tkinter import ttk

def mensaje(*args):
    message.set("El botón fue presionado")

root = Tk()
root.title("Botón")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

message = StringVar()

ttk.Button(mainframe, text="Mensaje", command=mensaje).grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, textvariable=message).grid(column=2, row=2, sticky=(E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", mensaje)

root.mainloop()