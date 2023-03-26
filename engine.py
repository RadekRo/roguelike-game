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
   
# jak połączyć to co zbieramy z planszy z wartościami w inventory? (add i remove?)

# added_items = "kupa", "kupa", "miecz", "łuk"
added_items = {"kupa": 13, "MANA": 3, "strzały": 5}
removed_items = {"kupa": 12, "MANA": 1, "strzały": 5}

def create_item(): # Greg
    # to jest inwentarz przedmiotów które można zbierać na planszy (dopisać narzędzia bojowe?)
    inventory = {}
    inventory["MEDICNE"] = 1
    inventory["FOOD"] = 1
    inventory["DRINK"] = 1
    inventory["MANA"] = 1
    return inventory
    
def display_inventory(inventory):
    for item in inventory:
        print(f"{item}: {inventory[item]}")

def add_to_inventory(inventory, added_items):
    # tu chyba trzeba dopisać funkcję która będzie dodawała punkty do poszczególnych rzeczy w inwentarzu
    for item in added_items:
        if item in inventory:
            inventory[item] += added_items[item]
        else:
            inventory[item] = added_items[item]
    print(inventory)

def remove_from_inventory(inventory, removed_items):
    # tu trzeba dopisać jak poszczególne rzeczy będą ubywać w walce lub w trakcie np chodzenia
    for item in removed_items:
        if item in inventory:
            inventory[item] -= removed_items[item]
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

def import_inventory(inventory, filename = "inventory.csv"):
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            csvreader = csv.reader(file, skipinitialspace=True)
            for row in csvreader:
                for i in range(0, len(row)):
                    if row[i] in inventory:
                        inventory[row[i]] += 1
                    else:
                        inventory[row[i]] = 1
        print(inventory)
    else:
        print(f"File '{filename}' not found!")
            
def export_inventory(inventory, filename = "inventory.csv"):
    export_data = []
    for item in inventory:
        for i in range(0, inventory[item]):
            export_data.append(item)
    try:
        with open(filename, "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(export_data)
        print("Data export done!")
    except:
        print(f"You don't have permission creating file '{filename}'!")

# testowanie funkcji importu i exportu, add i remove from inventory  
inventory = {}
import_inventory(inventory, "inventory.csv")
print_inventory_table(inventory, "count,desc")
inventory = create_item()
print_inventory_table(inventory, "count,desc")
add_to_inventory(inventory, added_items)
print_inventory_table(inventory, "count,desc")
export_inventory(inventory, "inventory.csv")
print_inventory_table(inventory, "count,desc")
remove_from_inventory(inventory, removed_items)
print_inventory_table(inventory, "count,desc")
export_inventory(inventory, "inventory.csv")
import_inventory(inventory, "inventory.csv")
print_inventory_table(inventory, "count,desc")

    
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
