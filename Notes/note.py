from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from datetime import datetime

current_datetime = datetime.now()

def new_file():
    global file_name
    text.delete('1.0', END)

def save_note():
    out = asksaveasfile(mode='w', defaultextension='.scv')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Error")

def open_note():
    global file_name
    inp = askopenfile(mode='r')
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = Tk()
root.title('Note')
root.geometry('500x500')

text= Text(root, width=500, height=500)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_note)
file_menu.add_command(label="Save As", command=save_note)

menu_bar.add_cascade(label = "Файл", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()