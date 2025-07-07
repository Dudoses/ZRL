import msvcrt
import time
import os

MAPWIDTH = 20
MAPHEIGHT = 10

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
    def act(self, key):
        if key in [b'a', b'A']:
            self.x -= 1
        elif key in [b'd', b'D']:
            self.x += 1
        if self.x < 0:
            self.x = MAPWIDTH-1
        elif self.x >= MAPWIDTH:
            self.x = 0

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[" " for _ in range(width)] for _ in range(height)]
    
    # adds walls at map borders
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

objects_list = [player]

while True:
    game_map = GameMap(MAPWIDTH, MAPHEIGHT)
    game_map.MakeBorders()
    os.system('cls')
    key = '0'
    if msvcrt.kbhit():
        key = msvcrt.getch()
    time.sleep(0.02)
    print(key)
    print(game_map)
    player.act(key)
    game_map.map[player.y][player.x] = '@'
    game_map.show()
