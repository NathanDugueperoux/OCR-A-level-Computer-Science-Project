from initialization import existing_territories
import random

# takes an object and returns creates a dictionary with the key being home territory and the value being a list of territories the home territory can attack.

def find_adjacent_enemy_territories(territory: object):
    adjacent_enemy_territories = {}
    temp = []
    for i in territory.get_info()[3]:
        for j in existing_territories:
            if i == j.get_info()[1]:
                if j.get_info()[0] != territory.get_info()[0]:
                    temp.append(j)
        adjacent_enemy_territories[territory] = temp
    return adjacent_enemy_territories

# takes a list of attackable enemy nodes iterates through the attackable enemy list and
# problem 1: if function recturns none it causes issues

def fortifying_decision_making(enemy_territories: list, team: list):
    priority = None
    difference = 0
    total = 0
    for i in range(len(enemy_territories)):
        for key, value in enemy_territories[i].items():
            for j in value:
                total += j.get_info()[2]
            temp = difference
            difference = total - key.get_info()[2]
            total = 0
            if difference > temp:
                priority = key
    if priority == None:
        priority = team[random.randint(0, len(team)-1)]
    return priority
                    
