import pygame
import ressources

pygame.init()

class HomePage() :
    def __init__(self) :
        self.background = ressources.background
        self.game_title = ressources.font_title.render("Treasure Recovery", False, ressources.white, ressources.marron)

        #Images et boutons
        self.image_btn_jouer = self.scale_button(pygame.image.load("images/boutons/jouer.png"))
        self.image_btn_options = self.scale_button(pygame.image.load("images/boutons/options.png"))
        self.image_btn_quitter = self.scale_button(pygame.image.load("images/boutons/retour.png"))
        self.home_page_images = [self.image_btn_jouer, self.image_btn_options, self.image_btn_quitter]

        self.bouton_jouer = self.image_btn_jouer.get_rect(left = ressources.center_content(self.image_btn_jouer), top = 260)
        self.bouton_options = self.image_btn_options.get_rect(left = ressources.center_content(self.image_btn_options), top = 365)
        self.bouton_quitter = self.image_btn_quitter.get_rect(left = ressources.center_content(self.image_btn_quitter), top = 470)
        self.boutons_home_page = [self.bouton_jouer, self.bouton_options, self.bouton_quitter]

    def scale_button(self, button) :
        return pygame.transform.scale(button, (198, 78))

    def manage_buttons(self, current_page_name, previous_page_name) :
        mouse_pos = pygame.mouse.get_pos()
        page_name = current_page_name
        previous = previous_page_name
        if self.bouton_jouer.collidepoint(mouse_pos) :
            page_name = "game"
            previous = current_page_name
        elif self.bouton_options.collidepoint(mouse_pos) :
            page_name = "options"
            previous = current_page_name
        elif self.bouton_quitter.collidepoint(mouse_pos) :
            page_name = "quitter"
            previous = current_page_name
        
        return (page_name, previous)

    def draw_content(self, screen, previous_page_name) :
        screen.blit(self.background, (0,0))
        screen.blit(self.game_title, (ressources.center_content(self.game_title), 90))

        i = 0
        for bouton in self.boutons_home_page :
            screen.blit(self.home_page_images[i], bouton)
            i += 1

        mouse_pos = pygame.mouse.get_pos()
        i = 0
        for bouton in self.boutons_home_page :
            ressources.animate_button(screen, self.home_page_images[i], bouton, mouse_pos, i)
            i += 1

home_page = HomePage()