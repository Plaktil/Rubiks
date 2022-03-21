# Imports

import pygame
import os

'''
TEST_LIST = [
    ([-1, -1, -1],[-5, -1, -3]),
    ([0, -1, -1],[0, -1, -3]),
    ([1, -1, -1],[2, -1, -3]),
    ([-1, 0, -1],[-5, 0, -3]),
    ([0, 0, -1],[0, 0, -3]),
    ([1, 0, -1],[2, 0, -3]),
    ([-1, 1, -1],[-5, 6, -3]),
    ([ 0, 1, -1],[0, 6, -3]),
    ([ 1, 1, -1],[2, 6, -3]),
    ([-1, -1, 0],[-5, -1, 4]),
    ([ 0, -1, 0],[0, -1, 4]),
    ([ 1, -1, 0],[2, -1, 4]),
    ([-1, 0, 0],[-5, 0, 4]),
    ([0, 0, 0],[0, 0, 4]),
    ([1, 0, 0],[2, 0, 4]),
    ([-1,  1, 0],[-5, 6, 4]),
    ([0, 1, 0],[0, 6, 4]),
    ([1, 1, 0],[2, 6, 4]),
    ([-1, -1, 1],[-5, -1, 0]),
    ([ 0, -1, 1],[0, -1, 0]),
    ([ 1, -1, 1],[2, -1, 0]),
    ([-1, 0, 1],[-5, 0, 0]),
    ([0, 0, 1.],[0, 0, 0]),
    ([1, 0, 1],[2, 0, 0]),
    ([-1, 1, 1],[-5, 6, 0]),
    ([0, 1, 1],[0, 6, 0]),
    ([1, 1, 1],[2, 6, 0])]
'''

# Constants

WIDTH, HEIGHT = 500, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cube")
CUBE_WIDTH = 500
CUBE_HEIGHT = 500
BACK_SHIFT = 475
SIDE_SHIFT = 282
TOP_FACE_HEIGHT = 45
TOP_FACE_WIDTH = 80
SIDE_FACE_HEIGHT = 70
SIDE_FACE_WIDTH = 40

# Assets

BACKGROUND = pygame.image.load(
    os.path.join('assets', 'background.png'))
BACKGROUND_RESIZED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

CUBE_FRAME = pygame.image.load(
    os.path.join('assets', 'cube.png'))
CUBE_FRAME_RESIZED = pygame.transform.scale(CUBE_FRAME, (CUBE_WIDTH, CUBE_HEIGHT))

#RED_TOP = pygame.image.load(
#    os.path.join('assets', 'red_top.png'))
#RED_TOP_RESIZED = pygame.transform.scale(RED_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

#WHITE_TOP = pygame.image.load(
#    os.path.join('assets', 'white_top.png'))
#WHITE_TOP_RESIZED = pygame.transform.scale(WHITE_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

#BLUE_TOP = pygame.image.load(
#    os.path.join('assets', 'blue_top.png'))
#BLUE_TOP_RESIZED = pygame.transform.scale(BLUE_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

#GREEN_TOP = pygame.image.load(
#    os.path.join('assets', 'green_top.png'))
#GREEN_TOP_RESIZED = pygame.transform.scale(GREEN_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

#ORANGE_TOP = pygame.image.load(
#    os.path.join('assets', 'orange_top.png'))
#ORANGE_TOP_RESIZED = pygame.transform.scale(ORANGE_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

#YELLOW_TOP = pygame.image.load(
#    os.path.join('assets', 'yellow_top.png'))
#YELLOW_TOP_RESIZED = pygame.transform.scale(YELLOW_TOP, (TOP_FACE_WIDTH, TOP_FACE_HEIGHT))

RED_LEFT = pygame.image.load(
    os.path.join('assets', 'red_left.png'))
