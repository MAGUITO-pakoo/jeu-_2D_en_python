import pygame
import ressources
from game import player

pygame.init()

class QuitterPage() :
    def __init__(self) :
        #Surfaces et textes
        self.pop_up_surface = pygame.Surface((950, 600), pygame.SRCALPHA)
        self.pop_up_surface.fill(ressources.black_transp)

        self.cadre = pygame.Rect(226, 204, 485, 198)
        self.text_game = ressources.font_exit.render("Retourner au menu ?", False, ressources.white)
        self.text_home = ressources.font_exit.render("Quitter le jeu ?", False, ressources.white)

        #images et boutons
        self.yes_image = self.scale_exit_zone_buttons(pygame.image.load("images/boutons/oui.png"))
        self.no_image = self.scale_exit_zone_buttons(pygame.image.load("images/boutons/non.png"))
        self.exit_zone_images = [self.yes_image, self.no_image]

        self.bouton_yes = self.yes_image.get_rect(left=319, top=305)
        self.bouton_no = self.no_image.get_rect(left=495, top=305)
        self.boutons_exit_page = [self.bouton_yes, self.bouton_no]

    def scale_exit_zone_buttons(self, image) :
        return pygame.transform.scale(image, (122, 64))

    def manage_buttons(self, current_page_name, previous_page_name) :
        mouse_pos = pygame.mouse.get_pos()
        page_name = previous_page_name
        if self.bouton_yes.collidepoint(mouse_pos) :
            if previous_page_name == "game" or previous_page_name == "pause" :
                page_name = "home"
                player.__init__()
            elif previous_page_name == "home" :
                pygame.quit()
        
        elif self.bouton_no.collidepoint(mouse_pos) :
            page_name = previous_page_name

        else : 
            page_name = current_page_name
        
        return (page_name, previous_page_name)

    def draw_content(self, screen, previous_page_name) :
        screen.blit(self.pop_up_surface, (0, 0))
        pygame.draw.rect(self.pop_up_surface, ressources.black, self.cadre, 0, 20)
        if previous_page_name == "game" or previous_page_name == "pause" :
            self.pop_up_surface.blit(self.text_game, (253, 240))
        elif previous_page_name == "home" :
            self.pop_up_surface.blit(self.text_home, (317, 240))
        self.pop_up_surface.blit(self.yes_image, self.bouton_yes)
        self.pop_up_surface.blit(self.no_image, self.bouton_no)

        i = 0
        mouse_pos = pygame.mouse.get_pos()
        for bouton in self.boutons_exit_page :
            ressources.animate_button(screen, self.exit_zone_images[i], bouton, mouse_pos, i)
            i += 1

quitter_page = QuitterPage()