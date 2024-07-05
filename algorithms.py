from main import Territories

England = Territories("Red", "England", 5, ["Denmark", "United_States", "France"])
Denmark = Territories("Red", "Denmark", 0, ["England", "United_States", "Brazil"])
Brazil = Territories("Red", "Brazil", 0, ["Denmark"])
United_States = Territories("Red", "United_States", 0, ["Denmark", "England", "France", "Germany"])
France = Territories("Blue", "France", 15, ["England", "United_States", "Germany"])
Germany = Territories("Blue", "Germany", 1, ["France", "United_States", "Austria"])
Austria = Territories("Blue", "Austria", 0, ["Germany"])

existing_territories = [England, Denmark, Brazil, France, Austria, United_States, Germany]

red_team = [i for i in existing_territories if i.get_info()[0] == "Red"]
blue_team = [i for i in existing_territories if i.get_info()[0] == "Blue"]

# creates a dictionary with the key being home territory and the value being a list of territories the home territory can attack.

def find_adjacent_enemy_territories(territory: object):
    adjacent_enemy_territories = {}
    temp = []
    for i in territory.get_info()[3]:
        for j in existing_territories:
            if i == j.get_info()[1]:
                if j.get_info()[0] != territory.get_info()[0]:
                    temp.append(i)
        adjacent_enemy_territories[territory.get_info()[1]] = temp
    return adjacent_enemy_territories

def fortifying_decision_making(enemy_territories: list):
    priority = None
    difference = 0
    total = 0
    for i in range(len(attackable_enemy_territories)):
        for key, value in attackable_enemy_territories[i].items():
            for j in existing_territories:
                if key == j.get_info()[1]:
                    for k in value:
                        for l in existing_territories:
                            if k == l.get_info()[1]:
                                total += l.get_info()[2]
                    temp = difference
                    difference = total - j.get_info()[2]
                    if difference > temp:
                        priority = j
    return priority
                    

# iterates through the red team list and runs each item through find_adjacent_enemy_territories() putting resulting dictionary in the list attackable_enemy_territories.

attackable_enemy_territories = []

for i in red_team: 
    if find_adjacent_enemy_territories(i)[i.get_info()[1]] == []:
        pass
    else:
        attackable_enemy_territories.append(find_adjacent_enemy_territories(i))

# test

print(attackable_enemy_territories)

print(fortifying_decision_making(attackable_enemy_territories).get_info()[1])