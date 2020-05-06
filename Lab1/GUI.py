from tkinter import *
import random, pickle
import Lab1.simpler_alg as s_alg
import Lab1.main_alg as m_alg
import Lab1.intersection as inters


def variant():
    G = 93
    N = 12
    M = "ІО"
    if M == "ІО": N += 2
    return str((N + G % 60) % 30 + 1)


def from_string_to_set(x):
    x = x.replace(',', ' ')
    x = x.replace(';', ' ')
    x = x.replace(':', ' ')
    x = x.replace('.', ' ')
    x = list(x.split(' '))
    for i in range(x.count('')):
        x.remove('')
    x = {int(i) for i in x}
    return x


def gener_vyp_set(l):
    if entU_do.get() == '':
        do = 0
    else:
        do = int(entU_do.get())

    if entU_vid.get() == '':
        vid = 0
    else:
        vid = int(entU_vid.get())

    s = set()
    for i in range(l):
        s.add(random.randint(vid, do))

    while len(s) < l:
        s.add(random.randint(vid, do))
    return s


def generABC():
    global A, B, C, U

    v = var.get()
    if v == 0:
        if entA.get() == '':
            A = set()
        else:
            A = from_string_to_set(entA.get())

        if entB.get() == '':
            B = set()
        else:
            B = from_string_to_set(entB.get())

        if entC.get() == '':
            C = set()
        else:
            C = from_string_to_set(entC.get())
    if v == 1:
        if lenA.get() == '':
            A = set()
        else:
            A = gener_vyp_set(int(lenA.get()))

        if lenB.get() == '':
            B = set()
        else:
            B = gener_vyp_set(int(lenB.get()))

        if lenC.get() == '':
            C = set()
        else:
            C = gener_vyp_set(int(lenC.get()))

    if entU_do.get() == '':
        do = 0
    else:
        do = int(entU_do.get()) + 1

    if entU_vid.get() == '':
        vid = 0
    else:
        vid = int(entU_vid.get())

    U = set(range(vid, do))
    label_output.configure(text='A = {}\n'
                               'B = {}\n'
                               'C = {}\n'
                               'U = {}'.format(A, B, C, U))


def manual_method():
    global A, B, C
    entA['state'] = NORMAL
    entB['state'] = NORMAL
    entC['state'] = NORMAL
    lenA['state'] = DISABLED
    lenB['state'] = DISABLED
    lenC['state'] = DISABLED


def random_method():
    global A, B, C
    entA['state'] = DISABLED
    entB['state'] = DISABLED
    entC['state'] = DISABLED
    lenA['state'] = NORMAL
    lenB['state'] = NORMAL
    lenC['state'] = NORMAL


def save_to_file(x):
    f = open('Результат.txt', 'ab')
    pickle.dump(x, f)
    f.close()


def window2():
    slave = Toplevel(root, bg="ORANGE")
    slave.title('Обчислення заданого виразу')
    slave.grab_set()
    slave.focus_set()

    def show():
        lf = LabelFrame(slave, text="Розв'язок", font='Arial 12', bg="ORANGE")
        lf.grid(column=0, row=5, columnspan=4)
        Label(lf, text='\nnotA = {nA}\n'
                       'notB = {nB}\n'
                       'notC = {nC}\n\n'
                       '1) NotA | NotB = {f1}\n'
                       '2) (NotA | B) = {f2}\n'
                       '3) (NotB & C) = {f3}\n'
                       '4) NotA | NotB | (notA & B)  = {f4}\n'
                       '5) NotA | NotB | (notA & B) | (NotB & C) = {f5}\n'
                       '6) NotA | NotB | (notA & B) | (NotB & C) | NotC = {result}\n\n'
                       'Відповідь: {result}'
              .format(nA=m_alg.notX(A, U), nB=m_alg.notX(B, U), nC=m_alg.notX(C, U),
                      f1=(m_alg.notX(A, U) | m_alg.notX(B, U)),
                      f2=(m_alg.notX(A, U) | B), f3=(m_alg.notX(B, U) & C),
                      f4=(m_alg.notX(A, U) | m_alg.notX(B, U)) | (m_alg.notX(A, U) & B),
                      f5=(m_alg.notX(A, U) | m_alg.notX(B, U)) | (m_alg.notX(A, U) & B) | (m_alg.notX(B, U) & C),
                      result=m_alg.vyraz(A, B, C, U)),
              font='Arial 14', justify=LEFT, bg="ORANGE").grid(column=0, row=5, sticky=W, columnspan=4, )

    def but_disable(event):
        but['text'] = 'Збережено!'
        but['state'] = DISABLED

    Label(slave, text='A = {}\n'
                      'B = {}\n'
                      'C = {}\n'.format(A, B, C),
          font="Arial 14", justify=LEFT, bg="ORANGE").grid(column=0, row=1, sticky=W, columnspan=3)
    Label(slave, text='Заданий вираз:\n'
                      'D = NotA | NotB | (notA & B) | (NotB & C) | NotC = {}\n'.format(m_alg.vyraz(A, B, C, U)),
          font='Arial 14 bold', bg="ORANGE") \
        .grid(column=0, row=0, sticky=W, columnspan=2)
    Button(slave, text="Показати розв'язок", font="Arial 12",
           command=show, bg="ORANGE").grid(column=0, row=3, )

    s = save_to_file(m_alg.vyraz(A, B, C, U))
    but = Button(slave, text='Зберегти в файл', font='Arial 12', command=s, bg="ORANGE")
    but.grid(column=1, row=3)
    but.bind("<Button-1>", but_disable)


