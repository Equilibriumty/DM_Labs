# IMPORT MODULES
from tkinter import *
import networkx as nx
import pylab as plt
import random

# GLOBAL VARIABLES
NZK = 9313
my_variant = str((NZK % 6) + 1)


# MAIN CLASS
class Lab4:

    def evrestechniy_algorithm(self):
        pass

    def generate_table(self, N):
        self.table = []
        for i in range(N):
            self.table.append([])
            for j in range(N):
                self.table[i].append(random.randint(0, 1))
        for i in range(N):
            for j in range(N):
                if i == j:
                    self.table[i][j] = 0
                else:
                    self.table[i][j] = self.table[j][i]
        return self.table


    def window_2(self):
        self.slave2 = Toplevel(self.root)
        self.slave2.title("Задайте матрицю суміжності")
        self.slave2.focus_set()
        self.slave2.minsize(500, 500)
        self.Label = Label(self.slave2, bg="ORANGE", width=20, height=2, text="Задайте к-сть вершин", relief="solid")\
            .grid(row=0, column=0)
        self.input = Entry(self.slave2, bg="ORANGE")
        self.input.grid(row=0, column=1, padx=(10, 0))
        self.but = Button(self.slave2, width=30, height=2, bg="ORANGE", relief="solid",
                          text="Згенерувати матрицю суміжності", command=self.generate_table(5))    \
                            .grid(row=0, column=2, padx=10)
    def main_window(self):
        self.root = Tk()
        self.root.title("DM LAB4")
        self.root.minsize(500, 250)
        Label(self.root, width=15, height=2, bg='ORANGE', text='П.І.Б: ', relief="solid").grid(row=0, column=10, pady=5)
        Label(self.root, width=30, height=2, bg='ORANGE', text='Ільків Максим Ярославович',
              relief="groove").grid(row=0, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=15, height=2, bg='ORANGE', text='Група:',
              relief="solid").grid(row=1, column=10, pady=5)
        Label(self.root, width=20, height=2, bg='ORANGE', text='ІО-93',
              relief="groove").grid(row=1, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=15, height=2, bg='ORANGE', text='Номер у списку:',
              relief="solid").grid(row=2, column=10, pady=5)
        Label(self.root, width=20, height=2, bg='ORANGE', text='12',
              relief="groove").grid(row=2, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=15, height=2, bg="ORANGE", text='Варіант',
              relief="solid").grid(row=3, column=10, pady=5)
        Label(self.root, width=20, height=2, bg="ORANGE",
              relief="groove", text="" + my_variant).grid(row=3, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=15, height=2, bg="ORANGE", relief="solid",text="Завдання").grid(row=4, column=10, pady=5)
        Label(self.root, width = 50, height=5, bg="ORANGE", relief="groove",
                        text='Набути теоретичні знання по темі «Розфарбування графів». \n'
                              'Створити програму розфарбування графів, яка реалізує \n'
                              'евристичний алгоритм розфарбування.',).grid(row=4, column=11, pady=5, padx=(0, 150))
        Button(self.root, width=15, height=2, bg="ORANGE", relief="groove", text="Наступне вікно", command=self.window_2)\
            .grid(row=5, column=10, pady=5)
        self.root.mainloop()


a = Lab4()
a.main_window()
