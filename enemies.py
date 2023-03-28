import random

NAMES_BASE = ["Janek", "Marcin", "Bartek", "Siergiej", "Sebastian", "Ryszard", "Jakub", "Marek"] 

class Enemy:
  def __init__(self, name, type, level = 1):
    self.name = name
    self.type = type
    self.strength = level * random.randint(2, 4)
    self.health = level * random.randint(3, 5)
    self.coords = list()

  def __str__(self):
    return f"Name: {self.name}\nMonster class: /{self.type}/\nStrength: {self.strength}\nHealth: {self.health}\nStarting position: {self.coords}"

def get_enemy_name():
    return NAMES_BASE[random.randint(0, len(NAMES_BASE) - 1)]
    
def evoke_hangman():
    name = get_enemy_name()
    hangman = Enemy(name, "hangman")
    return hangman

def evoke_tic_tac_toe(mark):
    name = mark
    tic_tac_toe = Enemy(name, "tic-tac-toe", 2)
    return tic_tac_toe

def evoke_zombie_sailor():
    name = get_enemy_name()
    zombie_sailor = Enemy(name, "zombie-sailor", 3)
    return zombie_sailor

def evoke_agent_smith():
    name = "Agent Smith"
    agent = Enemy(name, "virus", 4)
    return agent

def evoke_milestone():
    #TODO Boss instance, create when the main functions will be operative
    pass

def create_enemy(level = 1, number = 2):
    print(evoke_hangman())