def window3():
    slave = Toplevel(root, bg="ORANGE")
    slave.title('Обчислення спрощеного вразу')
    slave.grab_set()
    slave.focus_set()

    def show():
        lf = LabelFrame(slave, text="Розв'язок", font='Arial 12', bg="ORANGE")
        lf.grid(column=0, row=5, sticky=W, columnspan=4)
        Label(lf, text='1) notA | notB = {f1}\n'
                       '2) notA | notC | notB = {result}\n\n'
                       'Відповідь: {result}'.format(f1=(m_alg.notX(A, U) | m_alg.notX(C, U)),
                                                    result=s_alg.spr_vyraz(A, B, C, U)),
              font='Arial 14', justify=LEFT, bg="ORANGE").grid(column=0, row=5, sticky=W, columnspan=4)

    def but_disable(event):
        but['text'] = 'Збережено!'
        but['state'] = DISABLED

    Label(slave, text='A = {}\n'
                      'B = {}\n'
                      'C = {}'.format(A, B, C),
          font="Arial 14", justify=LEFT, bg="ORANGE").grid(column=0, row=1, sticky=W, columnspan=3)
    Label(slave, text='Спрощений вираз:\n'
                      'D = notA | notC | notB = {}'.format(s_alg.spr_vyraz(A, B, C, U)), font='Arial 14 bold',
          bg="ORANGE") \
        .grid(column=0, row=0, sticky=W, columnspan=4)
    Button(slave, text="Показати розв'язок", font="Arial 12",
           command=show, bg="ORANGE").grid(column=0, row=3)

    s = save_to_file(s_alg.spr_vyraz(A, B, C, U))
    but = Button(slave, text='Зберегти в файл', font='Arial 12', command=s, bg="ORANGE")
    but.grid(column=1, row=3)
    but.bind("<Button-1>", but_disable)


def window4():
    global time1, time2, X, Y
    X = m_alg.notX(A, U)
    Y = m_alg.notX(B, U)

    slave = Toplevel(root, bg="ORANGE")
    slave.title('Перетин')
    slave.grab_set()
    slave.focus_set()

    def but_disable(event):
        but['text'] = 'Збережено!'
        but['state'] = DISABLED

    Label(slave, text='Задана операція:\n'
                      'Z = X & Y', font="Arial 14 bold", bg="ORANGE").grid(column=0, row=0, columnspan=3)
    Label(slave, text='X = {}\n'
                      'Y = {}\n'.format(X, Y),
          font="Arial 14", justify=LEFT, bg="ORANGE").grid(column=0, row=1, sticky=W, columnspan=7)

    s = save_to_file(inters.intersection(X, Y))
    but = Button(slave, text='Зберегти в файл', font='Arial 12', command=s, bg="ORANGE")
    but.grid(column=1, row=3)
    but.bind("<Button-1>", but_disable)


