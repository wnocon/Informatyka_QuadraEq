# main

from tkinter import *
from tkinter import messagebox

from project_mathematics import quadratic_eqiation


def quit_program():
    answer = messagebox.askyesno("Podejmij decyzję", "Czy zakończyć program?")
    if answer:
        root.destroy()

def get_a_b_c():
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        # print('a = ', a, 'b = ', b, 'c = ', c)
    except ValueError:
        messagebox.showerror("Błąd",
                             "Nie możba konwertować wpisanych wartości do liczb. Popraw proszę swoje zachowanie")
        return None
    return [a, b, c]

def calcul():
    result = get_a_b_c()
    if result is not None:
        a = result[0]
        b = result[1]
        c = result[2]
        result = quadratic_eqiation(a, b, c)
        if len(result) == 0:
            s = "Brak rozwiązań"
        elif len(result) == 1:
            s = "x0 = %+10.3f" % result[0]
        else:
            s = "x01 = %+10.3f    x02 = %+10.3f" % (result[0], result[1])
        result_lbl.config(text=s)
    else:
        result_lbl.config(text='---')

root = Tk()
root.title('Rozwiązywanie równania kwadratowego')

# na samej górze będzie kolejna ramka, która będzie zawierała narzędzia w programie
toolbar = Frame(root)
toolbar.pack(side=TOP, fill=BOTH)

# przycisk, który będzie zamykać program
stop_btn = Button(toolbar, text="Stop", fg='red', command=quit_program)
stop_btn.pack(side=LEFT)

calcul_btn = Button(toolbar, text="Rozwiąż równanie", command=calcul)
calcul_btn.pack(side=LEFT)

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

# tekst wyniku
result_lbl = Label(root, text="Jeszcze nie policzono pierwiastków...")
result_lbl.pack(side=TOP)

mainloop()