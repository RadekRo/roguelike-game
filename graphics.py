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

def print_skull_and_bones():
    print('''
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
''')

print_skull_and_bones()