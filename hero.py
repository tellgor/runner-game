import pygame
import sprites  # importing sprites for hero animation


class Hero(pygame.sprite.Sprite):
    is_jump = False  # variable to check when hero is jumping
    jump_count = 10  # variable for counting and calculating jump physics
    HERO_X = 80  # x cor for hero
    HERO_Y = 375  # y cor for hero
    sprite_counter = 0  # variable for counting index sprites tuple for animation

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # initializing parent class
        self.image = sprites.hero_sprites[Hero.sprite_counter]  # getting surface in `sprites.hero_sprites` on
        # sprite_counter as index
        self.rect = self.image.get_rect() # getting parameters of rectangle from `self.image` surface
        self.key_input = None  # variable for using key_input for jump function
        self.rect.x = Hero.HERO_X
        self.rect.y = Hero.HERO_Y

    def jump(self, key_input):  # jump physics algorithm
        self.key_input = key_input  # getting keyboard input from parameter to self variable
        if not Hero.is_jump:  # if hero not jumping checking keyboard input
            if self.key_input[pygame.K_SPACE] or self.key_input[pygame.K_UP]:
                Hero.is_jump = True

        else:  # calculating physics when `Hero.is_jump` is True
            if Hero.jump_count >= -10:
                Hero.HERO_Y -= (Hero.jump_count * abs(Hero.jump_count)) * 0.5
                Hero.jump_count -= 0.5
            else:
                Hero.jump_count = 10
                Hero.is_jump = False

    def next_sprite(self):  # function for hero animation
        if Hero.is_jump:  # setting sprite when hero is jumping
            Hero.sprite_counter = 4  # index in `sprites.hero_sprites` where sprite for jumping hero
        elif Hero.sprite_counter >= 3:  # if to avoid "out of range error", and to avoid hero with jumping sprite when not jumping
            Hero.sprite_counter = 0  # start counting sprites again
        else:
            Hero.sprite_counter += 1  # counting next sprite index in `sprites.hero_sprites`

    def restore(self):  # restoring class variables
        Hero.HERO_Y = 375
        Hero.is_jump = False
        Hero.jump_count = 10
        Hero.sprite_counter = 0