def window5():
    slave = Toplevel(root, bg="ORANGE")
    slave.title('Результати')
    slave.grab_set()
    slave.focus_set()

    f = open('Результат.txt', 'rb')
    D1 = pickle.load(f)
    D2 = pickle.load(f)
    Z1 = pickle.load(f)
    Z2 = X & Y

    rez1 = 'Вітаю, результати збігаються!' if D1 == D2 else 'Щось не так. Можливо, помилка при обчисленні'
    rez2 = 'Вітаю, результати збігаються!' if Z1 == Z2 else 'Щось не так. Можливо, помилка при обчисленні'

    def but():
        Label(slave, text=rez1, font="Arial 12", fg='red', bg="ORANGE").grid(column=0, row=3, sticky=W, columnspan=2)
        Label(slave, text=rez2, font="Arial 12", fg='red', bg="ORANGE").grid(column=0, row=9, sticky=W, columnspan=2)

    lf1 = LabelFrame(slave, text='Множина D', font='Arial 12', bg="ORANGE")
    lf2 = LabelFrame(slave, text='Множина Z', font='Arial 12', bg="ORANGE")
    lf1.grid(column=0, row=1, sticky=W, columnspan=2, rowspan=2)
    lf2.grid(column=0, row=7, sticky=W, columnspan=2, rowspan=2)

    Label(slave, text='Результати обчислень', font='Arial 14 bold', bg="ORANGE").grid(column=0, row=0, columnspan=2)
    Label(lf1, text='D(початковий алгоритм) = NotA | NotB | (notA & B) | (NotB & C) | NotC =\n\t\t= {}'.format(D1),
          font="Arial 14", justify=LEFT, bg="ORANGE") \
        .grid(column=0, row=1, sticky=W, columnspan=2)
    Label(lf1, text='D(спрощений алгоритм) = notA | notB | notC = {}'.format(D2), font="Arial 14", justify=LEFT,
          bg="ORANGE") \
        .grid(column=0, row=2, sticky=W, columnspan=2)
    Label(slave, text='\t', bg="ORANGE").grid(column=0, row=6, sticky=W, columnspan=2, )

    Label(lf2, text='Z(свій алгоритм) = {}'.format(Z1), font="Arial 14", justify=LEFT, bg="ORANGE") \
        .grid(column=0, row=7, sticky=W, columnspan=2)
    Label(lf2, text='Z(алгоритм Python) = {}'.format(Z2), font="Arial 14", justify=LEFT, bg="ORANGE") \
        .grid(column=0, row=8, sticky=W, columnspan=2)
    Label(slave, text='   ', bg="ORANGE").grid(column=2, row=2, rowspan=2, )
    Label(slave, text='\t', bg="ORANGE").grid(column=0, row=11)

    Button(slave, text='Порівняти результати', font="Arial 12", command=but, bg="ORANGE").grid(column=0, row=12)


root = Tk()
root.title('Задати множини')
root.minsize(550, 500)

Label(root, width=15, height=2, bg='ORANGE', text='П.І.Б: ', relief="solid").grid(row=0, column=10, pady=5)
Label(root, width=30, height=2, bg='ORANGE', text='Ільків Максим Ярославович',
      relief="groove").grid(row=0, column=11, pady=5, padx=(0, 150))
Label(root, width=15, height=2, bg='ORANGE', text='Номер у групі:',
      relief="solid").grid(row=1, column=10, pady=5)
Label(root, width=20, height=2, bg='ORANGE', text='ІО-93',
      relief="groove").grid(row=1, column=11, pady=5, padx=(0, 150))
Label(root, width=15, height=2, bg='ORANGE', text='Номер в списку:',
      relief="solid").grid(row=2, column=10, pady=5)
Label(root, width=20, height=2, bg='ORANGE', text='12',
      relief="groove").grid(row=2, column=11, pady=5, padx=(0, 150))
Label(root, width=20, height=2, bg="ORANGE", text='Варіант',
      relief="solid").grid(row=3, column=10, pady=5)
Label(root, width=20, height=2, bg="ORANGE",
      relief="groove", text="" + variant()).grid(row=3, column=11, pady=5, padx=(0, 150))

window2 = Button(root, width=20, height=2, bg="ORANGE", text='Вікно 2',
                 relief="solid", command=window2).grid(row=4, column=10, pady=5)
window3 = Button(root, width=20, height=2, bg="ORANGE", text='Вікно 3',
                 relief="solid", command=window3).grid(row=4, column=11, pady=5)
