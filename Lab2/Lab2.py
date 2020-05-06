import networkx as nx
import pylab as plt
import random
from tkinter import *


class Lab2:
    A = set()
    B = set()
    Relation_S = set()
    Relation_R = set()
    S = set()
    R = set()

    def my_variant(self, n=12, g=93, m="IO"):
        if m == "IO":
            n += 1
        return str((n + g % 60) % 30 + 1)

    def window2(self):
        self.A = set()
        self.B = set()
        self.slave2 = Toplevel(self.root)
        self.slave2.title("Вікно 2")
        self.slave2.focus_set()

        def set_women():
            if women_set.get() == "A":
                for i in list_of_women.curselection():
                    self.A.add(self.list_of_women_text[i])
            elif women_set.get() == "B":
                for i in list_of_women.curselection():
                    self.B.add(self.list_of_women_text[i])

        def set_men():
            if men_set.get() == "A":
                for i in list_of_men.curselection():
                    self.A.add(self.list_of_men_text[i])
            elif men_set.get() == "B":
                for i in list_of_men.curselection():
                    self.B.add(self.list_of_men_text[i])

        def save_in_a():
            with open(r'/saved_in_a', "w") as w:
                for i in self.A:
                    w.write(str(i) + "\n")
            print(self.A)

        def save_in_b():
            with open(r'/saved_in_b', "w") as w:
                for i in self.B:
                    w.write(str(i) + "\n")
            print(self.B)

        def read_from_a():
            with open(r'/saved_in_a', "r") as r:
                for line in r:
                    self.A.add(line[:-1])

        def read_from_b():
            with open(r'/saved_in_b', "r") as r:
                for line in r:
                    self.B.add(line[:-1])

        def clear_a():
            self.A.clear()

        def clear_b():
            self.B.clear()

        Label(self.slave2, width=15, height=2, bg='ORANGE', text='Список жіночих імен', relief="solid") \
            .grid(row=0, column=0, pady=5)
        list_of_women = Listbox(self.slave2, selectmode=EXTENDED, bg='ORANGE', relief="groove")
        list_of_women.grid(row=0, column=1, pady=5)
        self.list_of_women_text = ['Інна', 'Жанна', 'Ганна', 'Ірина', 'Каріна', 'Роксолана', 'Людмила', 'Василина',
                                   'Надія']
        for i in self.list_of_women_text:
            list_of_women.insert(END, str(i))
        women_set = StringVar()
        women_set.set("A")
        Radiobutton(self.slave2, text="A", variable=women_set, value="A", bg='ORANGE', relief="groove").grid(row=1,
                                                                                                             column=0,
                                                                                                             pady=5)
        Radiobutton(self.slave2, text="B", variable=women_set, value="B", bg='ORANGE', relief="groove").grid(row=1,
                                                                                                             column=1,
                                                                                                             pady=5)
        Button(self.slave2, text="Запис в", command=set_women, width=15, height=2, bg='ORANGE', relief="solid") \
            .grid(row=1, column=2, pady=5)
        Label(self.slave2, width=15, height=2, bg='ORANGE', text='Список чоловічих імен', relief="solid") \
            .grid(row=3, column=0, pady=5)
        list_of_men = Listbox(self.slave2, selectmode=EXTENDED, bg='ORANGE', relief="groove")
        list_of_men.grid(row=3, column=1, pady=5)
        self.list_of_men_text = ['Артур', "Тимофій", "Артем", "Олександр", "Володимир", "Євгеній", 'Назар', "Максим",
                                 "Орест"]
        for i in self.list_of_men_text:
            list_of_men.insert(END, str(i))
        men_set = StringVar()
        men_set.set("A")
        Radiobutton(self.slave2, text="A", variable=men_set, value="A", bg='ORANGE', relief="groove").grid(row=4,
                                                                                                           column=0,
                                                                                                           pady=5)
        Radiobutton(self.slave2, text="B", variable=men_set, value="B", bg='ORANGE', relief="groove").grid(row=4,
                                                                                                           column=1,
                                                                                                           pady=5)
        Button(self.slave2, text="Запис в", width=15, height=2, bg='ORANGE', relief="solid", command=set_men).grid(
            row=4, column=2, pady=5)
        Button(self.slave2, text="Зчитати А", width=15, height=2, bg='ORANGE', relief="solid",
               command=read_from_a).grid(row=5, column=0, pady=5)
        Button(self.slave2, text="Зчитати B", width=15, height=2, bg='ORANGE', relief="solid",
               command=read_from_b).grid(row=6, column=0, pady=5)
        Button(self.slave2, text="Записати А", width=15, height=2, bg='ORANGE', relief="solid", command=save_in_a).grid(
            row=5, column=1, pady=5)
        Button(self.slave2, text="Записати B", width=15, height=2, bg='ORANGE', relief="solid", command=save_in_b).grid(
            row=6, column=1, pady=5)
        Button(self.slave2, text="Очистити A", width=15, height=2, bg='ORANGE', relief="solid", command=clear_a).grid(
            row=5, column=2, pady=5)
        Button(self.slave2, text="Очистити B", width=15, height=2, bg='ORANGE', relief="solid", command=clear_b).grid(
            row=6, column=2, pady=5)

    def window3(self):
        self.slave3 = Toplevel(self.root)
        self.slave3.title("Вікно 3")
        self.slave3.focus_set()

        def update_a():
            list_a.delete(0, END)
            for i in list(self.A):
                list_a.insert(END, str(i))

        def update_b():
            list_b.delete(0, END)
            for i in list(self.B):
                list_b.insert(END, str(i))

        Label(self.slave3, text="Множина А:", width=15, height=2, bg='ORANGE', relief="solid").grid(row=0, column=0,
                                                                                                    pady=5)
        list_a = Listbox(self.slave3, selectmode=EXTENDED, bg='ORANGE', relief="groove")
        list_a.grid(row=0, column=1, pady=5)
        Button(self.slave3, text="Оновити А", width=15, height=2, bg='ORANGE', relief="solid", command=update_a).grid(
            row=0, column=2, pady=5)
        Label(self.slave3, text="Множина B:", width=15, height=2, bg='ORANGE', relief="solid").grid(row=1, column=0,
                                                                                                    pady=5)
        list_b = Listbox(self.slave3, selectmode=EXTENDED, bg='ORANGE', relief="groove")
        list_b.grid(row=1, column=1, pady=5)
        Button(self.slave3, text="Оновити B", width=15, height=2, bg='ORANGE', relief="solid", command=update_b).grid(
            row=1, column=2, pady=5)

        def form_relation_s():
            if self.A != set() and self.B != set():
                self.edges_list_s = set([])
                selection_father = list(self.A)
                selection_child = list(self.B)
                while selection_father != list():
                    father = random.choice(selection_father)
                    selection_father.remove(father)
                    if father in self.list_of_men_text:
                        if father in selection_child:
                            selection_child.remove(father)
                        while random.randrange(0, 10) in range(7) and selection_child != list():
                            child = random.choice(selection_child)
                            if child != father and (child, father) not in self.Relation_S:
                                self.Relation_S.add((father, child))
                                selection_child.remove(child)
                                self.edges_list_s.add((father, child))
                                if child in selection_father:
                                    selection_father.remove(child)
                print(self.Relation_S)
                self.S = self.edges_list_s
                self.g1 = nx.DiGraph()
                self.g1.add_nodes_from(list(self.A | self.B))
                self.g1.add_edges_from(self.edges_list_s)
                nx.draw_networkx(self.g1, pos=nx.spring_layout(self.g1), arrows=True, with_labels=True,
                                 edges=self.g1.edges(), edge_color="b")
                plt.show()
        Button(self.slave3, text="Сформувати aSb", width=15, height=2, bg='ORANGE', relief="solid",
               command=form_relation_s).grid(
            row=2, column=0, pady=5)
        def form_relation_r():
            if self.A != set() and self.B != set() and self.Relation_S != set():
                self.edges_list_r = set()
                selection_svekor = list(self.A)
                selection_narechenii = list(self.B)
                while selection_svekor != list():
                    svekor = random.choice(selection_svekor)
                    selection_svekor.remove(svekor)
                    if svekor in self.list_of_men_text:
                        flag = True
                        local_select_narechenii = list(selection_narechenii)
                        while local_select_narechenii != list() and flag:
                            narechenii = random.choice(local_select_narechenii)
                            if narechenii != svekor and (
                                    narechenii,
                                    svekor) not in self.Relation_R and narechenii in self.list_of_men_text and \
                                    (narechenii, svekor) not in self.Relation_S and (
                                    svekor, narechenii) not in self.Relation_S:
                                self.Relation_R.add((svekor, narechenii))
                                selection_narechenii.remove(narechenii)
                                self.edges_list_r.add((svekor, narechenii))
                                flag = False
                            else:
                                local_select_narechenii.remove(narechenii)
                print(self.Relation_R)
                self.R = self.edges_list_r
                self.g1 = nx.DiGraph()
                self.g1.add_nodes_from(list(self.A | self.B))
                self.g1.add_edges_from(self.edges_list_r)
                nx.draw_networkx(self.g1, pos=nx.spring_layout(self.g1), arrows=True, with_labels=True,
                                 edges=self.g1.edges(), edge_color="r")
                plt.show()

        Button(self.slave3, text="Сформувати aRb", width=15, height=2, bg='ORANGE', relief="solid",
               command=form_relation_r).grid(
            row=2, column=1, pady=5)

    def window4(self):
        self.slave4 = Toplevel(self.root)
        self.slave4.title('Вікно 4')
        self.slave4.focus_set()

        def union():
            C = self.R | self.S
            print(C)
            g = nx.DiGraph()
            g.add_nodes_from(list(self.A | self.B))
            g.add_edges_from(C, color="r")
            nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
            plt.show()
        Button(self.slave4, text="R | S", width=15, height=2, bg='ORANGE', relief="solid",
               command=union).grid(row=0, column=0, pady=5)

        def crossing():
            C = self.R & self.S
            print(C)
            g = nx.DiGraph()
            g.add_nodes_from(list(self.A | self.B))
            g.add_edges_from(C)
            nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
            plt.show()

        Button(self.slave4, text="R & S", width=15, height=2, bg='ORANGE', relief="solid",
               command=crossing).grid(row=0, column=1, pady=5)

        def difference():
            C = self.R - self.S
            print(C)
            g = nx.DiGraph()
            g.add_nodes_from(list(self.A | self.B))
            g.add_edges_from(C)
            nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
            plt.show()

        Button(self.slave4, text="R - S", width=15, height=2, bg='ORANGE', relief="solid",
               command=difference).grid(row=1, column=0, pady=5)

        def bez_R():
            U = {(a, b) for a in self.A for b in self.B}
            C = U - self.R
            print(C)
            g = nx.DiGraph()
            g.add_nodes_from(list(self.A | self.B))
            g.add_edges_from(C)
            nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
            plt.show()
        Button(self.slave4, text="U / R", width=15, height=2, bg='ORANGE', relief="solid",
               command=bez_R).grid(row=1, column=1, pady=5)

        def inversionS():
            C = list((elem[1], elem[0]) for elem in self.S)
            print(C)
            g = nx.DiGraph()
            g.add_nodes_from(list(self.A | self.B))
            g.add_edges_from(C)
            nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
            plt.show()
        Button(self.slave4, text="S^-1", width=15, height=2, bg='ORANGE', relief="solid",
               command=inversionS).grid(row=2, column=0, pady=5)

    def main_window(self):
        self.root = Tk()
        self.root.title("DM LAB2")
        self.root.minsize(500, 250)
        Label(self.root, width=15, height=2, bg='ORANGE', text='П.І.Б: ', relief="solid").grid(row=0, column=10, pady=5)
        Label(self.root, width=30, height=2, bg='ORANGE', text='Ільків Максим Ярославович',
              relief="groove").grid(row=0, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=15, height=2, bg='ORANGE', text='Група:',
              relief="solid").grid(row=1, column=10, pady=5)
        Label(self.root, width=20, height=2, bg='ORANGE', text='ІО-93',
              relief="groove").grid(row=1, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=15, height=2, bg='ORANGE', text='Номер в списку:',
              relief="solid").grid(row=2, column=10, pady=5)
        Label(self.root, width=20, height=2, bg='ORANGE', text='12',
              relief="groove").grid(row=2, column=11, pady=5, padx=(0, 150))
        Label(self.root, width=20, height=2, bg="ORANGE", text='Варіант',
              relief="solid").grid(row=3, column=10, pady=5)
        Label(self.root, width=20, height=2, bg="ORANGE",
              relief="groove", text="" + self.my_variant()).grid(row=3, column=11, pady=5, padx=(0, 150))
        window2 = Button(self.root, width=20, height=2, bg="ORANGE", text='Вікно 2',
                         relief="solid", command=self.window2).grid(row=4, column=10, pady=5, )
        window3 = Button(self.root, width=20, height=2, bg="ORANGE", text='Вікно 3',
                         relief="solid", command=self.window3).grid(row=4, column=11, pady=5, padx=(0, 150))
        window4 = Button(self.root, width=20, height=2, bg="ORANGE", text='Вікно 4',
                         relief="solid", command=self.window4).grid(row=6, column=10, pady=5, )
        self.root.mainloop()

main = Lab2()
main.main_window()