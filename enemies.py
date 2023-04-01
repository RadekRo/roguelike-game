import random

NAMES_BASE = ["Kai", "Eliana", "Jayden", "Ezra", "Luca", "Rowan", "Nova", "Amara", "Aaliyah", "Finn", "Zion", "Maeve", "Kayden", "Mia", "Mila", "Aurora", "Alina", "Remi", "Amaya", "Ari", "Blake", "Elliot", "Ivy", "Quinn", "Leo", "Arthur", "Rachel", "River", "Axel", "Aria", "Alex", "Molly", "Jude", "Elias", "Milo", "Malachi", "Charlie", "Ira", "Atlas", "Evelyn"] 


def get_enemy_strength(basic):
    return basic * random.randint(1, 5)

def get_enemy_health(basic):
    return int(basic * random.randint(2, 6))


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
                "strength": get_enemy_strength(1.25), 
                "health": get_enemy_health(1.25), 
                "coords": list() }
    return tic_tac_toe, mark
    

def evoke_zombie_sailor():
    mark = '\033[31m' + '\u26f4' + '\033[0m'
    zombie_sailor = { "name": get_enemy_name(), 
                "type": "Marynarz Zombie", 
                "strength": get_enemy_strength(1.5), 
                "health": get_enemy_health(1.5), 
                "coords": list() }
    return zombie_sailor, mark
    

def evoke_agent_smith():
    mark = '\033[31m' + '\u26c7' + '\033[0m'
    agent_smith = { "name": "Agent Smith", 
                "type": "Matrix", 
                "strength": get_enemy_strength(1), 
                "health": get_enemy_health(1), 
                "coords": list() }
    return agent_smith, mark
    

def evoke_milestone():
    mark = '\033[31m' + '#' + '\033[0m'
    milestone = { "name": "Milestone", 
                "type": "exam", 
                "strength": get_enemy_strength(0.25), 
                "health": get_enemy_health(0.25), 
                "coords": list() }
    return milestone, mark


def find_empty_board_position(board):
    empty_slot = False
    while empty_slot == False:
        enemy_x = random.randint(0, len(board) - 1)
        enemy_y = random.randint(0, len(board[0]) - 1)
        if board[enemy_x][enemy_y] == 0:
            empty_slot = True
    return [enemy_x, enemy_y]


def place_enemy_on_board(board, coordinations, sign):
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
                enemies.append(enemy)
        enemy_starting_position = find_empty_board_position(board)
        enemies[i]["coords"] = enemy_starting_position
        board = place_enemy_on_board(board, enemy_starting_position, mark)

    return board, enemies
    
