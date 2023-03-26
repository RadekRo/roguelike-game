import util
from textwrap import dedent


PLAYER_CLASSES = {
                "1": "KANDYDAT", 
                "2": "STUDENT", 
                "3": "MENTOR"
                 }
CLASS_CHARACTERISTICS = { 
                        "KANDYDAT": 
                            {"strength": 5, "mana": 2, "health": 15},
                        "STUDENT":
                            {"strength": 4, "mana": 5, "health": 20},
                        "MENTOR":
                            {"strength": 3, "mana": 10, "health": 10}
                        }

def show_player_class_description(user_name, user_class):
    print(f"{user_name} - wybrałeś klasę: {user_class}")
    match user_class:
        case "KANDYDAT":
            print(dedent('''
                    To ambitny i pełen wigoru osobnik, 
                    który nie może doczekać się nowych
                    wyzwań!
              
                    Zawsze też w wolnej chwili wymyka się 
                    do pobliskiej karczmy, aby posłuchać 
                    nowych, ciekawych historii i wypić kufel 
                    zimnego piwa!
                    '''))
        case "STUDENT":
            print(dedent('''
                    To już nieco doświadczony w bojach osobnik, 
                    rozważniej dobierajacy ekwipunek i studiujący 
                    dokładniej mapy niezdobytych jeszcze przez 
                    niego terenów.
            
                    Pomimo jego roztropności, świat ciągle 
                    go zadziwia i stawia przed nim nowe wyzwania.
                    '''))
        case "MENTOR":
            print(dedent('''
                    Jego liczne blizny świadczą o wielu bojach,
                    o których chętnie opowiada, ucząc co gorliwszych, 
                    by bardziej roztropnie stawiali swoje kroki w 
                    świecie przygody. 
              
                    Pomimo wielkiej wiedzy i on czasem musi się 
                    zatrzymać i pomedytować nad ogniskiem by 
                    doznać inspiracji.
                    '''))
            
    input("Naciśnij [ENTER], aby przejść dalej...")
  
# def draw_line(dots, spaces):
#     dot = "."*dots
#     space = " "*spaces
#     print(f"\n{space}Xx{dot}xXx{dot}xX")

def get_input_validation(user_input, type):
    match type:
        case "name":
            return user_input.isalpha()
        case "class":
            return int(user_input) > 0 and int(user_input) < 4
        case _:
            raise TypeError("Unknown input data!")    

def get_user_input(announcement, type):
    user_input = input(announcement)
    user_input_validated = get_input_validation(user_input, type)
    return user_input if user_input_validated else False

def get_player_class(player_class):
    return PLAYER_CLASSES[player_class]

def get_player_strength(player_class):
    return CLASS_CHARACTERISTICS[player_class]["strength"]

def get_player_mana(player_class):
    return CLASS_CHARACTERISTICS[player_class]["mana"]

def get_player_health(player_class):
    return CLASS_CHARACTERISTICS[player_class]["health"]


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = dict()
    player_name = player_class = False

    while player_name == False:
        player_name = get_user_input("Wpisz swoje miano: ", "name")
        not player_name and print("Spróbuj ponownie! Wprowadzaj wyłącznie litery, bez odstępów.") 
    player["name"] = player_name.upper()
    util.clear_screen()
    
    while player_class == False:
        player_class = get_user_input(dedent(f'''
        Wybierz klasę postaci:
        (1) {PLAYER_CLASSES["1"]} 
        \t[siła: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["1"]]["strength"]}, mana: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["1"]]["mana"]}, zdrowie: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["1"]]["health"]}]
        (2) {PLAYER_CLASSES["2"]} 
        \t[siła: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["2"]]["strength"]}, mana: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["2"]]["mana"]}, zdrowie: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["2"]]["health"]}]
        (3) {PLAYER_CLASSES["3"]}
        \t[siła: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["3"]]["strength"]}, mana: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["3"]]["mana"]}, zdrowie: {CLASS_CHARACTERISTICS[PLAYER_CLASSES["3"]]["health"]}]
        Kim będziesz {player["name"]} (1-3)? '''), "class")
        not player_class and print("Spróbuj ponownie! Pamiętaj, wprowadź tylko liczbę od 1 do 3!")
    player["class"] = get_player_class(player_class)
    player["strength"] = get_player_strength(player["class"])
    player["mana"] = get_player_mana(player["class"])
    player["health"] = get_player_health(player["class"])
    util.clear_screen()

    show_player_class_description(player["name"], player["class"])

    return player