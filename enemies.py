import random

NAMES_BASE = ["Kai", "Eliana", "Jayden", "Ezra", "Luca", "Rowan", "Nova", "Amara", "Aaliyah", "Finn", "Zion", "Maeve", "Kayden", "Mia", "Mila", "Aurora", "Alina", "Remi", "Amaya", "Ari", "Blake", "Elliot", "Ivy", "Quinn", "Leo", "Arthur", "Rachel", "River", "Axel", "Aria", "Alex", "Molly", "Jude", "Elias", "Milo", "Malachi", "Charlie", "Ira", "Atlas", "Evelyn"] 

class Enemy:
  def __init__(self, name, type, level = 1):
    self.name = name
    self.type = type
    self.strength = level * random.randint(2, 4)
    self.health = level * random.randint(3, 5)
    self.coords = list()

  def __str__(self):
    return f"Name: {self.name}\nMonster class: '{self.type}'\nStrength: {self.strength}\nHealth: {self.health}\nStarting position: {self.coords}\n"

def get_enemy_name():
    return NAMES_BASE[random.randint(0, len(NAMES_BASE) - 1)]
    
def evoke_hangman():
    name = get_enemy_name()
    hangman = Enemy(name, "Wisielec")
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
    enemies = dict()
    match level:
        case 1:
          for i in range(number):
             enemies[i] = evoke_hangman()
        case 2: 
          enemy_nickname = "XO"
        case 3:
          enemy_nickname = "Zombie marynarz"
        case 4:
          enemy_nickname = "Agent"
        case 5:
          enemy_nickname = "Lord Milestone"
    return enemies      

enemies = create_enemy(1, 3)
print(enemies[0], enemies[1], enemies[2])