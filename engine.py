import random, csv, os

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

# calling function for testing purposes only.     
# create_enemy(30, 20)

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
    inventory = {}
    inventory["MEDICNE"] = 5
    inventory["FOOD"] = 15
    inventory["DRINK"] = 100
    inventory["MANA"] = 10
    return inventory
    
def display_inventory(inventory):
    for item in inventory:
        print(f"{item}: {inventory[item]}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print(inventory)

def remove_from_inventory(inventory, removed_items):
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] == 0:
                del inventory[item]
    return inventory

def print_inventory_table(inventory, order):
    print("""
-----------------
item name | count
-----------------""")
    order = order.replace(" ", "")
    if order == "empty":
        for item in inventory:
            print(f"{item} | {inventory[item]}")
    elif order == "count,asc":
        sorted_dictionary = sorted(inventory.items(), key=select_value_of_key)
        for item in sorted_dictionary:
            print(f"{item[0]} | {item[1]}")
    elif order == "count,desc":
        sorted_dictionary = sorted(inventory.items(), key=select_value_of_key)
        reversed_dictionary = sorted_dictionary[::-1]
        for item in reversed_dictionary:
            print(f"{item[0]} | {item[1]}")
        
def select_value_of_key(item):
    return item[1]
    
inventory = create_item()
display_inventory(inventory)
print_inventory_table(inventory, "count,desc")

    
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
