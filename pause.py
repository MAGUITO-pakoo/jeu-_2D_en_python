import pygame
import ressources

pygame.init()

class PausePage() :
    def __init__(self) :
        self.background = ressources.background_2
        self.cadre = pygame.Rect(292.9, 48, 367, 493)
        self.text = ressources.font_exit.render("Pause", False, ressources.marron)

        #images et boutons
        self.play_image = self.scale_pause_menu_buttons(pygame.image.load("images/boutons/jouer.png"))
        self.options_image = self.scale_pause_menu_buttons(pygame.image.load("images/boutons/options.png"))
        self.back_image = self.scale_pause_menu_buttons(pygame.image.load("images/boutons/retour.png"))
        self.pause_menu_images = [self.play_image, self.options_image, self.back_image]

        self.bouton_play = self.play_image.get_rect(left=388, top=166)
        self.bouton_options = self.options_image.get_rect(left=388, top=286)
        self.bouton_back = self.back_image.get_rect(left=388, top=403)
        self.boutons_pause_menu = [self.bouton_play, self.bouton_options, self.bouton_back]

    def scale_pause_menu_buttons(self, image) :
        return pygame.transform.scale(image, (175, 69))

    def manage_buttons(self, current_page_name, previous_page_name) :
        mouse_pos = pygame.mouse.get_pos()
        page_name = current_page_name
        previous = previous_page_name
        if self.bouton_play.collidepoint(mouse_pos) :
            page_name = "game"
            previous = current_page_name
        elif self.bouton_options.collidepoint(mouse_pos) :
            page_name = "options"
            previous = current_page_name
        elif self.bouton_back.collidepoint(mouse_pos) :
            page_name = "quitter"
            previous = current_page_name
        
        return (page_name, previous)

    def draw_content(self, screen, previous_page_name) :
        screen.blit(self.background, (0, 0))
        pygame.draw.rect(screen, ressources.black, self.cadre, 0, 20)
        screen.blit(self.text, (411, 86))
        
        i = 0
        for image in self.pause_menu_images :
            screen.blit(image, self.boutons_pause_menu[i])
            i += 1

        i = 0
        mouse_pos = pygame.mouse.get_pos()
        for bouton in self.boutons_pause_menu :
            ressources.animate_button(screen, self.pause_menu_images[i], bouton, mouse_pos, i)
            i += 1

pause_page = PausePage()