RED_LEFT_RESIZED = pygame.transform.scale(RED_LEFT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

WHITE_LEFT = pygame.image.load(
    os.path.join('assets', 'white_left.png'))
WHITE_LEFT_RESIZED = pygame.transform.scale(WHITE_LEFT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

BLUE_LEFT = pygame.image.load(
    os.path.join('assets', 'blue_left.png'))
BLUE_LEFT_RESIZED = pygame.transform.scale(BLUE_LEFT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

GREEN_LEFT = pygame.image.load(
    os.path.join('assets', 'green_left.png'))
GREEN_LEFT_RESIZED = pygame.transform.scale(GREEN_LEFT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

ORANGE_LEFT = pygame.image.load(
    os.path.join('assets', 'orange_left.png'))
ORANGE_LEFT_RESIZED = pygame.transform.scale(ORANGE_LEFT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

YELLOW_LEFT = pygame.image.load(
    os.path.join('assets', 'yellow_left.png'))
YELLOW_LEFT_RESIZED = pygame.transform.scale(YELLOW_LEFT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

RED_RIGHT = pygame.image.load(
    os.path.join('assets', 'red_right.png'))
RED_RIGHT_RESIZED = pygame.transform.scale(RED_RIGHT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

WHITE_RIGHT = pygame.image.load(
    os.path.join('assets', 'white_right.png'))
WHITE_RIGHT_RESIZED = pygame.transform.scale(WHITE_RIGHT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

BLUE_RIGHT = pygame.image.load(
    os.path.join('assets', 'blue_right.png'))
BLUE_RIGHT_RESIZED = pygame.transform.scale(BLUE_RIGHT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

GREEN_RIGHT = pygame.image.load(
    os.path.join('assets', 'green_right.png'))
GREEN_RIGHT_RESIZED = pygame.transform.scale(GREEN_RIGHT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

ORANGE_RIGHT = pygame.image.load(
    os.path.join('assets', 'orange_right.png'))
ORANGE_RIGHT_RESIZED = pygame.transform.scale(ORANGE_RIGHT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

YELLOW_RIGHT = pygame.image.load(
    os.path.join('assets', 'yellow_right.png'))
YELLOW_RIGHT_RESIZED = pygame.transform.scale(YELLOW_RIGHT, (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT))

WIN.blit(BACKGROUND_RESIZED, (0,0))

def draw(TEST_LIST):
    
    #WIN.blit(CUBE_FRAME_RESIZED, (0,-50))
    #WIN.blit(CUBE_FRAME_RESIZED, (0,BACK_SHIFT))
    # Front
    # Top

    # Having an algorithm determine the blit position of each square depending on its block coordinate
    # would be a lot more compact and readable. Try asociating color prefixes (ie: RED, YELLOW, etc) to
    # numbers (1 to 6) and position (ie: TOP, LEFT, etc.) to coordinate + sign to form the name of
    # the asset to use so that you can use color + "_" + position + ".png" to load the assets just in time
    # instead of keeping them loaded in Globals for the whole code. Then you can loop through the blocks
    # and use a single blit statement to do the whole job.

    Y_COORDINATES = {
        "-1-1-1": (210, 47), "-1-10": (164, 73), "-1-11": (118, 99), "0-1-1": (256, 73), "0-10": (210, 99), "0-11": (164, 125),
        "1-1-1": (302, 99), "1-10": (256, 125), "1-11": (210, 151), "-11-1": (210, 572), "-110": (164, 598), "-111": (118, 624), 
        "01-1": (256, 598), "010": (210, 624), "011": (164, 650), "11-1": (302, 624), "110": (256, 650), "111": (210, 676)
    }

    for i in range(3):
        for k in range(3):
            for cube in range(len(TEST_LIST)):
                if TEST_LIST[cube][0][1] == -1:
                    if TEST_LIST[cube][1][1] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(-TEST_LIST[cube][1][1])+'_top.png')), (TOP_FACE_WIDTH, TOP_FACE_HEIGHT)), 
                                Y_COORDINATES[str(i-1)+str(-1)+str(k-1)])
                if TEST_LIST[cube][0][1] == 1:
                    if TEST_LIST[cube][1][1] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(TEST_LIST[cube][1][1])+'_top.png')), (TOP_FACE_WIDTH, TOP_FACE_HEIGHT)), 
                                Y_COORDINATES[str(i-1)+str(1)+str(k-1)])
 
    ''' 
    WIN.blit(RED_TOP_RESIZED, (210,47))
    WIN.blit(WHITE_TOP_RESIZED, (164,73))
    WIN.blit(YELLOW_TOP_RESIZED, (164,125))
    WIN.blit(ORANGE_TOP_RESIZED, (256,125))
    WIN.blit(BLUE_TOP_RESIZED, (210,99))
    WIN.blit(GREEN_TOP_RESIZED, (256,73))
    WIN.blit(ORANGE_TOP_RESIZED, (118,99))
    WIN.blit(BLUE_TOP_RESIZED, (302,99))
    WIN.blit(GREEN_TOP_RESIZED, (210,151))
    '''
    # Left
    WIN.blit(RED_LEFT_RESIZED, (115,127))
    WIN.blit(WHITE_LEFT_RESIZED, (160,153))
    WIN.blit(YELLOW_LEFT_RESIZED, (207,180))
    WIN.blit(ORANGE_LEFT_RESIZED, (115,182))
    WIN.blit(BLUE_LEFT_RESIZED, (160,208))
    WIN.blit(GREEN_LEFT_RESIZED, (207,235))
    WIN.blit(ORANGE_LEFT_RESIZED, (115,237))
    WIN.blit(BLUE_LEFT_RESIZED, (160,263))
    WIN.blit(GREEN_LEFT_RESIZED, (207,290))
    # Right
    WIN.blit(RED_RIGHT_RESIZED, (346,127))
    WIN.blit(WHITE_RIGHT_RESIZED, (300,153))
    WIN.blit(YELLOW_RIGHT_RESIZED, (254,180))
    WIN.blit(ORANGE_RIGHT_RESIZED, (346,182))
    WIN.blit(BLUE_RIGHT_RESIZED, (300,208))
    WIN.blit(GREEN_RIGHT_RESIZED, (254,235))
    WIN.blit(ORANGE_RIGHT_RESIZED, (346,237))
    WIN.blit(BLUE_RIGHT_RESIZED, (300,263))
    WIN.blit(GREEN_RIGHT_RESIZED, (254,290))

    # Back
    '''
    # Top
    WIN.blit(WHITE_TOP_RESIZED, (210,97+BACK_SHIFT))
    WIN.blit(WHITE_TOP_RESIZED, (164,123+BACK_SHIFT))
    WIN.blit(YELLOW_TOP_RESIZED, (164,175+BACK_SHIFT))
    WIN.blit(ORANGE_TOP_RESIZED, (256,175+BACK_SHIFT))
    WIN.blit(BLUE_TOP_RESIZED, (210,149+BACK_SHIFT))
    WIN.blit(GREEN_TOP_RESIZED, (256,123+BACK_SHIFT))
    WIN.blit(ORANGE_TOP_RESIZED, (118,149+BACK_SHIFT))
    WIN.blit(BLUE_TOP_RESIZED, (302,149+BACK_SHIFT))
    WIN.blit(GREEN_TOP_RESIZED, (210,201+BACK_SHIFT))
    '''
    # Left
    WIN.blit(RED_RIGHT_RESIZED, (207,127+SIDE_SHIFT))
    WIN.blit(WHITE_RIGHT_RESIZED, (160,153+SIDE_SHIFT))
    WIN.blit(YELLOW_RIGHT_RESIZED, (115,180+SIDE_SHIFT))
    WIN.blit(ORANGE_RIGHT_RESIZED, (207,182+SIDE_SHIFT))
    WIN.blit(BLUE_RIGHT_RESIZED, (160,208+SIDE_SHIFT))
    WIN.blit(GREEN_RIGHT_RESIZED, (115,235+SIDE_SHIFT))
    WIN.blit(ORANGE_RIGHT_RESIZED, (207,237+SIDE_SHIFT))
    WIN.blit(BLUE_RIGHT_RESIZED, (160,263+SIDE_SHIFT))
    WIN.blit(GREEN_RIGHT_RESIZED, (115,290+SIDE_SHIFT))
    # Right
    WIN.blit(RED_LEFT_RESIZED, (254,127+SIDE_SHIFT))
    WIN.blit(WHITE_LEFT_RESIZED, (300,153+SIDE_SHIFT))
    WIN.blit(YELLOW_LEFT_RESIZED, (346,180+SIDE_SHIFT))
    WIN.blit(ORANGE_LEFT_RESIZED, (254,182+SIDE_SHIFT))
    WIN.blit(BLUE_LEFT_RESIZED, (300,208+SIDE_SHIFT))
    WIN.blit(GREEN_LEFT_RESIZED, (346,235+SIDE_SHIFT))
    WIN.blit(ORANGE_LEFT_RESIZED, (254,237+SIDE_SHIFT))
    WIN.blit(BLUE_LEFT_RESIZED, (300,263+SIDE_SHIFT))
    WIN.blit(GREEN_LEFT_RESIZED, (346,290+SIDE_SHIFT))

    pygame.display.update()
'''
def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw(TEST_LIST)

    pygame.quit()

if __name__ == "__main__":
    main()
'''