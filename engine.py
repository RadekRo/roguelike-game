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

player = {"coordinations": [3, 3]}
board = [[0] * 5] * 5
print(board)

def get_board_edges(board):
    left_edge = upper_edge = 0
    right_edge = len(board[0])
    lower_edge = len(board)
    return upper_edge, lower_edge, left_edge, right_edge


def move_player(player, board):
    while True:
        key = key_pressed()
        current_player_position = player["coordinations"]
        upper_edge, lower_edge, left_edge, right_edge = get_board_edges(board) 
        print(upper_edge, lower_edge, left_edge, right_edge)
        match key:
            case "w":
                new_player_position = [current_player_position[0] - 1, current_player_position[1]]
                print(f"player moves up. before: {current_player_position} next: {new_player_position}")
            case "s":
                print("player moved down")
            case "a":
                print("player moved left")
            case "d":
                print("player moved right")
            case "i":
                print("inventory opened")
            case _:
                print("unknown command")
                break
move_player(player, board)

