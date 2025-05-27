import pygame

pygame.init()

##### INTERFACE #####
resolution = (950,600)
screen_width, screen_height = resolution

#Couleurs
blue = (68, 172, 225)
green = (3, 83, 40)
yellow = (240, 204, 0)
marron = (164, 108, 34)
white = (255, 243, 201)
black = (5, 17, 21)
black_transp = (5, 17, 21, 0)

#Polices
font_title = pygame.font.Font("font/Montserrat-Bold.ttf", 70)
font_score = pygame.font.Font("font/Montserrat-Bold.ttf", 22)
font_exit = pygame.font.Font("font/Montserrat-Bold.ttf", 40)
font_options = pygame.font.Font("font/Montserrat-Bold.ttf", 24)

##### ELEMENTS DU DECOR ET AUDIO #####
###### PAGE D'ACCUEIL ########
background = pygame.image.load("images/décors/background1.jpg")
background = pygame.transform.scale(background, resolution)

####### PAGE DE JEU ##########
background_2 = pygame.image.load("images/décors/ciel.jpg")
background_2 = pygame.transform.scale(background_2, resolution)

# Images du personnage
stand_image = pygame.image.load("images/persos/player_stand.png")
run_image_1 = pygame.image.load("images/persos/player_run_1.png") 
run_image_2 = pygame.image.load("images/persos/player_run_2.png")
run_image_3 = pygame.image.load("images/persos/player_run_3.png")
run_images = [run_image_1, run_image_2, run_image_3]

stand_image_left = pygame.transform.flip(stand_image, 1, 0)
run_image_left_1 = pygame.transform.flip(run_image_1, 1, 0)
run_image_left_2 = pygame.transform.flip(run_image_2, 1, 0)
run_image_left_3 = pygame.transform.flip(run_image_3, 1, 0)
run_images_left = [run_image_left_1, run_image_left_2, run_image_left_3]

jump_image = pygame.image.load("images/persos/player_run_1.png")
jump_image_left = pygame.transform.flip(jump_image, 1, 0)

tir_image_1 = pygame.image.load("images/persos/player_with_ball_2.png")
tir_image_2 = pygame.image.load("images/persos/player_with_ball_1.png")
tir_images = [tir_image_1, tir_image_2]

tir_image_left_1 = pygame.transform.flip(tir_image_1, 1, 0)
tir_image_left_2 = pygame.transform.flip(tir_image_2, 1, 0)
tir_images_left = [tir_image_left_1, tir_image_left_2]

### Plateformes
platform_image = pygame.transform.scale(pygame.image.load("images/décors/sol.png"), (292, 30))


##### BALLES (CAILLOUX) #####
ball_image = pygame.image.load("images/décors/balle.png")

#Background page d'options
background_3 = pygame.image.load("images/décors/background2.jpg")
background_3 = pygame.transform.scale(background_3, resolution)

#Audio
back_sound = pygame.mixer.Sound("audio/bg007.mp3")
back_sound.set_volume(0.6)

hover_sound = pygame.mixer.Sound("audio/cursor.wav")
hover_sound.set_volume(0.5)
hover_sound_played = [False, False, False]

jump_sound = pygame.mixer.Sound("audio/jump.mp3")
jump_sound.set_volume(0.5)

### GENERAL ###
def center_content(element) :
    largeur = element.get_size()[0]
    position_x = (screen_width- largeur) // 2

    return position_x

#### BOUTTONS ####
def animate_button(screen, image_button ,button, mouse_pos, i) :
    original_size = image_button.get_size()
    scale_factor = 1.1

    if button.collidepoint(mouse_pos) :
        if hover_sound_played[i] == False :
            hover_sound.play(0, 300)
            hover_sound_played[i] = True

        new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        scaled_image = pygame.transform.scale(image_button, new_size)
        scaled_rect = scaled_image.get_rect(center = button.center)
    else :
        scaled_image = image_button
        scaled_rect = button
        hover_sound_played[i] = False

    screen.blit(scaled_image, scaled_rect)
