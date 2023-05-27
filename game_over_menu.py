import pygame
from score import Score  # importing for realization final score display on game over menu


class EndMenu:  # class with functions of surfaces and fonts of game over menu
    button_rect = None  # variable for getting Rect object from `show_button` and use in anothet function `button_backlight`

    def __init__(self):
        self.screen = None

    def init(self, screen, mouse_pos):  # function for initialization all functions in Restart class
        self.screen = screen
        self.background_blackout()
        self.show_button()
        self.show_text()
        self.show_final_score()
        self.button_backlight(mouse_pos)

    def background_blackout(self):  # creating translucent surface and rectangle and blit them for realization blackout mechanic
        surface = pygame.Surface((1000, 500), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 120))
        rect = surface.get_rect()
        self.screen.blit(surface, rect)

    def show_text(self):  # creating font and surface with "Game Over" text and blit at given coordinates
        font = pygame.font.Font(None, 140)
        text_surface = font.render("Game Over", True, (255, 255, 255))
        text_x = 240
        text_y = 90
        self.screen.blit(text_surface, (text_x, text_y))

    def show_button(self):  # creating button surface with "Restart" text
        button_font = pygame.font.Font(None, 100)
        button_surface = button_font.render("Restart", True, (255, 255, 255))
        button_x = 370
        button_y = 370
        EndMenu.button_rect = button_surface.get_rect()  # getting width and height of `button surface`
        EndMenu.button_rect.x = 370  # setting x cor to a `self.button_rect`
        EndMenu.button_rect.y = 370  # setting y cor to a `self.button_rect`
        self.screen.blit(button_surface, (button_x, button_y))

    def check_click(self, mouse_click):  # function which return if user was clicked on restart button (`Restart.button_rect`)
        if EndMenu.button_rect.collidepoint(mouse_click):
            return True
        else:
            return False

    def button_backlight(self, mouse_click):  # function which creates translucent surface with rectangle and rendering
        # him on screen when mouse position is on coordinates of rectangle
        surface = pygame.Surface((239, 68), pygame.SRCALPHA)
        surface.fill((255, 255, 255, 100))
        rect = EndMenu.button_rect
        if rect.collidepoint(mouse_click):
            self.screen.blit(surface, rect)

    def show_final_score(self):  # function creating text, getting score tuple from `Score` object, setting start
        # position of text, calculating position of each index of score tuple amd blit it on screen
        font = pygame.font.Font(None, 65)
        text = font.render("Final Score: ", True, (255, 255, 255))
        text_x = 312
        text_y = 200
        score_tpl = Score().get_surfaces  # getting tuple from `Score` function (thousands, hundreds, dozens, units)
        current_score_x = 588
        score_y = 200
        self.screen.blit(text, (text_x, text_y))
        for i in range(len(score_tpl)):  # loop which calculating position of each index of score tuple and blit on screem
            self.screen.blit(score_tpl[i], (current_score_x, score_y))
            current_score_x += 28  # moves index x on 28 pixels right on screen

    def restore(self):  # restoring class variable
        EndMenu.blackout_check = False
        EndMenu.backlight_check = False
