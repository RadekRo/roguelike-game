import random
from util import clear_screen

def create_board(width, height):
    board = list()
    board_fill = 0
    for i in range(height):
        row = list()
        for j in range(width):
            row.append(board_fill)
        board.append(row)
    return board

    
def put_player_on_board(board, player):
    board[player["coordinates"][0]][player["coordinates"][1]] = player["icon"]
    return board


def get_board_edges(board):
    left_edge = upper_edge = 0
    right_edge = len(board[0])
    lower_edge = len(board)
    return upper_edge, lower_edge, left_edge, right_edge


def move_player(key, player, board, enemies):
    
    player_x, player_y = player["coordinates"]
    upper_edge, lower_edge, left_edge, right_edge = get_board_edges(board)
    player_hits_the_wall = False 
    
    match key:
        case "w":
            if player_x - 1 >= upper_edge:
                player["coordinates"] = [player_x - 1, player_y]
                player, fight = interaction_on_board(player, enemies, board[player_x - 1][player_y])
                board[player_x - 1][player_y] = player["icon"]
                board[player_x][player_y] = 0    
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case "s":    
            if player_x + 1 <= lower_edge - 1:
                player["coordinates"] = [player_x + 1, player_y]
                player, fight = interaction_on_board(player, enemies, board[player_x + 1][player_y])
                board[player_x + 1][player_y] = player["icon"]
                board[player_x][player_y] = 0                 
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case "a":
            if player_y - 1 >= left_edge:
                player["coordinates"] = [player_x, player_y - 1]
                player, fight = interaction_on_board(player, enemies, board[player_x][player_y -1])
                board[player_x][player_y - 1] = player["icon"]
                board[player_x][player_y] = 0
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case "d":
            if player_y + 1 <= right_edge - 1:
                player["coordinates"] = [player_x, player_y + 1]
                player, fight = interaction_on_board(player, enemies, board[player_x][player_y + 1])
                board[player_x][player_y + 1] = player["icon"]
                board[player_x][player_y] = 0
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case _:
            print("unknown command")

    return player, board, player_hits_the_wall, fight

def check_surroundings(coord, board):
    upper_edge, lower_edge, left_edge, right_edge = get_board_edges(board)
    potential_moves = list()
    if coord[0] > upper_edge:
        board[coord[0] - 1][coord[1]] == 0 and potential_moves.append([coord[0] - 1, coord[1]])
    if coord[0] < lower_edge - 1:
        board[coord[0] + 1][coord[1]] == 0 and potential_moves.append([coord[0] + 1, coord[1]])
    if coord[1] > left_edge:
        board[coord[0]][coord[1] - 1] == 0 and potential_moves.append([coord[0], coord[1] - 1])
    if coord[1] < right_edge - 1:
        board[coord[0]][coord[1] + 1] == 0 and potential_moves.append([coord[0], coord[1] + 1])
    return random.choice(potential_moves)


def move_enemies(enemies, board):
    for i in range(len(enemies)):
        current_coords = enemies[i]["coords"]
        new_coords = check_surroundings(current_coords, board)
        enemies[i]["coords"] = new_coords
        board[new_coords[0]][new_coords[1]] = board[current_coords[0]][current_coords[1]]
        board[current_coords[0]][current_coords[1]] = 0


def find(arr, coords):
    for x in arr:
        if x["coords"] == coords:
            return x


def interaction_on_board(player, enemies, sign): # co się dzieje po najechaniu na poszczególne litery
    player_coords = player["coordinates"]
    fight = False
    if sign != 0:
        match sign:
            case "L":
                player["health"] += 1
            case "J":
                player["mana"] += 1
            case "J":
                player["mana"] += 1
            case "S":
                if "SZTYLET" in player["inventory"]:
                    player["inventory"]["SZTYLET"] += 1
                else:
                    player["inventory"]["SZTYLET"] = 1
            case "D":
                if "DZIDA" in player["inventory"]:
                    player["inventory"]["DZIDA"] += 1
                else:
                    player["inventory"]["DZIDA"] = 1            
            case "M":
                if "MIECZ" in player["inventory"]:
                    player["inventory"]["MIECZ"] += 1
                else:
                    player["inventory"]["MIECZ"] = 1
            case "Ł":
                if "ŁUK" in player["inventory"]:
                    player["inventory"]["ŁUK"] += 1
                else:
                    player["inventory"]["ŁUK"] = 1
            case "W" | "X" | "O" | "Z" | "A":
                    fight = True

    return player, fight

def one_on_one(round, player, enemies):
    enemy = find(enemies, player["coordinates"])
    enemy_health = enemy["health"] * '\u2764 '
    print(f'''---------- TWÓJ PRZECIWNIK ----------
{enemy["name"]}, ({enemy["type"]})
SIŁ: {enemy["strength"]}
ZDR: {enemy_health}''') 
    if round%2:
        print("Twój atak!")
        dice = random.randint(1, 6)
        if player["strength"] + dice > enemy["strength"]:
            lost_hp = player["strength"] + dice - enemy["strength"]
            print(f"Trafienie! Co za cios! Przeciwnik traci {lost_hp} pkt. życia!")
        else:
            print("Pech! Nie udaje Ci się zadać obrażeń...")
    else:
        print("Atak przeciwnika!")
        dice = random.randint(1, 6)
        if enemy["strength"] + dice > player["strength"]:
            lost_hp = enemy["strength"] + dice - player["strength"]
            print(f"Trafienie! Czujesz ostry ból. Tracisz {lost_hp} pkt. życia!")
        else:
            print("Szczęśliwe unikasz obrażeń!")

