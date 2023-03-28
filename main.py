import util
from player import create_player
from engine import create_board, put_player_on_board, move_player
from ui import display_board, display_game_info
from graphics import get_game_header, get_level_annoucement, show_game_intro
from inventory import get_items_on_board, display_inventory

BOARD_WIDTH = 40
BOARD_HEIGHT = 10

PLAYER_ICON = '\033[1;36m' + '@' + '\033[0m'
PLAYER_START_X = 9
PLAYER_START_Y = 19

MOVEMENT_KEYS = ["w", "s", "a", "d"]

def main():
    util.clear_screen()
    player = create_player(PLAYER_ICON, [PLAYER_START_X, PLAYER_START_Y])
    board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    #print(f"User validated: {player}")
    
    is_running = True
    level = 1
    door_status = "closed"
    get_game_header()
    board = put_player_on_board(board, player)
    util.clear_screen()
    get_game_header()
    show_game_intro()
    key = " "
    while is_running:
        util.clear_screen()
        get_game_header()
        get_level_annoucement(1)
        current_level = "active"
        wall_hit = False
        while current_level == "active":
            util.clear_screen()
            get_game_header()
            display_game_info(player)
            #display_board(board, door_status)
            #input("naciśnij dowolny klawisz żeby zobaczyć przedmioty")
            #util.clear_screen()
            #get_game_header()
            #get_items_on_board(board, level)
            display_board(board, door_status)
            #display_inventory(player["inventory"])
            print(f"key pressed {key}")
            if wall_hit:
                print("Zdrowo przydzwoniłeś(aś) w ścianę. Tracisz 1 pkt życia. Uważaj!")
            key = util.key_pressed()
            if key in MOVEMENT_KEYS:
                player, board, wall_hit = move_player(key, player, board)
            if key == "q":
                current_level = "off"
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
