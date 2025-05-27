import pygame
import ressources

pygame.init()

class OptionsPage() :
    def __init__(self) :
        self.background = ressources.background_3
        self.cadre = pygame.Rect(226, 44, 485, 509)
        self.ligne_separatrice = pygame.Rect(270, 250, 395, 8)

        #Textes
        self.text_title = ressources.font_exit.render("Options", False, ressources.marron)
        self.text_musique = ressources.font_options.render("Musique de fond", False, ressources.white)
        self.text_effets = ressources.font_options.render("Effets sonores", False, ressources.white)
        self.text_contents_list = ["Liste des commandes", "- Avancer : D", "- Reculer : Q", 
                            "- Sauter : ESPACE", "- Tirer : RCTRL", "- Pause/play : P"]

        self.text_list = []
        for i in range(len(self.text_contents_list)) :
            self.text_list.append(ressources.font_options.render(self.text_contents_list[i], False, ressources.white)) 

        #images et boutons
        self.on_image_1 = self.scale_options_page_buttons(pygame.image.load("images/boutons/oui.png"))
        self.on_image_2 = self.scale_options_page_buttons(pygame.image.load("images/boutons/oui.png"))
        self.off_image_1 = self.scale_options_page_buttons(pygame.image.load("images/boutons/non.png"))
        self.off_image_2 = self.scale_options_page_buttons(pygame.image.load("images/boutons/non.png"))
        self.back_image = pygame.transform.scale(pygame.image.load("images/boutons/retour.png"), (130, 54))

        self.bouton_on_1 = self.on_image_1.get_rect(left=493, top=133)
        self.bouton_on_2 = self.on_image_2.get_rect(left=463, top=195)
        self.bouton_off_1 = self.off_image_1.get_rect(left=493, top=133)
        self.bouton_off_2 = self.off_image_2.get_rect(left=463, top=195)
        self.bouton_back = self.back_image.get_rect(left=535, top=468)

        self.images_options_page = [self.on_image_1, self.on_image_2, self.back_image]
        self.boutons_options_page = [self.bouton_on_1, self.bouton_on_2, self.bouton_back]

    def scale_options_page_buttons(self, image) :
        return pygame.transform.scale(image, (72, 38))

    def manage_buttons(self, current_page_name, previous_page_name) :
        mouse_pos = pygame.mouse.get_pos()
        page_name = current_page_name
        previous = previous_page_name
        if self.bouton_on_1.collidepoint(mouse_pos) :
            ressources.back_sound.stop()
            self.images_options_page.remove(self.on_image_1)
            self.boutons_options_page.remove(self.bouton_on_1)
            self.bouton_on_1.x = -1000
            self.bouton_off_1.x = 493
            self.images_options_page.append(self.off_image_1)
            self.boutons_options_page.append(self.bouton_off_1)

        elif self.bouton_on_2.collidepoint(mouse_pos) :
            ressources.hover_sound.set_volume(0)
            ressources.jump_sound.set_volume(0)
            self.images_options_page.remove(self.on_image_2)
            self.boutons_options_page.remove(self.bouton_on_2)
            self.bouton_on_2.x = -1000
            self.bouton_off_2.x = 463
            self.images_options_page.append(self.off_image_2)
            self.boutons_options_page.append(self.bouton_off_2)

        elif self.bouton_off_1.collidepoint(mouse_pos) :
            ressources.back_sound.play()
            self.images_options_page.remove(self.off_image_1)
            self.boutons_options_page.remove(self.bouton_off_1)
            self.bouton_off_1.x = -1000
            self.bouton_on_1.x = 493
            self.images_options_page.append(self.on_image_1)
            self.boutons_options_page.append(self.bouton_on_1)

        elif self.bouton_off_2.collidepoint(mouse_pos) :
            ressources.hover_sound.set_volume(0.5)
            ressources.jump_sound.set_volume(0.5)
            self.images_options_page.remove(self.off_image_2)
            self.boutons_options_page.remove(self.bouton_off_2)
            self.bouton_off_2.x = -1000
            self.bouton_on_2.x = 463
            self.images_options_page.append(self.on_image_2)
            self.boutons_options_page.append(self.bouton_on_2)

        elif self.bouton_back.collidepoint(mouse_pos) :
            page_name = previous
            previous = current_page_name
        
        return (page_name, previous)

    def draw_content(self, screen, previous_page_name) :
        screen.blit(self.background, (0, 0))
        pygame.draw.rect(screen, ressources.black, self.cadre, 0, 20)
        screen.blit(self.text_title, (387, 71))
        screen.blit(self.text_musique, (270, 140))
        screen.blit(self.text_effets, (270, 200))
        pygame.draw.rect(screen, ressources.marron, self.ligne_separatrice, 0, 3)
        
        y = 282
        for i in range(len(self.text_list)) :
            screen.blit(self.text_list[i], (270, y))
            y += 42
        
        i = 0
        for button in self.boutons_options_page :
            screen.blit(self.images_options_page[i], button)
            i += 1
        
        i = 0
        mouse_pos = pygame.mouse.get_pos()
        for bouton in self.boutons_options_page :
            ressources.animate_button(screen, self.images_options_page[i], bouton, mouse_pos, i)
            i += 1

options_page = OptionsPage()