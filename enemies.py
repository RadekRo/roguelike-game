import random

NAMES_BASE = ["Kai", "Eliana", "Jayden", "Ezra", "Luca", "Rowan", "Nova", "Amara", "Aaliyah", "Finn", "Zion", "Maeve", "Kayden", "Mia", "Mila", "Aurora", "Alina", "Remi", "Amaya", "Ari", "Blake", "Elliot", "Ivy", "Quinn", "Leo", "Arthur", "Rachel", "River", "Axel", "Aria", "Alex", "Molly", "Jude", "Elias", "Milo", "Malachi", "Charlie", "Ira", "Atlas", "Evelyn"] 

class Enemy:
    def __init__(self, name, type, level = 1):
        self.name = name
        self.type = type
        self.strength = level * random.randint(2, 4)
        self.health = level * random.randint(3, 5)
        self.coords = list()

    def update_coords(self, new_coords):
        self.coords = new_coords

    def update_health(self, new_health):
        self.health = new_health

    def __str__(self):
        return f"Name: {self.name}\nMonster class: '{self.type}'\nStrength: {self.strength}\nHealth: {self.health}\nStarting position: {self.coords}\n"


def get_enemy_name():
    return NAMES_BASE[random.randint(0, len(NAMES_BASE) - 1)]
    

def evoke_hangman():
    name = get_enemy_name()
    mark = "W"
    hangman = Enemy(name, "Wisielec")
    return hangman, mark


def evoke_tic_tac_toe():
    name = get_enemy_name()
    mark = random.choice(["X", "O"])
    tic_tac_toe = Enemy(name, "XO")
    return tic_tac_toe, mark


def evoke_zombie_sailor():
    name = get_enemy_name()
    mark = "Z"
    zombie_sailor = Enemy(name, "Marynarz Zombie")
    return zombie_sailor, mark


def evoke_agent_smith():
    name = "Agent Smith"
    mark = "A"
    agent_smith = Enemy(name, "Matrix")
    return agent_smith, mark


def evoke_milestone():
    #TODO Boss instance, create when the main functions will be operative
    pass


def find_empty_board_position(board):
    empty_slot = False
    while empty_slot == False:
        enemy_x = random.randint(0, len(board) - 1)
        enemy_y = random.randint(0, len(board[0]) - 1)
        if board[enemy_x][enemy_y] == 0:
            empty_slot = True
    return [enemy_x, enemy_y]


def place_enemy_on_board(board, coordinations, sign):
    board[coordinations[0]][coordinations[1]] = "\u001B[31m" + sign + "\u001b[0m"
    return board


def create_enemies(board, level = 1, number = 2):
    
    enemies = dict()
    for i in range(number):
        match level:
            case 1:
                enemies[i], mark = evoke_hangman()
            case 2:
                enemies[i], mark = evoke_tic_tac_toe()
            case 3:
                enemies[i], mark = evoke_zombie_sailor()
            case 4:
                enemies[i], mark = evoke_agent_smith()
            case 5:
                enemies[i], mark = evoke_milestone()
        enemy_starting_position = find_empty_board_position(board)
        enemies[i].update_coords(enemy_starting_position)
        board = place_enemy_on_board(board, enemy_starting_position, mark)

    return board, enemies

#tests
# board = [[0, 1, 1],[0, 0, 0],[1, 1, 1]]
# print(board)
# enemies, board = create_enemy(board, 3, 3)
# print(enemies[0])
# print(enemies[1])
# print(enemies[2])
# print(board)
