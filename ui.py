def get_total_strength(player):
    return  player["strength"] + sum(player["inventory"].values())

def display_game_info(player, show_inventory_info = True):
    mana = player["mana"] * '\u2728'
    health = player["health"] * '\u2764 '
    total_strength = get_total_strength(player) if len(player["inventory"]) > 0 else player["strength"]
    
    print(f'''SIŁ: {player["strength"]} ({total_strength})
MAN: {mana}
ZDR: {health}''') 
    
    if show_inventory_info: 
        print("naciśnij [i], aby pokazać/ukryć ekwipunek")
        print("naciśnij [l], aby pokazać legendę gry")


def display_board(board, door_status = "closed"):
    wall = "\u2584" * (len(board[0])+2)
    wall = open_door(wall, 6) if door_status == "open" else close_door(wall, 6)
    for row in board:
        wall += "\n\u2588"
        for col in row:
            insert = " " if col == 0 else col
            wall += insert
        wall += "\u2588"
    print(wall)
    print("\u2580"*(len(board[0])+2))


def open_door(wall, door_size = 4):
    wall = list(wall)
    half_wall = int(len(wall)  / 2) - int(door_size/2)
    for i in range(half_wall, half_wall + door_size):
        wall[i] = " "
    wall = "".join(wall)    
    return wall


def close_door(wall, door_size = 4):
    wall = list(wall)
    half_wall = int(len(wall)  / 2) - int(door_size/2)
    for i in range(half_wall, half_wall + door_size):
        wall[i] = "\033[0;31m" + wall[i] + "\u001b[0m"
    wall = "".join(wall)    
    return wall


def door(board, door_size):
    door_start = int(len(board[0])  / 2) - int(door_size / 2)
    door_coords = list()
    for i in range(door_size):
        door_coords.append([0, door_start + i])
    return door_coords
