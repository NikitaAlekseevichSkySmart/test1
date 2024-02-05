from random import *

class Field:
    def  __init__(self, ships, size=10):
        self.size=size
        self.ships=ships
        self.grid = []
        for i in range(self.size):
            a=[]
            for o in range(self.size):
                a.append(0)
            self.grid.append(a)
        self.ships_alive=self.ships
        self.field()

    def place_ships_randomly(self):
            y = []
            x = []
            for i in range(self.ships):
                y1 = randint(0, self.size - 1)
                x1 = randint(0, self.size - 1)
                for p in range(len(y)):
                    if y[p] == y1 and x[p] == x1:
                        i = i - 1
                        break
                y.append(y1)
                x.append(x1)
            return y, x

    def field(self):
            y1, x1 = self.place_ships_randomly()
            for i in range(self.ships_alive):
                self.grid[y1[i]][x1[i]] = "■"

    def display(self, you_grid, you_battle_grid):
            print("Ваша расстановка")
            for i in range(self.size):
                for j in range(self.size):
                    if j !=self.size-1:
                        print(you_grid.grid[i][j], end=" ")
                    else:
                        print(you_grid.grid[i][j])

            print("Расстановка врага")
            for i in range(self.size):
                for j in range(self.size):
                    if j != self.size - 1:
                        print(you_battle_grid.grid[i][j], end=" ")
                    else:
                        print(you_battle_grid.grid[i][j])


    def play(self, a, b, c, d):
        you_ships_alive=a.ships_alive
        enemi_ships_alive=c.ships_alive
        while you_ships_alive!=0 or enemi_ships_alive!=0:
            self.display(a, b)
            x=int(input("Х: от 0 до 9"))
            y=int(input("Y: от 0 до 9"))
            if c.grid[y][x] == "■":
                c.grid[y][x] = "+"
                b.grid[y][x] = "+"
                enemi_ships_alive=enemi_ships_alive-1
            else:
                c.grid[y][x] = "*"
                b.grid[y][x] = "*"

            t=0
            while t==0:
                x1=randint(0, 9)
                y1=randint(0, 9)
                if d.grid[y1][x1]==0:
                    t=1
            if a.grid[y1][x1] == "■":
                a.grid[y1][x1] = "+"
                d.grid[y1][x1] = "+"
                you_ships_alive = you_ships_alive - 1
            else:
                a.grid[y1][x1] = "*"
                d.grid[y1][x1] = "*"

a=Field(10)
b=Field(0)
c=Field(10)
d=Field(0)
a.play(a, b, c, d)