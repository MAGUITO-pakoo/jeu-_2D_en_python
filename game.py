import pygame
import ressources

pygame.init()

class Plateforme() :
    def __init__(self) :
        super().__init__()
    
        self.image = ressources.platform_image
        self.rect = self.image.get_rect(left=525, top=285)

class Balle() :
    def __init__(self) :
        super().__init__()
        
        self.image = ressources.ball_image
        self.rect = self.image.get_rect(left=0, top = player.rect.y + 34)
        if player.direction == "right" :
            self.rect.left = player.rect.x + player.rect.width + 15
        elif player.direction == "left" :
            self.rect.left = player.rect.x

        self.velocity = 5
        self.is_launched = False
        self.direction = player.direction

    def ball_run(self) :
        if self.direction == "right" :
            self.rect.x += self.velocity
        elif self.direction == "left" :
            self.rect.x -= self.velocity

class Player() :
    def __init__(self):
        super().__init__()

        #Image du joueur
        self.run_image_index = 0
        self.image = ressources.stand_image
        self.rect = self.image.get_rect(left=26, top=305)

        ###Mouvements et animations
        self.gravity = -160
        self.max_gravity = -160
        self.max_jump = False
        self.is_jumping = False
        self.direction = "right"

        self.is_shooting = False
        self.shoot_frame_triggered = False
        self.shoot_speed = 0.02
        self.shoot_image_index = 0

        self.on_platform = False

    def apply_gravity(self, sol) :
        if self.on_platform == False and self.is_jumping == False :
            if self.rect.bottom < sol.top + 7 :
                self.rect.y += 5

            if self.rect.bottom >= sol.top + 7 :
                self.rect.bottom = sol.top + 7

    def player_stand(self) :
        if self.direction == "right" :
            self.image = ressources.stand_image
        elif self.direction == "left" :
            self.image = ressources.stand_image_left

    def player_walk(self) : 
        self.run_image_index += 0.08      
        if self.direction == "right" :
            self.rect.x += 2
            if self.run_image_index >= len(ressources.run_images) :
                self.run_image_index = 0
            self.image = ressources.run_images[int(self.run_image_index)]

        elif self.direction == "left" :
            if self.rect.x <= 0 :
                self.rect.x = 0
            self.rect.x -= 2
            if self.run_image_index >= len(ressources.run_images_left) :
                self.run_image_index = 0
            self.image = ressources.run_images_left[int(self.run_image_index)]

    def player_jump(self, sol) :
        if self.direction == "right" :
            self.image = ressources.jump_image
        elif self.direction == "left" :
            self.image = ressources.jump_image_left
        
        if self.max_jump == False : #Monter tant qu'il n'a pas atteint le saut maximal
            self.rect.y -= 5
            self.gravity += 5
        
        if self.gravity >= 0 : #Atteinte du saut maximal
            self.max_jump = True

        if self.max_jump == True and self.is_jumping == True : #Redescendre jusqu'au sol ou une plateforme
            self.rect.y += 5
            self.gravity -= 5
            
            self.check_collision()

            if self.on_platform == True :
                self.gravity = self.max_gravity
                self.player_stand()

            if self.rect.bottom >= sol.top + 7 and self.is_jumping == True : #Si le joueur a atteint le sol
                self.rect.bottom = sol.top + 7
                self.gravity = self.max_gravity
                self.is_jumping = False
                self.max_jump = False
                self.player_stand()

    def player_shoot(self) :
        self.shoot_image_index += self.shoot_speed

        if int(self.shoot_image_index) == 0 and not self.shoot_frame_triggered :
            balle = Balle()
            balle.is_launched = True
            balles.append(balle)
            self.shoot_frame_triggered = True

        if self.direction == "right" :
            if self.shoot_image_index >= len(ressources.tir_images) :
                self.shoot_image_index = 0
                self.shoot_frame_triggered = False
            self.image = ressources.tir_images[int(self.shoot_image_index)]

        elif self.direction == "left" :
            if self.shoot_image_index >= len(ressources.tir_images_left) :
                self.shoot_image_index = 0
                self.shoot_frame_triggered = False
            self.image = ressources.tir_images_left[int(self.shoot_image_index)]

    ##### COLLISIONS AVEC LES PLATEFORMES #####
    def check_collision(self) :
        x1 = self.rect.x + self.rect.width - 23
        x2 = self.rect.x + 25
        y = self.rect.y + self.rect.height
        for platform in plateformes :
            if x1 > platform.rect.x and x2 < (platform.rect.x + platform.rect.width) :
                if y > platform.rect.top and self.max_jump == True :
                    self.on_platform = True
                    self.is_jumping = False
                    self.max_jump = False
                    self.rect.bottom = platform.rect.top
            
            else :
                self.on_platform = False

            if self.on_platform == True :
                break

    def manage_controls(self) :
        self.velocity = 1.4
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] :
            self.direction = "right"
            self.player_walk()
        elif keys[pygame.K_q] :
            self.direction = "left"
            self.player_walk()

        if keys[pygame.K_RCTRL] :
            if not self.is_shooting :
                self.is_shooting = True
                self.shoot_image_index = 0
                self.shoot_frame_triggered = False
            self.player_shoot()
        
        else : 
            self.is_shooting = False


