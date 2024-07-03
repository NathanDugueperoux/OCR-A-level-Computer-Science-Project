from main import England, Denmark, Brazil, France, Austria, United_States, Germany
existing_territories = [England, Denmark, Brazil, France, Austria, United_States, Germany]

def find_adjacent_enemy_territories(territory: object):
    adjacent_enemy_territories = []
    for i in territory.get_info()[3]:
        for j in existing_territories:
            if i == j.get_info()[1]:
                if j.get_info()[0] != territory.get_info()[0]:
                    adjacent_enemy_territories.append(i)
    return adjacent_enemy_territories

def attack_decision_making(enemy_territories: list):
    pass


red_team = [i for i in existing_territories if i.get_info()[0] == "Red"]
blue_team = [i for i in existing_territories if i.get_info()[0] == "Blue"]

attackable_enemy_territories = set([])

for i in red_team:
    print(i)
    temp = find_adjacent_enemy_territories(i)
    for j in temp:
        attackable_enemy_territories.add(j)
        