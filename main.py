import util
from player import create_player
from engine import create_board, put_player_on_board
from ui import display_board

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

def main():
    player = create_player(PLAYER_ICON, [PLAYER_START_X, PLAYER_START_Y])
    board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    print(f"User validated: {player}")
    is_running = True
    while is_running:
        board = put_player_on_board(board, player)
        display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
    util.clear_screen()
    print("GAME OVER")


if __name__ == '__main__':
    main()
