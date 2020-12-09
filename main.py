# main

from tkinter import *
from tkinter import messagebox
from project_mathematics import quadratic_eqiation, compute_function

FONT = ('Arial', 20, 'bold ')


def quit_program():
    status_bar.config(text='Zamykanie programu...')
    answer = messagebox.askyesno("Podejmij decyzję", "Czy zakończyć program?")
    if answer:
        root.destroy()
    else:
        status_bar.config(text='Gotowy...')


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
        status_bar.config(text='Obliczono pierwiastki...')
    else:
        result_lbl.config(text='---')
        status_bar.config(text='Błąd...')


def draw_axis():
    cv.delete("all")
    # rysujemy osie
    cv.create_line(400, 0, 400, 600)
    for i in range(6):
        cv.create_line(400, i*100, 410, i*100)
    cv.create_text(430, 200, text="1", font=FONT)

    cv.create_line(0, 300, 800, 300)
    for i in range(16):
        cv.create_line(i*100, 300, i*100, 290)
    cv.create_text(500, 270, text="1", font=FONT)


def draw():
    draw_axis()

    xc = []
    yc = []
    # pobieranie a, b, c
    result = get_a_b_c()
    if result is not None:
        # liczenie
        a = result[0]
        b = result[1]
        c = result[2]
        xx, yy = compute_function(a, b, c, -4, 4, 0.1)

        for x in xx:
            xc.append(100*x + 400)
        for y in yy:
            yc.append(-y*100 + 300)

        n = int(len(xc))
        for i in range(n-1):
            cv.create_line(xc[i], yc[i], xc[i+1], yc[i+1], fill="royal blue", width=3)
        status_bar.config(text='Narysowano wykres...')
    else:
        status_bar.config(text='Błąd...')


root = Tk()
root.title('Rozwiązywanie równania kwadratowego')

# na samej górze będzie kolejna ramka, która będzie zawierała narzędzia w programie
toolbar = Frame(root)
toolbar.pack(side=TOP, fill=BOTH)
toolbar.config(bg='tan1')

# przycisk, który będzie zamykać program
stop_btn = Button(toolbar, text="Stop", fg='red', command=quit_program)
stop_btn.pack(side=LEFT)

calcul_btn = Button(toolbar, text="Rozwiąż równanie", command=calcul)
calcul_btn.pack(side=LEFT)

draw_btn = Button(toolbar, text="Rysuj wykres", command=draw)
draw_btn.pack(side=LEFT)

mainframe = Frame(root)
mainframe.pack(side=TOP)

# a, b, c Entry
leftbar = Frame(mainframe)
leftbar.pack(side=LEFT)
leftbar.config(bg='tan1')

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
result_lbl = Label(mainframe, text="Jeszcze nie policzono pierwiastków...")
result_lbl.pack(side=TOP)

cv = Canvas(mainframe, width=800, height=600, bg="MediumOrchid3")
cv.pack(side=TOP)
draw_axis()

status_bar = Label(root, text='Gotowy...', bg="hot pink")
status_bar.pack(side=TOP, anchor=W, fill=BOTH)

mainloop()
