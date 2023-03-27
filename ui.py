def display_game_info(player):
    mana = player["mana"] * '\u2728'
    health = player["health"] * '\u2764 '
    print(f'''SIŁ: {player["strength"]}
MAN: {mana}
ZDR: {health} 
naciśnij [i] aby, obejrzeć ekwipunek''')



def display_board(board, door_status = "closed"):
    wall = "\u2584" * (len(board[0])+2)
    wall = open_door(wall, 6) if door_status == "open" else close_door(wall, 6)
    for row in board:
        wall += "\n\u2588"
        for col in row:
            if col == 0:
                insert = " "
            else:
                insert = col
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
