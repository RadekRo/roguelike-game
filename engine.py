import random

def create_enemy(number):
    '''
    Creates enemies in the given number.
    Each enemy has it's own characteristic.
    
    '''
    pass

def create_board(width, height): # to będzie robił Greg
    board = []
    board_fill = "~"
    vertical_wall_sign = "||"
    horizontal_wall_sign = "="
    door_sign = "D"
    for i in range(0, height):
        row = []
        row.insert(0, vertical_wall_sign)
        for j in range(0,width):
            row.append(board_fill)
        row.append(vertical_wall_sign)
        board.append(row)
    horizontal_wall = list()
    for i in range(width + 2):
        horizontal_wall.append(horizontal_wall_sign)
    board.insert(0, horizontal_wall)
    board.append(horizontal_wall)
    board[0][random.randint(1, height-1)] = door_sign  
    return board
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
   
print(create_board(10, 10))

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
