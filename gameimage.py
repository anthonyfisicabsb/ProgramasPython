import pygame
import sys

def run_game():
    pygame.init()

    screen=pygame.display.set_mode((1800,1200))

    image = pygame.image.load('images/ship.bmp')

    image_rect=image.get_rect()
    screen_rect=screen.get_rect()

    image_rect.centerx=screen_rect.centerx
    image_rect.bottom=screen_rect.bottom/2.0

    bg_color=(240,123,54)

    pygame.display.set_caption("Image on center")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(bg_color)
            screen.blit(image,image_rect)

            pygame.display.flip()


run_game()
