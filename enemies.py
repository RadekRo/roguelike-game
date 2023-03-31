import random

NAMES_BASE = ["Kai", "Eliana", "Jayden", "Ezra", "Luca", "Rowan", "Nova", "Amara", "Aaliyah", "Finn", "Zion", "Maeve", "Kayden", "Mia", "Mila", "Aurora", "Alina", "Remi", "Amaya", "Ari", "Blake", "Elliot", "Ivy", "Quinn", "Leo", "Arthur", "Rachel", "River", "Axel", "Aria", "Alex", "Molly", "Jude", "Elias", "Milo", "Malachi", "Charlie", "Ira", "Atlas", "Evelyn"] 


def get_enemy_strength(basic):
    return basic * random.randint(2, 4)

def get_enemy_health(basic):
    return basic * random.randint(3, 5)


def get_enemy_name():
    return NAMES_BASE[random.randint(0, len(NAMES_BASE) - 1)]
    

def evoke_hangman():
    mark = '\033[31m' + '\u2620' + '\033[0m'
    hangman = { "name": get_enemy_name(), 
                "type": "Wisielec", 
                "strength": get_enemy_strength(1), 
                "health": get_enemy_health(1), 
                "coords": list() }
    return hangman, mark


def evoke_tic_tac_toe():
    mark = '\033[31m' + '\u26d2' + '\033[0m'
    tic_tac_toe = { "name": get_enemy_name(), 
                "type": "XO", 
                "strength": get_enemy_strength(2), 
                "health": get_enemy_health(2), 
                "coords": list() }
    return tic_tac_toe, mark
    

def evoke_zombie_sailor():
    mark = '\033[31m' + '\u26f4' + '\033[0m'
    zombie_sailor = { "name": get_enemy_name(), 
                "type": "Marynarz Zombie", 
                "strength": get_enemy_strength(3), 
                "health": get_enemy_health(3), 
                "coords": list() }
    return zombie_sailor, mark
    

def evoke_agent_smith():
    mark = '\033[31m' + '\u26c7' + '\033[0m'
    agent_smith = { "name": "Agent Smith", 
                "type": "Matrix", 
                "strength": get_enemy_strength(4), 
                "health": get_enemy_health(4), 
                "coords": list() }
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
    #board[coordinations[0]][coordinations[1]] = "\u001B[31m" + sign + "\u001b[0m"
    board[coordinations[0]][coordinations[1]] = sign
    return board


def create_enemies(board, level = 1, number = 2):
    
    enemies = list()
    for i in range(number):
        match level:
            case 1:
                enemy, mark = evoke_hangman()
                enemies.append(enemy)
            case 2:
                enemy, mark = evoke_tic_tac_toe()
                enemies.append(enemy)
            case 3:
                enemy, mark = evoke_zombie_sailor()
                enemies.append(enemy)
            case 4:
                enemy, mark = evoke_agent_smith()
                enemies.append(enemy)
            case 5:
                enemy, mark = evoke_milestone()
        enemy_starting_position = find_empty_board_position(board)
        enemies[i]["coords"] = enemy_starting_position
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
