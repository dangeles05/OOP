from tkinter import *
from tkinter import ttk

def mensaje(*args):
    message.set(f'Fila: {row}, Columna; {column}')

root = Tk()
root.title("Botón")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

message = StringVar()

ttk.Button(mainframe, text="Mensaje1", command=lambda: mensaje(1,1)).grid(column=1, row=1, sticky=(E, N))
ttk.Button(mainframe, text="Mensaje2", command=lambda: mensaje(1,2)).grid(column=1, row=2, sticky=(N))
ttk.Button(mainframe, text="Mensaje3", command=lambda: mensaje(1,3)).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Mensaje4", command=lambda: mensaje(2,1)).grid(column=2, row=1, sticky=(W))
ttk.Button(mainframe, text="Mensaje5", command=lambda: mensaje(2,2)).grid(column=2, row=2, sticky=(W, N))
ttk.Button(mainframe, text="Mensaje6", command=lambda: mensaje(2,3)).grid(column=2, row=3, sticky=(E))
ttk.Button(mainframe, text="Mensaje7", command=lambda: mensaje(3,1)).grid(column=3, row=1, sticky=(S, W))
ttk.Button(mainframe, text="Mensaje8", command=lambda: mensaje(3,2)).grid(column=3, row=2, sticky=(S))
ttk.Button(mainframe, text="Mensaje9", command=lambda: mensaje(3,3)).grid(column=3, row=3, sticky=(S, E))

ttk.Label(mainframe, textvariable=message).grid(column=2, row=2, sticky=(E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", mensaje)

root.mainloop()