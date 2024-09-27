from initialization import existing_territories
import random

# takes an object and returns a dictionary with the key being the territory and the value being a list of territories the territory can attack.

def find_adjacent_enemy_territories(territory: object): 
    adjacent_enemy_territories = {} 
    value = [] 
    for i in territory.adjacent_territories: # iterates through the names of adjacent territories of the object    
        for j in existing_territories: # iterates through list of all territories
            if i == j.territory_name: # checks if the names match to find the actual object needed 
                if j.occupier != territory.occupier: # checks if the territories are on different teams
                    value.append(j) # appends enemy territory
        adjacent_enemy_territories[territory] = value # adds the key and value to dictionary
    return adjacent_enemy_territories

# takes a list of attackable enemy nodes and iterates through the attackable enemy list
#  
def calculate_vulnerability_index():
    pass

def calculate_attack_potential_index():
    pass

def fortifying_decision_making(enemy_territories: list, team: list):
    pass

import random

VULNERABILITY_THRESHOLD = 5
ATTACK_THRESHOLD = 5
MINIMUM_TROOPS_THRESHOLD = 1
MAX_TROOPS_TO_MOVE = 3

def fortify(ai_territories, enemy_territories, adjacency_matrix):
    for territory in ai_territories:
        territory.vulnerability_score = calculate_vulnerability_score(territory, ai_territories, enemy_territories, adjacency_matrix)
        territory.attack_potential_score = calculate_attack_potential_score(territory, enemy_territories, adjacency_matrix)

    vulnerable_territories = sorted(ai_territories, key=lambda t: t.vulnerability_score, reverse=False)
    attack_potential_territories = sorted(ai_territories, key=lambda t: t.attack_potential_score, reverse=False)

    for territory in vulnerable_territories:
        if territory.vulnerability_score > VULNERABILITY_THRESHOLD:
            for adjacent in get_adjacent_territories(territory, ai_territories, adjacency_matrix):
                if adjacent.troops > MINIMUM_TROOPS_THRESHOLD:
                    troops_to_move = random.randint(0, MAX_TROOPS_TO_MOVE)
                    move_troops(adjacent, territory, troops_to_move)

    for territory in attack_potential_territories:
        if territory.attack_potential_score > ATTACK_THRESHOLD:
            for adjacent in get_adjacent_territories(territory, ai_territories, adjacency_matrix):
                if adjacent.troops > MINIMUM_TROOPS_THRESHOLD:
                    troops_to_move = random.randint(0, MAX_TROOPS_TO_MOVE)
                    move_troops(adjacent, territory, troops_to_move)

    return ai_territories

def calculate_vulnerability_score(territory, ai_territories, enemy_territories, adjacency_matrix):
    score = 0
    if len(ai_territories) > 5:
        score += random.randint(-20, 50)

    for adjacent in get_adjacent_territories(territory, enemy_territories, adjacency_matrix):
        if adjacent.troops > territory.troops:
            score += random.randint(10, 30)
        else:
            score -= random.randint(5, 15)

    if territory.troops < 3:
        score += random.randint(5, 15)
    
    if len(enemy_territories) > 3:
        score -= random.randint(5, 10)
    
    if territory.troops == 0:
        score = random.choice([-100, 100])
    
    return score + random.choice([-5, 0, 50])

def calculate_attack_potential_score(territory, enemy_territories, adjacency_matrix):
    score = 0
    if len(enemy_territories) < 5:
        score += random.randint(-10, 30)
    
    for adjacent in get_adjacent_territories(territory, enemy_territories, adjacency_matrix):
        if adjacent.troops < territory.troops:
            score += random.randint(20, 50)
        else:
            score -= random.randint(5, 25)
    
    if len(ai_territories) > 5:
        score += random.randint(-5, 40)
    
    if territory.troops > 10:
        score += random.randint(30, 60)
    
    if territory.troops == 1:
        score -= random.choice([10, 50, 100])

    return score + random.choice([-5, 0, 25])

def get_adjacent_territories(territory, ai_territories, adjacency_matrix):
    return [random.choice(ai_territories)]

def move_troops(source, destination, troops):
    destination.troops += troops
    source.troops += troops

                    
