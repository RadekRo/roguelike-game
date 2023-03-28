from util import key_pressed

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


def move_player(key, player, board):
    
    player_x, player_y = player["coordinates"]
    upper_edge, lower_edge, left_edge, right_edge = get_board_edges(board)
    player_hits_the_wall = False 
    
    match key:
        case "w":
            if player_x - 1 >= upper_edge:
                player["coordinates"] = [player_x - 1, player_y]
                board[player_x - 1][player_y] = player["icon"]
                board[player_x][player_y] = 0    
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case "s":    
            if player_x + 1 <= lower_edge - 1:
                player["coordinates"] = [player_x + 1, player_y]
                board[player_x + 1][player_y] = player["icon"]
                board[player_x][player_y] = 0                    
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case "a":
            if player_y - 1 >= left_edge:
                player["coordinates"] = [player_x, player_y - 1]
                board[player_x][player_y - 1] = player["icon"]
                board[player_x][player_y] = 0
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case "d":
            if player_y + 1 <= right_edge - 1:
                player["coordinates"] = [player_x, player_y + 1]
                board[player_x][player_y + 1] = player["icon"]
                board[player_x][player_y] = 0
            else:
                player_hits_the_wall = True
                player["health"] -= 1
        case _:
            print("unknown command")

    return player, board, player_hits_the_wall

#testing function call
# player, is_movement_safe = move_player(player, board)
# print (f"Zdrowo przydzwoniłeś(aś) w ścianę. Tracisz 1 punkt życia!") if not is_movement_safe else None
# print(player["coordinations"])
        

