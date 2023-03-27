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
            text = "HANGMAN'S REVENGE"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 2:
            text = "TIC-TAC-TOE ATTACK"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 3:
            text = "ZOMBIE FROM THE OCEAN'S DEEP"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 4:
            text = "THE MATRIX"
            space = int(42 / 2 - len(text) / 2)
            return space, text
        case 5:
            text = "MILESTONE CURSE"
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