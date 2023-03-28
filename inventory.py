import random
from engine import create_board
from ui import display_board

BOARD_WIDTH = 40
BOARD_HEIGHT = 10

PLAYER_START_X = 9
PLAYER_START_Y = 19


def create_items(level): # to jest inwentarz przedmiotów które można zbierać na planszy
    items = dict()
    items["LEKARSTWO"] = level #adds health
    items["JEDZENIE"] = level #adds mana
    items["PICIE"] = level # adds mana
    items["SZTYLET"] = 1 # adds strength
    items["DZIDA"] = 2 # adds strength
    items["MIECZ"] = 3 # adds strength
    items["ŁUK"] = 4 # adds strength
    return items


def add_coordinates_to_items(items): # dodawanie losowych koordynaty do przedmiotów
    items_with_coordinates = dict()
    for key in items:
        x = random.randint(1, BOARD_HEIGHT-1)
        y = random.randint(1, BOARD_WIDTH-1)
        items_with_coordinates[key] = (x, y)
    # wykluczanie powtórzeń
    if len(items_with_coordinates.values()) == len(set(items_with_coordinates.values())):
        if (x, y) == (PLAYER_START_X, PLAYER_START_Y):
            add_coordinates_to_items(items)
        else:
            return items_with_coordinates
    else:
        add_coordinates_to_items(items)


def merge_inventory(items, items_with_coordinates): # łączenie słowników przedmiotów i koordynat z ilością przedmiotów
    merged_inventory = dict(items_with_coordinates)
    for key in items:
        if key in merged_inventory:
            merged_inventory[key] = [merged_inventory[key], items[key]]
        else:
            merged_inventory[key] = items[key]
    return merged_inventory
    

def put_items_on_board(board, merged_inventory): # wkładanie przedmiotów do boarda
    for key in merged_inventory:
        board[merged_inventory[key][0][0]][merged_inventory[key][0][1]] = key[0]
    return board


def get_items_on_board(board, level): # funkcja łącząca funkcje z inventory
    items = create_items(level)
    items_with_coordinates = add_coordinates_to_items(items)
    merged_inventory = merge_inventory(items, items_with_coordinates)
    board = put_items_on_board(board, merged_inventory)


def display_inventory(inventory): # wyświetlanie inwentarza (na razie nie używane)
    for item in inventory:
        print(f"{item} | +{inventory[item]} S")

# testy funkcji w inventory.py
door_status = "closed"
items = create_items(4)
print(items)
items_with_coordinates = add_coordinates_to_items(items)
print(items_with_coordinates)
board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
merged_inventory = merge_inventory(items, items_with_coordinates)
board = put_items_on_board(board, merged_inventory)
display_board(board, door_status)

