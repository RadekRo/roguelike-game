import random
# DO NOT MODIFY FUNCTIONS AND CLASS BELOW - part of a create enemy function!

NAMES_BASE = ["Janek", "Marcin", "Bartek", "Siergiej", "Sebastian", "Ryszard", "Jakub", "Marek"] 

class Enemy:
  def __init__(self, name, type, level = 1):
    self.name = name
    self.type = type
    self.strength = level * random.randint(2, 4)
    self.health = level * random.randint(3, 5)
    self.coords = list()

  def __str__(self):
    return f"Name: {self.name}\nMonster class: /{self.type}/\nStrength: {self.strength}\nHealth: {self.health}\nStarting position: {self.coords}"

def get_enemy_name():
    return NAMES_BASE[random.randint(0, len(NAMES_BASE) - 1)]
    
def evoke_hangman():
    name = get_enemy_name()
    hangman = Enemy(name, "hangman")
    return hangman

def evoke_tic_tac_toe(mark):
    name = mark
    tic_tac_toe = Enemy(name, "tic-tac-toe", 2)
    return tic_tac_toe

def evoke_zombie_sailor():
    name = get_enemy_name()
    zombie_sailor = Enemy(name, "zombie-sailor", 3)
    return zombie_sailor

def evoke_agent_smith():
    name = "Agent Smith"
    agent = Enemy(name, "virus", 4)
    return agent

def evoke_milestone():
    #TODO Boss instance, create when the main functions will be operative
    pass

def create_enemy(level = 1, number = 2):
    print(evoke_hangman())
    
create_enemy(30, 20)

def create_board(width, height): # Greg
    board = list()
    board_fill = 0
    for i in range(height):
        row = list()
        for j in range(width):
            row.append(board_fill)
        board.append(row)
    return board
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
   

def create_item(): # Greg
    healing_items = {}
    healing_items["MEDICNE"] = 10
    healing_items["FOOD"] = 10
    healing_items["DRINK"] = 10
    healing_items["MANA"] = 10
    
    fight_items = dict()
    
    return healing_items


    
def print_statistics(statistics, name):
    
    print(f"\n TWOJE STATYSTYKI! {name}")
    print("+---+---+---+---+---+\n")
    for i, c in statistics.items():
        print(f"{i:>9} |  {c:>4}\n")
    print("+---+---+---+---+---+\n")
        

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    name = input("Wpisz swoje miano: ").upper()
    print(name)
    print(f"Kim jesteć {name}? Rasy do wyboru [ELF, KRASNOLUD, MAG, RYCERZ]")
    input("Wybierz rasę! ").upper()
    stats = get_statistics()
    print_statistics(stats, name)
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
