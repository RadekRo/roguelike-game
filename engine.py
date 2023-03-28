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

def move_player():
    while True:
        key = key_pressed()
        match key:
            case "w":
                print("player moves up")
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
move_player()

