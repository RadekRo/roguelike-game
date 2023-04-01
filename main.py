import util
from player import create_player, is_player_dead
from enemies import create_enemies
from engine import create_board, put_player_on_board, move_player, move_enemies, one_on_one
from ui import display_board, display_game_info, door
from graphics import get_game_header, get_level_annoucement, show_game_intro, print_skull_and_bones, show_game_legend
from inventory import get_items_on_board, display_inventory
import time

BOARD_WIDTH = 40
BOARD_HEIGHT = 10

PLAYER_ICON = '\033[1;36m' + '\u26f9' + '\033[0m'
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
    get_game_header()
    board = put_player_on_board(board, player)
    util.clear_screen()
    get_game_header()
    show_game_intro()
    key = " "
    
    while is_running:
        door_status = "closed"
        util.clear_screen()
        get_game_header()
        get_level_annoucement(level)
        current_level = "active"
        wall_hit = False
        inventory = False
        get_items_on_board(board, level)
        board, enemies = create_enemies(board, level, 1)
        moves = 1
        while current_level == "active":
            if len(enemies) == 0:
                door_status = "open"
            util.clear_screen()
            get_game_header()
            display_game_info(player)
            display_board(board, door_status)
            inventory == True and display_inventory(player["inventory"])
            #print(f"key pressed {key}")
            if wall_hit:
                print("Zdrowo przydzwoniłeś(aś) w ścianę. Tracisz 1 pkt życia. Uważaj!")
            key = util.key_pressed()
            if key in MOVEMENT_KEYS:
                door_coordinates = door(board, 6) if len(enemies) < 1 else [0, 0]
                if player["coordinates"] in door_coordinates and door_status == "open" and key == "w":
                    level += 1
                    current_level = "inactive"
                    continue
                player, board, wall_hit, fight = move_player(key, player, board, enemies)
                if fight:
                    round = 1
                    count_enemies = current_enemies = len(enemies)
                    while count_enemies == current_enemies:
                        util.clear_screen()
                        get_game_header()
                        display_game_info(player, False)
                        player, enemies = one_on_one(round, player, enemies)
                        current_enemies = len(enemies)
                        time.sleep(2)
                        round += 1
                util.clear_screen()
                get_game_header()
                display_game_info(player)
                display_board(board, door_status)
              
                inventory == True and display_inventory(player["inventory"])
                if moves % 2 == 0: 
                    move_enemies(enemies, board)
                moves += 1
            if key == "i":
                inventory = True if inventory == False else False
            if key == "l":
                show_game_legend()
                input("Naciśnij ENTER, aby ukryć legendę")
            if key == "q":
                current_level = "off"
                is_running = False
            player_dead = is_player_dead(player)
            if player_dead == True:
                current_level = "inactive"
                is_running = False
    
    if player_dead == True:
        util.clear_screen()
        print_skull_and_bones()
        print("Zginąłeś!")
    print("GAME OVER")


if __name__ == '__main__':
    main()
