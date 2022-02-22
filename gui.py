import pygame
import os

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cube")
CUBE_WIDTH = 500
CUBE_HEIGHT = 500
TOP_FACE_HEIGHT = 45
TOP_FACE_WIDTH = 80
SIDE_FACE_HEIGHT = 60
SIDE_FACE_WIDTH = 30


BACKGROUND = pygame.image.load(
    os.path.join('assets', 'background.png'))
BACKGROUND_RESIZED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

CUBE_FRAME = pygame.image.load(
    os.path.join('assets', 'cube.png'))
CUBE_FRAME_RESIZED = pygame.transform.scale(CUBE_FRAME, (CUBE_WIDTH, CUBE_HEIGHT))

RED_TOP = pygame.image.load(
    os.path.join('assets', 'red_top.png'))
RED_TOP_RESIZED = pygame.transform.scale(RED_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

WHITE_TOP = pygame.image.load(
    os.path.join('assets', 'white_top.png'))
WHITE_TOP_RESIZED = pygame.transform.scale(WHITE_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

BLUE_TOP = pygame.image.load(
    os.path.join('assets', 'blue_top.png'))
BLUE_TOP_RESIZED = pygame.transform.scale(BLUE_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

GREEN_TOP = pygame.image.load(
    os.path.join('assets', 'green_top.png'))
GREEN_TOP_RESIZED = pygame.transform.scale(GREEN_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

ORANGE_TOP = pygame.image.load(
    os.path.join('assets', 'orange_top.png'))
ORANGE_TOP_RESIZED = pygame.transform.scale(ORANGE_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

YELLOW_TOP = pygame.image.load(
    os.path.join('assets', 'yellow_top.png'))
YELLOW_TOP_RESIZED = pygame.transform.scale(YELLOW_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))


def draw_window():
    WIN.blit(BACKGROUND_RESIZED, (0,0))
    #WIN.blit(CUBE_FRAME_RESIZED, (0,0))
    WIN.blit(RED_TOP_RESIZED, (210,97))
    WIN.blit(WHITE_TOP_RESIZED, (164,123))
    WIN.blit(YELLOW_TOP_RESIZED, (164,175))
    WIN.blit(ORANGE_TOP_RESIZED, (256,175))
    WIN.blit(BLUE_TOP_RESIZED, (210,149))
    WIN.blit(GREEN_TOP_RESIZED, (256,123))
    WIN.blit(ORANGE_TOP_RESIZED, (118,149))
    WIN.blit(BLUE_TOP_RESIZED, (302,149))
    WIN.blit(GREEN_TOP_RESIZED, (210,201))

    pygame.display.update()

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
