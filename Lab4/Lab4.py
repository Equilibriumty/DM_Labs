# IMPORT MODULES
from tkinter import *
import networkx as nx
import pylab as plt
import numpy as np

# GLOBAL VARIABLES
NZK = 9313
my_variant = str((NZK % 6) + 1) # = 2


# MAIN CLASS
class Lab4:
    def GraphColoring(self, Edges):
        print(Edges)
        result = {}
        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'springgreen', 'lime', 'olive', 'indigo', 'fuchsia']

        def SortEdges():
            sort_list = {}
            for key in Edges:
                sort_list[key] = len(Edges[key])
            sort2 = sorted(sort_list.items(),key=lambda x: x[1], reverse=True)

            return sort2

        def colorize():
            n = 0

            def removeColor():
                for color in colors:
                    if color not in stackColor: return color
                color = colors[n+1]
                colors.append(color)
                return color

            for key in sort_list:
                stackColor = []
                for key2 in Edges[key[0]]:
                    if key2 in result: stackColor.append(result[key2])
                color = removeColor()
                result[key[0]] = color
            return result

        sort_list = SortEdges()
        return colorize()

    def colorize_graph(self):
        Edges = dict()
        for i in range(int(self.input.get())):
            edge_list = []
            for j in range(int(self.input.get())):
                if self.table[i][j] == '1':
                    edge_list.append(j + 1)
            Edges[i + 1] = edge_list

        plt.figure('Розфарбований граф')
        self.gr = nx.Graph()
        for i in range(int(self.input.get())):
            self.gr.add_node(i + 1)
        for i in range(int(self.input.get())):
            for j in range(int(self.input.get())):
                if self.table[i][j] != '0':
                    self.gr.add_edge(i + 1, j + 1)
        pos = nx.circular_layout(self.gr)
        node_colors = Lab4.GraphColoring(self, Edges).items()
        nx.draw_networkx(self.gr, pos)
        for i in node_colors:
            nx.draw_networkx(self.gr, pos, nodelist=[i[0]], node_color=i[1])
        plt.axis('off')
        plt.show()

    def show_graph(self):
        self.table = []
        for i in range(int(self.input.get())):
            self.table.append([])
            for j in range(int(self.input.get())):
                self.table[i].append(self.matrix_of_empty_elements[i][j].get())
        plt.figure("Заданий граф")
        self.Graph = nx.Graph()
        for i in range(int(self.input.get())):
            self.Graph.add_node(i+1)
        for i in range(int(self.input.get())):
            for j in range(int(self.input.get())):
                if self.table[i][j] != "0":
                    self.Graph.add_edge(i+1, j+1)
        pos = nx.circular_layout(self.Graph)
        nx.draw_networkx(self.Graph, pos)
        plt.axis("off")
        plt.show()

    def generate_table(self):

        self.Frame = LabelFrame(self.slave2, text="Матриця суміжності")
        self.Frame.grid(row=1, columnspan=3)
        self.random_matrix = np.random.randint(0, 2, size=(int(self.input.get()), int(self.input.get())))
        self.temporary_matrix = np.tril(self.random_matrix) + np.tril(self.random_matrix, -1).transpose()
        np.fill_diagonal(self.temporary_matrix, 0)
        self.matrix_of_empty_elements = []
        for row in range(int(self.input.get())):
            self.matrix_of_empty_elements.append([])
            for column in range(int(self.input.get())):
                self.matrix_of_empty_elements[row].append(Entry(self.Frame, width=4))
                self.matrix_of_empty_elements[row][column].grid(row=row + 1, column=column + 1, padx=4, pady=4)
                self.matrix_of_empty_elements[row][column].insert(END, self.temporary_matrix[row][column])
        self.Frame1 = LabelFrame(self.slave2, text="Дії з графами")
        self.Frame1.grid(row=11, column=11)
        self.Button = Button(self.slave2, text="Відобразити граф", width=15, height=2, command = self.show_graph, bg="ORANGE", relief="groove")
        self.Button.grid(row=11, column=0)
        self.Button1 = Button(self.slave2, text="Розмалювати граф", width=15, height=2, command= self.colorize_graph, bg="ORANGE", relief="groove")
        self.Button1.grid(row=11, column=1)

    def window_2(self):
        self.slave2 = Toplevel(self.root)
        self.slave2.title("Задайте матрицю суміжності")
        self.slave2.focus_set()
        self.slave2.minsize(500, 500)
        self.Label = Label(self.slave2, bg="ORANGE", width=20, height=2, text="Задайте к-сть вершин", relief="solid") \
            .grid(row=0, column=0)
        self.input = Entry(self.slave2, bg="ORANGE")
        self.input.grid(row=0, column=1, padx=(10, 0))
        self.but = Button(self.slave2, width=30, height=2, bg="ORANGE", relief="solid",
                          text="Згенерувати матрицю суміжності", command=self.generate_table) \
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
        Label(self.root, width=15, height=2, bg="ORANGE", relief="solid", text="Завдання").grid(row=4, column=10,
                                                                                                pady=5)
        Label(self.root, width=50, height=5, bg="ORANGE", relief="groove",
              text='Набути теоретичні знання по темі «Розфарбування графів». \n'
                   'Створити програму розфарбування графів, яка реалізує \n'
                   'евристичний алгоритм розфарбування.', ).grid(row=4, column=11, pady=5, padx=(0, 150))
        Button(self.root, width=15, height=2, bg="ORANGE", relief="groove", text="Наступне вікно",
               command=self.window_2) \
            .grid(row=5, column=10, pady=5)
        self.root.mainloop()

# CLASS & WINDOW EXAMPLE
a = Lab4()
a.main_window()
