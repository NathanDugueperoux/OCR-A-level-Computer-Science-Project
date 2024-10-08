import pygame 
import sys
from initialization import existing_territories
from algorithms import find_adjacent_enemy_territories, fortifying_decision_making

pygame.init()

pygame.display.set_caption("")
window = pygame.display.set_mode((780, 480))

clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)

england = pygame.Rect(190, 50, 100, 100)
denmark = pygame.Rect(160, 150, 120, 100)
brazil = pygame.Rect(170, 250, 100, 100)
united_states = pygame.Rect(280, 150, 130, 100)
france = pygame.Rect(290, 50, 150, 100)
germany = pygame.Rect(410, 150, 100, 100)
austria = pygame.Rect(510, 150, 100, 130)

while True:

    england_troops = font.render(str(existing_territories[0].amount_of_troops), True, "White")
    denmark_troops = font.render(str(existing_territories[1].amount_of_troops), True, "White")
    brazil_troops = font.render(str(existing_territories[2].amount_of_troops), True, "White")
    united_states_troops = font.render(str(existing_territories[5].amount_of_troops), True, "White")
    france_troops = font.render(str(existing_territories[3].amount_of_troops), True, "White")
    germany_troops = font.render(str(existing_territories[6].amount_of_troops), True, "White")
    austria_troops = font.render(str(existing_territories[4].amount_of_troops), True, "White")

    red_territories = [[england, england_troops], [denmark, denmark_troops], [brazil, brazil_troops], [united_states, united_states_troops]]
    blue_territories = [[france, france_troops], [germany, germany_troops], [austria, austria_troops]]

    window.fill((0,157,196))

    for i in red_territories:
        if i[0].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, (255,0,0), i[0])
            window.blit(i[1], (i[0].x, i[0].y))
        else:
            pygame.draw.rect(window, (200,0,0),i[0])
            window.blit(i[1], (i[0].x, i[0].y))

    for i in blue_territories:
        if i[0].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, (0, 0, 255), i[0])
            window.blit(i[1], (i[0].x, i[0].y))
        else:
            pygame.draw.rect(window, (0, 0, 200), i[0])
            window.blit(i[1], (i[0].x, i[0].y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:

                given_troops = 6

                red_team = [i for i in existing_territories if i.occupier == "Red"] # creates a list of red teams territories
                blue_team = [i for i in existing_territories if i.occupier == "Blue"] # creates a list of blue teams territories
                
                attackable_enemy_territories = []
                
                for i in red_team: 
                    if find_adjacent_enemy_territories(i)[i] == []: # checks if a territory has no enemy territories
                        pass
                    else:
                        attackable_enemy_territories.append(find_adjacent_enemy_territories(i))
                        
                fortifying_decision_making(attackable_enemy_territories, red_team).change_troops(1)

            if event.key == pygame.K_b:

                given_troops = 6

                red_team = [i for i in existing_territories if i.occupier == "Red"] # creates a list of red teams territories
                blue_team = [i for i in existing_territories if i.occupier == "Blue"] # creates a list of blue teams territories
                
                attackable_enemy_territories = [] 
                
                for i in blue_team: 
                    if find_adjacent_enemy_territories(i)[i] == []: # checks if a territory has no enemy territories
                        pass
                    else:
                        attackable_enemy_territories.append(find_adjacent_enemy_territories(i))

                
                fortifying_decision_making(attackable_enemy_territories, blue_team).change_troops(1)

        
    pygame.display.update()
    clock.tick(60)