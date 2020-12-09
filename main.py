# main

from tkinter import *
from tkinter import messagebox

def quit_program():
    answer = messagebox.askyesno("Podejmij decyzję", "Czy zakończyć program?")
    if answer:
        root.destroy()


root = Tk()
root.title('Rozwiązywanie równania kwadratowego')

# na samej górze będzie kolejna ramka, która będzie zawierała narzędzia w programie
toolbar = Frame(root)
toolbar.pack(side=TOP, fill=BOTH)

# przycisk, który będzie zamykać program
stop_btn = Button(toolbar, text="Stop", fg='red', command=quit_program)
stop_btn.pack(side=LEFT)

# a, b, c Entry
leftbar = Frame(root)
leftbar.pack(side=LEFT)

Label(leftbar, text="a").grid(row=0, column=0)
a_entry = Entry(leftbar, width=10)
a_entry.insert(0, str(1.0))
a_entry.grid(row=0, column=1)

Label(leftbar, text="b").grid(row=1, column=0)
b_entry = Entry(leftbar, width=10)
b_entry.insert(0, str(0.0))
b_entry.grid(row=1, column=1)

Label(leftbar, text="c").grid(row=2, column=0)
c_entry = Entry(leftbar, width=10)
c_entry.insert(0, str(-2.0))
c_entry.grid(row=2, column=1)

mainloop()