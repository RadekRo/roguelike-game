import sys

def get_game_header():
    print('''\033[1;31m
   ______          __                      __
  / ____/___  ____/ /__  _________  ____  / /
 / /   / __ \/ __  / _ \/ ___/ __ \/ __ \/ / 
/ /___/ /_/ / /_/ /  __/ /__/ /_/ / /_/ / /  
\____/\____/\__,_/\___/\___/\____/\____/_/   \033[1;36m
       /_  __/___ _      _____  _____              
        / / / __ \ | /| / / _ \/ ___/              
       / / / /_/ / |/ |/ /  __/ /                  
      /_/  \____/|__/|__/\___/_/    \033[0m
------------------------------------------
 \033[1;31mA GAME BY GRAMA Team. Copyright (c) 2023\033[0m
------------------------------------------''')

def get_level_annoucement(level):
    if level == 6:
        quit()
        
    space, text = get_level_description(level)
    space = " " * space
    input(f'''

                 \033[1;31mPOZIOM {level}
{space}{text}\033[0m
    
\033[1;36mNaciśnij [ENTER] aby kontynuować...''')

def get_level_description(level):
    match level:
        case 1:
            text = "ZEMSTA WISIELCA"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 2:
            text = "MASAKRA KÓŁKA I KRZYŻYKA"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 3:
            text = "MARYNARZE ZOMBIE"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 4:
            text = "MATRIX"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 5:
            text = "KLĄTWA MILESTONE'A"
            space = int(42 / 2 - len(text) / 2)
            return space, text 
        
def show_game_intro():
    input('''\033[3m
Nie ma teraz znaczenia co wcześniej 
łączyło Cię z Codecool.
Jesteś studentem, mentorem, 
a może dopiero kandydatem?
Budzisz się na kamiennej podłodze, 
a wokół Ciebie zaczyna się koszmar.
Zmierz się z kolejnymi wyzwaniami, 
dopadnij krwiożerczego Milestone'a
i pomścij tych, którzy polegli przed Tobą...\u001B[0m

\033[1;36mNaciśnij [ENTER] aby kontynuować...''')
    
def show_game_legend():
    print('''Do poruszania się po planszy używaj klawiszy:
             - [W] - ruch w górę
             - [S] - ruch w dół
             - [A] - ruch w lewo
             - [D] - ruch w prawo
            
            \033[31mWszytkie ikony na czerwono to Twoi wrogowie,\033[0m jeśli się do nich zbliżysz czeka Cię walka.
            \033[33mWszystkie ikony na żółto to bronie\033[0m (dodają Ci siły do walki), 
            sprawdź inwentarz [i], żeby zobaczyć co znalazłeś
            \033[32mIkony na zielono dodają odpowiednio zdrowia\033[0m (lekarstwo) \033[32mi many \033[0m(jedzenie i picie).
            To ile masz zdrowia, siły i many widać nad planszą.
            Pokonaj wszystkich wrogów aby móc otworzyć drzwi i wyjść do kolejnego poziomu.
             ''')

