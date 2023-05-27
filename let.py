import pygame
import random  # importing for generate lets in randomly interval and for set random sprite when spawning let
import sprites  # importing for get let sprites and set on Let object


class Let(pygame.sprite.Sprite):
    LET_X = 1100
    sprite_index = 0  # variable which used for generating random sprites indexes for animation

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # initializing parent class
        self.LET_Y = 375
        self.image = sprites.let_sprites[
            Let.sprite_index]  # getting surface from `sprites.let_sprites` in index `Let.sprite_counter`
        self.rect = self.image.get_rect()  # getting rectangle parameters from `self.image` surface
        self.rect.x = Let.LET_X
        self.rect.y = self.LET_Y

    def init(self):  # function for initializing `self.move()` and `self.generate_index()`
        spawn_call = random.randint(1, 50)
        if spawn_call == 1 and Let.LET_X == 1100:  # when spawn_call is 1 generating let and sprite for let
            self.move()
            self.generate_index()
        if Let.LET_X != 1100:  # moves let when was generated
            self.move()

    def move(self):  # algorithm for calculating let position
        if Let.LET_X > -280:  # when let is not reached final pos moves him on 7 pixels left
            Let.LET_X -= 7
        else:  # if let reached final position moves let to start position
            Let.LET_X = 1100

    def generate_index(self):  # generate random sprite index to set on `self.image`
        Let.sprite_index = random.randint(0, 2)

    def restore(self):  # restoring class variables
        Let.LET_X = 1100
