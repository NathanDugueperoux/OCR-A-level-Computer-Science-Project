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


                    
