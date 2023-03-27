import util
from player import create_player
from engine import create_board, put_player_on_board
from ui import display_board, display_game_info
from graphics import get_game_header, get_level_annoucement, show_game_intro

BOARD_WIDTH = 40
BOARD_HEIGHT = 10

PLAYER_ICON = '\033[1;36m' + '@' + '\033[0m'
PLAYER_START_X = 9
PLAYER_START_Y = 19

def main():
    util.clear_screen()
    player = create_player(PLAYER_ICON, [PLAYER_START_X, PLAYER_START_Y])
    board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    print(f"User validated: {player}")
    
    is_running = True
    level = 1
    door_status = "closed"
    
    while is_running:
        get_game_header()
        level = 1
        board = put_player_on_board(board, player)
        show_game_intro()
        util.clear_screen()
        get_game_header()
        get_level_annoucement(1)
        util.clear_screen()
        get_game_header()
        display_game_info(player)
        display_board(board, door_status)
        is_running = False
        # key = util.key_pressed()
        # if key == 'q':
        #     is_running = False
        # else:
        #     pass
    #util.clear_screen()
    print("GAME OVER")


if __name__ == '__main__':
    main()
