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

red_team = [i for i in existing_territories if i.get_info()[0] == "Red"]
blue_team = [i for i in existing_territories if i.get_info()[0] == "Blue"]

enemy_territories = []

for i in red_team:
    enemy_territories.append(find_adjacent_enemy_territories(i))

print(enemy_territories[0][0].get_info())