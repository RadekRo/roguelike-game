import util
import engine
import ui


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
   
def draw_line(dots, spaces):
    dot = "."*dots
    space = " "*spaces
    print(f"\n{space}Xx{dot}xXx{dot}xX")
    
       


def player_stats(player):
    
    
    ASPIRANT = {
        "HEALTH": 50,
        "STRENGTH": 30,
        "MANA": 20,
    }
    
    STUDENT = {
        "HEALTH": 50,
        "STRENGTH": 25,
        "MANA": 15,
    }
    
    MENTOR = {
        "HEALTH": 50,
        "STRENGTH": 15,
        "MANA": 10,
    }
    
    
    if player == "K" or player == "KANDYDAT":
        return ASPIRANT
    elif player == "S" or player == "STUDENT":
        return STUDENT
    elif player == "M" or player == "MENTOR":
        return MENTOR
    
    
def print_statistics(statistics):
    space = " "*25
    for i, c in statistics.items():
        print(space + i,c)
    

def player_class(name_class, name, stats):
    space = " "*23
    if name_class == "K" or name_class == "KANDYDAT":
        print(f"{space}{name} WYBRAŁEŚ/ŁAS KANDYDATA!")
        draw_line(16,14)
        print("""
              To ambitny i pełen wigou osobnik, 
              który nie może doczekać się nowych
              wyzwań!
              
              Zawsze też w wolnej chwili wymyka się 
              do pobliskiej karczmy, by posłuchać 
              nowych ciekawych histori i wypieć kufel 
              zimnego piwa!
              
                        TWOJE STATYSTYKI!
              """)
        print_statistics(stats)
        draw_line(16,14)
        
    elif name_class == "S" or name_class == "STUDENT":
        print(f"{space}{name} WYBRAŁEŚ STUDENTA!")
        draw_line(16,14)
        print("""
            To już nie co doświadczony w bojach osobnik, 
            rozwarzniej dobierajacy ekwipunek i studiujący 
            dokładniej mampy niezdobytych jeszcze przez 
            niego terenów.
            
            Po mimo jego roztropności, świat ciągle 
            go zadziwia i stawia przed nim nowe wyzwania.
            
                        TWOJE STATYSTYKI!
              """)
        print_statistics(stats)
        draw_line(16,14)
        
    elif name_class == "M" or name_class == "MENTOR":
        print(f"{space}{name} WYBRAŁEŚ MENTORA!")
        draw_line(16,14)
        print("""
              Jego liczne blizny światczą o wielu bojach,
              o których chętnie opowiada, ucząć co gorliwszych 
              by bardziej roztropnie stawiali swoje kroki w 
              świecie przygody. 
              
              Po mimo wielkiej wiedzy i on czasem musi się 
              zatrzymać i pomedytować nad ogniskiem by 
              doznać inspiracji.
              
                        TWOJE STATYSTYKI!
              """)
        print_statistics(stats)
        draw_line(16,14)
        
def HP_Player():
    pass

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    run = True
    
    while run:
        draw_line(15,0)
        name = str(input("Wpisz swoje miano: ").upper())
        if not all(x.isalpha or x == "" for x in  name):
            print("Spróbój ponownie.")
        else:
            print(name)
        util.clear_screen()
        draw_line(30,0)
        print(f"Kim jesteć {name}? Klasy do wyboru [KANDYDAT, StUDENT, MENTOR]")
        print("Możesz wpisać pęłną nazwę lub, tylko pierwszą literę.")
        name_class = input("Wybierz Klasę! ").upper()
        util.clear_screen()
        stats = player_stats(name_class)
        print(player_class(name_class, name, stats))
    else:
        run = False
     

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
