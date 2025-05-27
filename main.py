import pygame
import ressources
from home import home_page
from game import game_page, player
from pause import pause_page
from options import options_page
from quitter import quitter_page

pygame.init()

#Paramètres d'affichage et audio
resolution = (950,600)
screen_width, screen_height = resolution
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Treasure Recovery")

ressources.back_sound.play(-1) #133000

#### PAGES DU JEU ####
pages = [home_page, game_page, pause_page, options_page, quitter_page]
current_page_name = "home"
current_page_content = pages[0]
previous_page_name = "home"

### BOUCLE PRINCIPALE ###
### BOUCLE PRINCIPALE ###
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            current_page_name, previous_page_name = current_page_content.manage_buttons(current_page_name, previous_page_name)
            print(f"from {previous_page_name} to {current_page_name}")

        if event.type == pygame.KEYDOWN :
            if current_page_name == "game" :
                if event.key == pygame.K_SPACE :
                    player.is_jumping = True
                    ressources.jump_sound.play() 
                
                if event.key == pygame.K_p :
                    if current_page_name == "game" :
                        current_page_name = "pause"
                    
                    elif current_page_name == "pause" :
                        current_page_name = "game"


    ###Navigation entre les pages
    if current_page_name == "home" :
        current_page_content = pages[0]

    elif current_page_name == "game" :
        current_page_content = pages[1]

    elif current_page_name == "pause" :
        current_page_content = pages[2]

    elif current_page_name == "options" :
        current_page_content = pages[3]

    elif current_page_name == "quitter" :
        current_page_content = pages[4]

    current_page_content.draw_content(screen, previous_page_name)
    pygame.display.flip()

pygame.quit()