def print_skull_and_bones():
    print('''\033[31m
MMMMMMMMMMMMMMMMMMMMMWNK00000KXWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWXkl;'..   ...,cxKWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNk:.               .;dXMMMMMMMMMMMM
MMMMMMMMMMMMMWO;                     'xNMMMMMMMMMM
MMMMMMMMMMM0'                           .xMMMMMMMM
MMMMMMMMMMM0'   ;dkOkdc.     .:oxOkxc.  .xMMMMMMMM
MMMMMMMMMMMX;  :XMMMMMMx.    cWMMMMMWo  .OMMMMMMMM
MMMMMMMMMMMWl  ,0WMMMMX:     ,0MMMMMXc  ;XMMMMMMMM
MMMMMMMMMMMMO.  .:oddl'   ..  .cdxoc'  .dWMMMMMMMM
MMMMMMMMMMMMWk'         ,d0Xc         .dNMMMMMMMMM
MMMMMMMMMMMMMMXko,      lKXXx.     'lxKWMMMMMMMMMM
MMMMMWX00KWMMMMMMNo.    .....     :XMMMMMMWX00KWMM
MMMMXl.. .;kNMMMMMNc.            ;KMMMMMW0c.  .:0M
MMMMK:      cKMMMMMNOl;:' ''.;;ckXMMMMMNd.     ,OM
MMMMMK,      .o0NMMMMWWWX0XXKNWWMMMMWKd,      .kMM
MMMMWo         .':dkKWMMMMMMMMMWXOdc,.         :XM
MMMMWk;........     .,cok0KXOdc;.     ........,dNM
MMMMMMWXKXXNXK0Oxl:'     ...     .;cdk0KXXXXKXNMMM
MMMMMMMMMMMMWXKOdl:'       .     .:ldk0XNWMMMMMMMM
MMMMW0olllc:,..     .';lxkO0xo:'.     ..';cllllOWM
MMMM0,         .':ok0NWMMMMMMMMNKkoc,.         .kM
MMMMX:      .:d0NMMMMMMMMMMMMMMMMMMMWKkc.      .OM
MMMMMK,   .c0WMMMMMMMMMMMMMMMMMMMMMMMMMMXo.   .kWM
MMMMMMO;,:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,,xNMM
\033[0m''')


def print_you_win():
    print('''   
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###############(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###%%%#########(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########%%%#########(((######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########%%%#########(((######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@###%%%#########(((@@@###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########%%%######(((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@   @@@.  &@@@@       (@@@@   @@@@#  *@@@@@@@@@@   @@@@&   @@@         @@@   @@@@.  #@@*  #@@@
@@@@@@@   @@@.  &@@.  &@@@@   @@@   @@@@#  *@@@@@@@@@@   @@(@&   @@@@@@   @@@@@@    ((@.  %@@*  %@@@
@@@@@@@@@      @@@@.  &@@@@   @@@   @@@@#  *@@@@@@@@@@           @@@@@@   @@@@@@          %@@*  %@@@
@@@@@@@@@@   &@@@@@.  &@@@@   @@@   @@@@(  *@@@@@@@@@@    .@     @@@@@@   @@@@@@   @@@    %@@@@@@@@@
@@@@@@@@@   *&@@@@@@@       %@@@@@         @@@@@@@@@@@@@  @@@@  @@@@@        @@@   @@@@   %@@   &@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
    
def print_congrats():
    print(''' '\033[33m'
         ____                            _       _         
        / ___|___  _ __   __ _ _ __ __ _| |_ ___| |        
       | |   / _ \| '_ \ / _` | '__/ _` | __/ __| |        
       | |__| (_) | | | | (_| | | | (_| | |_\__ |_|        
        \____\___/|_| |_|\__, |_|  \__,_|\__|___(_)        
                         |___/                             
     \033[0m         \033[32m                            _              _ 
  _   _  ___  _   _   _ __ ___  __ _  ___| |__   ___  __| |
 | | | |/ _ \| | | | | '__/ _ \/ _` |/ __| '_ \ / _ \/ _` |
 | |_| | (_) | |_| | | | |  __| (_| | (__| | | |  __| (_| |
  \__, |\___/ \__,_| |_|  \___|\__,_|\___|_| |_|\___|\__,_|
  |___/                                                    
                                __ _          _            
      _   _  ___  _   _ _ __   / _(_)_ __ ___| |_          
     | | | |/ _ \| | | | '__| | |_| | '__/ __| __|         
     | |_| | (_) | |_| | |    |  _| | |  \__ | |_          
      \__, |\___/ \__,_|_|    |_| |_|_|  |___/\__|         
      |___/     \033[0m         \033[31m                                   
              _ _          _                   _ _ _       
    _ __ ___ (_| | ___ ___| |_ ___  _ __   ___| | | |      
   | '_ ` _ \| | |/ _ / __| __/ _ \| '_ \ / _ | | | |      
   | | | | | | | |  __\__ | || (_) | | | |  __|_|_|_|      
   |_| |_| |_|_|_|\___|___/\__\___/|_| |_|\___(_(_(_)\033[0m
''')

def quit():
    print_you_win()
    print_congrats()
    print("Dzięki za grę i do zobaczenia na następnym module CodeCoola.")
    sys.exit(0)