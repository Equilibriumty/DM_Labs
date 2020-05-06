from tkinter import *
import pylab as plt
import networkx as nx
from tkinter import messagebox

root = Tk()


class Main(Entry):
    def __init__(self, parent, c):
        self.value = StringVar()
        Entry.__init__(self, parent, textvariable=self.value, width=3, justify="center")
        self.Label3 = Label(parent, bg="ORANGE")
        self.Label3.grid(row=0, column=0)
        for i in range(c):
            self.Label1 = Label(parent, bg="ORANGE", relief="groove")
            self.Label1['text'] += "X" + "{0}".format(i+1)
            self.Label1.grid(row=0, column=i+1)
            self.Label2 = Label(parent, bg="ORANGE", relief="groove")
            self.Label2['text'] += "X" + "{0}".format(i+1)
            self.Label2.grid(row=i+1, column=0)


def my_variant():
    return str((9313 % 10) + 1)


class Table(Frame):
    def __init__(self, parent, cols):
        Frame.__init__(self, parent)
        self.cells_of_table = [[Main(parent, cols) for i in range(cols)] for j in range(cols)]
        [self.cells_of_table[i][j].grid(row=i+1, column=j+1) for i in range(cols) for j in range(cols)]


class Lab_3(Table):
    def __init__(self, main_menu):
        Table.__init__(self, main_menu, 0)
        self.main_menu = main_menu
        self.main_menu.title("DM LAB3")
        self.main_menu.minsize(500, 500)
        self.Label = Label(self.main_menu, text="Введіть к-сть вершин", bg="ORANGE", relief="groove")
        self.Input = Entry(self.main_menu, width=5, relief="solid", bg="ORANGE")
        self.Button = Button(self.main_menu, text="Зберегти", command=self.get_input_values, bg="ORANGE", relief="groove")
        self.Button1 = Button(self.main_menu, text="Побудувати граф\nта найкоротший знайти\n шлях за допомогою\n алгоритма Дейкстри",
                              bg="ORANGE", command=self.matrix_of_weight)
        self.Label1 = Label(self.main_menu, text="Введіть № першої вершини", bg="ORANGE", relief="groove")
        self.Input1 = Entry(self.main_menu, width=5, bg="ORANGE", relief="solid")
        self.Label2 = Label(self.main_menu, text="Введіть № останньої вершини", bg="ORANGE", relief="groove")
        self.Input2 = Entry(self.main_menu, width=5, bg="ORANGE", relief="solid")
        self.Label3 = Label(self.main_menu, width=20, bg="ORANGE", relief="groove", text="Матриця ваг")
        self.Label4 = Label(self.main_menu, width=40, bg="ORANGE", relief="groove", text="П.І.Б: Ільків Максим Ярославович")
        self.Label5 = Label(self.main_menu, width=20, bg="ORANGE", relief="groove", text="Група: ІО-93")
        self.Label6 = Label(self.main_menu, width=20, bg="ORANGE", relief="groove", text="Номер у списку: 12")
        self.Label7 = Label(self.main_menu, width=40, bg="ORANGE", relief="groove", text="Варіант: " + my_variant())
        self.Label.place(x=5, y=5)
        self.Label4.place(x=5, y=35)
        self.Label5.place(x=5, y=60)
        self.Label6.place(x=165, y=60)
        self.Label7.place(x=5, y=85)
        self.Button.place(x=175, y=5)
        self.Input.place(x=125, y=5)
        self.main_menu.mainloop()

    def get_input_values(self):
        c = int(self.Input.get())
        self.Label.place_forget()
        self.Input.place_forget()
        self.Button.place_forget()
        self.Label4.place_forget()
        self.Label5.place_forget()
        self.Label6.place_forget()
        self.Label7.place_forget()
        self.Button1.place(x=120*c/2, y=150)
        self.Label1.place(x=240, y=5*(c+1)+5)
        self.Input1.place(x=400, y=5*(c+1)+5)
        self.Label2.place(x=240, y=10*(c+1)+55)
        self.Input2.place(x=400, y=10*(c+1)+55)
        self.Label3.place(x=0, y=10*(c+3)+60)
        try:
            self.table = Table(self.main_menu, c)
            self.table.pack()
        except TclError:
            pass
        self.main_menu.geometry("%dx%d+%d+%d" % (100*c+50, 30*(c+1)+100, 500, 200))

    def matrix_of_weight(self):
        if self.Input1 == "" or self.Input2 == "":
            messagebox.showerror("Помилка", "Задайте дані")
        elif self.Input1 == 0 or self.Input2 == 0:
            messagebox.showerror("Помилка", "Введіть правильні дані")
        else:
            c = int(self.Input.get())
            self.array = []
            for i in range(c):
                self.array.append([])
                for j in range(c):
                    self.array[i].append(self.table.cells_of_table[i][j].value.get())
            self.algorithm_deijkstra(c, int(self.Input1.get()), self.array, int(self.Input2.get()))

    def algorithm_deijkstra(self, N, S, w, Last_Node):
        inf = float("inf")
        dist = [inf] * N
        dist[S-1] = 0
        prev = [None] * N
        used = [False] * N
        min_dist = 0
        min_vertex = S-1
        try:
            while min_dist < inf:
                i = min_vertex
                used[i] = True
                for j in range(N):
                    if w[i][j] == "i":
                        w[i][j] = inf
                        if dist[i] + float(w[i][j]) < dist[j]:
                            dist[j] = dist[i] + float(w[i][j])
                            prev[j] = i
                    else:
                        if dist[i] + float(w[i][j]) < dist[j]:
                            dist[j] = dist[i] + float(w[i][j])
                            prev[j] = i
                min_dist = inf
                for j in range(N):
                    if not used[j] and dist[j] < min_dist:
                        min_dist = dist[j]
                        min_vertex = j
            path = []
            j = Last_Node-1
            while j is not None:
                path.append(j)
                j = prev[j]
            path = path[::-1]
            print(path)
            result = []
            for i in range(len(path)-1):
                result.append(("X%i" % (path[i]+1), "X%i" % (path[i+1]+1)))

            plt.figure("Найкоротший шлях від вершини {0} до вершини {1}".format(S, Last_Node))
            self.Graph = nx.DiGraph()
            for i in range(N):
                self.Graph.add_node("X" + "{0}".format(i+1))
            for i in range(len(w)):
                for j in range(len(w[i])):
                    if w[i][j] == inf:
                        continue
                    else:
                        self.Graph.add_edge("X" + "{0}".format(i+1), "X" + "{0}".format(j+1), weight=w[i][j])
            nx.draw_networkx(self.Graph, pos=nx.shell_layout(self.Graph), arrows=True, with_labels=True, node_size=50,
                             width=0.5)
            edge_labels = dict([((u, v), d["weight"]) for u, v, d in self.Graph.edges(data=True)])
            nx.draw_networkx_edge_labels(self.Graph, pos=nx.shell_layout(self.Graph), edge_labels=edge_labels, label_pos=0.3)
            nx.draw_networkx_edges(self.Graph, pos=nx.shell_layout(self.Graph), edgelist=result, edge_color="purple",
                                   arrows=True, with_labels = True)
            plt.show()
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, заповніть матрицю")
main = Lab_3(root)