window4 = Button(root, width=20, height=2, bg="ORANGE", text='Вікно 4',
                 relief="solid", command=window4).grid(row=5, column=10, pady=5)
window5 = Button(root, width=20, height=2, bg="ORANGE", text='Вікно 5',
                 relief="solid", command=window5).grid(row=5, column=11, pady=5)

var = IntVar()
var.set(0)
rad0 = Radiobutton(root, text="Вручну", variable=var, value=0, command=manual_method, width=20, height=2, relief="solid",
                   bg="ORANGE")
rad1 = Radiobutton(root, text="Випадково", variable=var, value=1, command=random_method, width=20, height=2, relief="solid",
                   bg="ORANGE")
rad0.grid(column=0, row=0, columnspan=2, sticky=W)
rad1.grid(column=0, row=1, columnspan=2, sticky=W)

Label(root, text='Задати множини вручну', font="Arial 14", width=20, height=2, justify=LEFT, relief="groove",
      bg="ORANGE") \
    .grid(column=0, row=2, columnspan=3)

Label(root, text='A:', width=2, height=2, relief="groove", bg="ORANGE").grid(column=0, row=3, sticky=E)
Label(root, text='B:', width=2, height=2, relief="groove", bg="ORANGE").grid(column=0, row=4, sticky=E)
Label(root, text='C:', width=2, height=2, relief="groove", bg="ORANGE").grid(column=0, row=5, sticky=E)

entA = Entry(root, width=30, bd=1, state=DISABLED, relief="groove")
entA.grid(column=1, row=3, sticky=W)
entB = Entry(root, width=30, bd=1, state=DISABLED, relief="groove")
entB.grid(column=1, row=4, sticky=W)
entC = Entry(root, width=30, bd=1, state=DISABLED, relief="groove")
entC.grid(column=1, row=5, sticky=W)

Label(root, text='Задати множини випадково', font="Arial 14", width=30, height=2, justify=LEFT, relief="groove",
      bg="ORANGE") \
    .grid(column=3, row=2, columnspan=3)

Label(root, text='Потужність A:', width=20, height=2, relief="groove", bg="ORANGE").grid(column=3, row=3, sticky=E)
Label(root, text='Потужність B:', width=20, height=2, relief="groove", bg="ORANGE").grid(column=3, row=4, sticky=E)
Label(root, text='Потужність C:', width=20, height=2, relief="groove", bg="ORANGE").grid(column=3, row=5, sticky=E)

lenA = Entry(root, width=10, bd=1, state=DISABLED)
lenA.grid(column=4, row=3, sticky=W)
lenB = Entry(root, width=10, bd=1, state=DISABLED)
lenB.grid(column=4, row=4, sticky=W)
lenC = Entry(root, width=10, bd=1, state=DISABLED)
lenC.grid(column=4, row=5, sticky=W)
Label(root, text='Задати універсальну множину', font="Arial 12", width=25, height=2, relief="solid", bg="ORANGE",
      justify=LEFT) \
    .grid(column=0, row=6, columnspan=3)

Label(root, text='Від:', width=5, height=2, relief="groove", bg="ORANGE").grid(column=0, row=7, sticky=E)
Label(root, text='До:', width=5, height=2, relief="groove", bg="ORANGE").grid(column=0, row=8, sticky=E)

entU_vid = Entry(root, width=10, bd=1, relief="groove")
entU_vid.grid(column=1, row=7, sticky=W)

entU_do = Entry(root, width=10, bd=1, relief="groove")
entU_do.grid(column=1, row=8, sticky=W)

A = set()
B = set()
C = set()
U = set()
but_OK = Button(root, text='Згенерувати множини', font='Arial 12', command=generABC, width=25, height=2, relief="solid",
                bg="ORANGE")
but_OK.grid(column=1, row=9, columnspan=4)

open('Результат.txt', 'wb').close()

label_output = Label(root, text='A = {}\n'
                               'B = {}\n'
                               'C = {}\n'
                               'U = {}'.format(A, B, C, U),
                    font="Arial 14", justify=LEFT, width=40, height=5, relief="groove", bg="ORANGE", )
label_output.grid(column=1, row=11, columnspan=100, sticky=W, padx=5)

root.mainloop()
