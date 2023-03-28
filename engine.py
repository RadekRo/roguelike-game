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

# testing values and print
player = {"coordinations": [0, 3]}
board = [[0] * 5] * 5

def get_board_edges(board):
    left_edge = upper_edge = 0
    right_edge = len(board[0])
    lower_edge = len(board)
    return upper_edge, lower_edge, left_edge, right_edge


def move_player(player, board):
    
    player_x, player_y = player["coordinations"]
    key = key_pressed()
    upper_edge, lower_edge, left_edge, right_edge = get_board_edges(board) 
    match key:
        case "w":
            new_player_position = [player_x - 1, player_y] if player_x - 1 >= upper_edge else False
        case "s":                
            new_player_position = [player_x + 1, player_y] if player_x + 1 <= lower_edge else False
        case "a":
            new_player_position = [player_x, player_y - 1] if player_y - 1 >= left_edge else False
        case "d":
            new_player_position = [player_x, player_y + 1] if player_y + 1 <= right_edge else False
        case "i":
            print("inventory opened")
        case _:
            print("unknown command")

    return player, new_player_position

#testing function call
is_movement_safe = False
while is_movement_safe == False:
    player, is_movement_safe = move_player(player, board)
    print ("Zdrowo przydzwoniłeś(aś) w ścianę. Tracisz 1 punkt życia!") if not is_movement_safe else print ("Player moved")
        

