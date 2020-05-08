# IMPORT MODULES
from tkinter import *

# GLOBAL VARIABLES
NZK = 9313
my_variant = str((NZK % 26) + 1)  # = 6
max_length = (10 + NZK) % 18  # (9313 + 10) % 18 = 17

class Lab5:
    def window_2(self):
        pass

    def main_window(self):
        self.root = Tk()
        self.root.title("DM LAB5")
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
        Label(self.root, width=15, height=2, bg="ORANGE", relief="solid", text="Завдання").grid(row=4, column=10,
                                                                                                pady=5)
        Label(self.root, width=50, height=5, bg="ORANGE", relief="groove",
              text='Вивчити принципи роботи алгоритму перестановок у \n'
                    'антилексикографічному порядку. Написати програму \n'
                    'перестановок букв українського алфавіту \n'
                    'у антилексикографічному порядку.' , ).grid(row=4, column=11, pady=5, padx=(0, 150))
        Button(self.root, width=15, height=2, bg="ORANGE", relief="groove", text="Наступне вікно",
               command=self.window_2) \
            .grid(row=5, column=10, pady=5)
        self.root.mainloop()


# CLASS & MAIN WINDOW EXAMPLES
a = Lab5()
a.main_window()
