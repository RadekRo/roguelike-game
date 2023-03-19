# DO NOT MODIFY FUNCTIONS BELOW - part of a create enemy function!

def evoke_hangman()
  pass
def evoke_tic_tac_toe()
  pass
def evoke_zombie_sailor()
  pass
def evoke_agent_smith()
  pass
def evoke_milestone()
  pass


def create_enemy(number = 2):
    '''
    Creates enemies in the given number.
    Each enemy has it's own characteristic.
    Create at least 2 enemies
    '''
    pass

def create_board(width, height): # to będzie robił Greg
    board = []
    board_fill = "~"
    for i in range(0, height):
        row = []
        for j in range(0,width):
            row.append(board_fill)
        board.append(row)
    return board
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
   
print(create_board(20, 20))

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
