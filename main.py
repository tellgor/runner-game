# importing all objects for render them in main file on screen and use all their methods import pygame
import pygame
from let import Let
from hero import Hero
from game_over_menu import EndMenu
import sprites
from score import Score


clock = pygame.time.Clock
pygame.init()
screen = pygame.display.set_mode((1000, 500))
frame_counter = 0  # variable for counting frames, used for changing sprites in animations functions
animation_queue = 0  # variable for setting index of sprite in `sprites.background_spites`
game_stop = False  # check-variable for the game over condition


def global_animation():  # function for changing sprite in game animations every 5th frame
    global frame_counter, animation_queue
    if frame_counter == 5:  # every 5th frame changing `animation_queue`
        frame_counter = 0
        if animation_queue == 12:  # does not allow the `animetion_queue` to go beyond 12, in order to avoid `index out of range` error
            animation_queue = 0
        else:  # increase `animation_queue` by 1 and calling `Hero().next_sprite()`
            animation_queue += 1
            Hero().next_sprite()
    else:
        frame_counter += 1


def game_init():  # initialization of all classes and methods of the game
    global frame_counter, game_stop, animation_queue
    run = True  # variable for while loop realization

    while run:
        for event in pygame.event.get():  # loop in indexes of gotten events from pygame
            mouse_pos = pygame.mouse.get_pos()  # getting current position of mouse
            pressed_key = pygame.key.get_pressed()  # getting current pressed key
            if event.type == pygame.QUIT:  # condition to exit the loop
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # getting mouse pos when clicked
                mouse_click = pygame.mouse.get_pos()
                if EndMenu().check_click(mouse_click) and game_stop:  # checking if mouseclick was coordinates of
                    # restart button, and checking if game over menu was in active state
                    game_stop = False  # restarting the game
                    # restoring all variables for game restart
                    Hero().restore()
                    Let().restore()
                    EndMenu().restore()
                    Score().restore()
                    frame_counter = 0
                    animation_queue = 0

        # drawing all independent classes (classes that be drawn regardless of anything)
        screen.blit(sprites.background_sprite[animation_queue], (0, 0))
        screen.blit(Hero().image, Hero().rect)
        screen.blit(Let().image, Let().rect)

        if Hero().rect.colliderect(Let()):  # checking if hero collided the let
            EndMenu().init(screen, mouse_pos)  # initialization of game over menu
            game_stop = True
        if not game_stop:  # checking if game over menu in non-active state
            global_animation()
            Hero().jump(pressed_key)
            Let().init()
            Score().init(screen)
        pygame.display.flip()  # moving to next frame
        clock().tick(60)  # number of frames per second

    pygame.quit()  # exit from pygame in program after loop


if __name__ == "__main__":
    game_init()