class GamePage() :
    def __init__(self) :
        self.score = 0
        self.background = ressources.background_2

        #Texte
        self.player_name = ressources.font_score.render("Mouola", False, ressources.white)
        self.score_text = ressources.font_score.render(f"{self.score}", False, ressources.white)

        #Rectangles de données (score, barre de vie...)
        self.sol_image = pygame.transform.scale(pygame.image.load("images/décors/sol.png"), (980, 200))
        self.sol = self.sol_image.get_rect(left=-15, top=426)

        plateformes.append(Plateforme())

        self.big_rect = pygame.Rect(38.7, 17.1, 324, 58)
        self.photo_rect = pygame.Rect(38.7, 17.1, 70, 58)
        # x = big_rect.x + photo_rect.width - 3
        # y = big_rect.y + (big_rect.height / 2)
        # w = big_rect.x + big_rect.width - x
        # h = big_rect.height / 2
        self.blood_rect = pygame.Rect(105.7, 46.1, 257, 29)
        self.blood = pygame.Rect(108.7, 49.1, 251, 23)

        #images et boutons
        self.player_photo = pygame.transform.scale(pygame.image.load("images/persos/Baby Boss 2.png"), (64, 52))
        self.pause_icon = self.scale_icon(pygame.image.load("images/boutons/pause.png"))
        self.home_icon = self.scale_icon(pygame.image.load("images/boutons/home.png"))
        self.icones_game = [self.pause_icon, self.home_icon]

        self.bouton_pause = self.pause_icon.get_rect(left=800, top=26)
        self.bouton_home = self.home_icon.get_rect(left=865, top=26)
        self.boutons_game_page = [self.bouton_pause, self.bouton_home]

    def scale_icon(self, icon) :
        return pygame.transform.scale(icon, (41, 39))

    def manage_buttons(self, current_page_name, previous_page_name) :
        mouse_pos = pygame.mouse.get_pos()
        page_name = current_page_name
        previous = previous_page_name
        if self.bouton_pause.collidepoint(mouse_pos) :
            page_name = "pause"
            previous = current_page_name
        elif self.bouton_home.collidepoint(mouse_pos) :
            page_name = "quitter"
            previous = current_page_name
        
        return (page_name, previous)

    def create_platforms (self) :
        pass

    def draw_content(self, screen, previous_page_name) :
        #Elements du décor
        screen.blit(self.background, (0,0))
        screen.blit(self.player_name, (112, 20))
        screen.blit(self.score_text, (340, 20))

        screen.blit(self.sol_image, self.sol)
        pygame.draw.rect(screen, ressources.marron, self.big_rect, 3)
        pygame.draw.rect(screen, ressources.marron, self.photo_rect, 3)
        pygame.draw.rect(screen, ressources.marron, self.blood_rect, 3)
        pygame.draw.rect(screen, ressources.yellow, self.blood)

        screen.blit(self.player_photo, (41.7, 20.1))

        i = 0
        for bouton in self.boutons_game_page :
            screen.blit(self.icones_game[i], bouton)
            i += 1

        mouse_pos = pygame.mouse.get_pos()
        i = 0
        for bouton in self.boutons_game_page :
            ressources.animate_button(screen, self.icones_game[i], bouton, mouse_pos, i)
            i += 1


        #### Plateformes
        screen.blit(plateformes[0].image, plateformes[0].rect)

        ##### JOUEUR #####
        screen.blit(player.image, player.rect)
        player.player_stand()
        if player.is_jumping == True :
            player.manage_controls()
            player.player_jump(game_page.sol)
            if player.is_shooting :
                player.player_shoot()
        else :
            player.manage_controls()
            if player.is_shooting :
                player.player_shoot()
        
        player.check_collision()
        player.apply_gravity(game_page.sol)

        ##### BALLES #####
        for balle in balles :
            if balle.is_launched == True :
                screen.blit(balle.image, balle.rect)
                balle.ball_run()

                if balle.rect.x < 0 or balle.rect.x > 950 :
                    balles.remove(balle)


player = Player()
balles = []
plateformes = []
game_page = GamePage()