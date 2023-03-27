import random
from engine import create_board
from ui import display_board


BOARD_WIDTH = 40
BOARD_HEIGHT = 10

def create_items(level): # Greg
    # to jest inwentarz przedmiotów które można zbierać na planszy
    items = dict()
    items["LEKARSTWO"] = level #adds health
    items["JEDZENIE"] = level #adds mana
    items["PICIE"] = level # adds mana
    items["MIECZ"] = level # adds strength
    items["ŁUK"] = level # adds strength
    items["DZIDA"] = level # adds strength
    items["SZTYLET"] = level # adds strength
    return items

def add_coordinates_to_items(items):
    items_with_coordinates = dict()
    for key in items:
        x = random.randint(1, BOARD_HEIGHT-1)
        y = random.randint(1, BOARD_WIDTH-1)
        items_with_coordinates[key] = (x, y)
        # jak wykluczyć powtórzenia koordynat? 
        # for key in items_with_coordinates:
        #   items_with_coordinates.values() - porównywać czy w liście się powtarzają?
    return items_with_coordinates

def put_items_on_board(board, items_with_coordinates):
    for key in items_with_coordinates:
        board[items_with_coordinates[key][0]][items_with_coordinates[key][1]] = key[0]
    return board

def get_items_on_board(board, level):
    items = create_items(level)
    items_with_coordinates = add_coordinates_to_items(items)
    board = put_items_on_board(board, items_with_coordinates)


# jak połączyć to co zbieramy z planszy z wartościami w inventory? (add i remove?)
def player_inventory(player_name):
    player_inventory = dict()
    




added_items = {"kupa": 13, "MANA": 3, "strzały": 5}
removed_items = {"kupa": 12, "MANA": 1, "strzały": 5}

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

door_status = "closed"
items = create_items(3)
print(items)
items_with_coordinates = add_coordinates_to_items(items)
print(items_with_coordinates)
print(items_with_coordinates.values())
board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
board = put_items_on_board(board, items_with_coordinates)
display_board(board, door_status)
