import msvcrt
import time


class GameObject:
    def __init__(self, pos_x, pos_y, symbol):
        self.char = str(symbol)
        self.x = pos_x
        self.y = pos_y
    def describe(self):
        return f"{self.char} at ({self.x}, {self.y})"


class Player(GameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, "@")
        self.health = 100
        self.attack = 10
        self.defense = 5


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[" " for _ in range(width)] for _ in range(height)]
    
    #добавляет стены по краям карты
    def MakeBorders (self):
        for x in range(self.width):
            self.map[0][x] = "#"
            self.map[self.height - 1][x] = "#"
        for y in range(self.height):
            self.map[y][0] = "#"
            self.map[y][self.width - 1] = "#"
    def show (self):
        for row in self.map:
            print("".join(row))


player = Player(1, 8)
print(player.describe())
game_map = GameMap(20, 10)
game_map.MakeBorders()          
game_map.show()