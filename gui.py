# Imports

import pygame
import os

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

    pygame.event.get()

    Y_COORDINATES = {
        "-1-1-1": (210, 47), "-1-10": (164, 73), "-1-11": (118, 99), "0-1-1": (256, 73), "0-10": (210, 99), "0-11": (164, 125),
        "1-1-1": (302, 99), "1-10": (256, 125), "1-11": (210, 151), "-11-1": (210, 572), "-110": (164, 598), "-111": (118, 624), 
        "01-1": (256, 598), "010": (210, 624), "011": (164, 650), "11-1": (302, 624), "110": (256, 650), "111": (210, 676)
    }

    for i in range(3):
        for j in range(3):
            for cube in range(len(TEST_LIST)):
                if TEST_LIST[cube][0][1] == -1:
                    if TEST_LIST[cube][1][1] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(-TEST_LIST[cube][1][1])+'_top.png')), (TOP_FACE_WIDTH, TOP_FACE_HEIGHT)), 
                                Y_COORDINATES[str(i-1)+str(-1)+str(j-1)])
                if TEST_LIST[cube][0][1] == 1:
                    if TEST_LIST[cube][1][1] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(TEST_LIST[cube][1][1])+'_top.png')), (TOP_FACE_WIDTH, TOP_FACE_HEIGHT)), 
                                Y_COORDINATES[str(i-1)+str(1)+str(j-1)])
    
    X_COORDINATES = {
        "-1-1-1": (207, 409), "-1-10": (160, 435), "-1-11": (115, 462), "-10-1": (207, 464), "-100": (160, 490), "-101": (115, 517),
        "-11-1": (207, 519), "-110": (160, 545), "-111": (115, 572), "1-1-1": (346, 127), "1-10": (300, 153), "1-11": (254, 180), 
        "10-1": (346, 182), "100": (300, 208), "101": (254, 235), "11-1": (346, 237), "110": (300, 263), "111": (254, 290)
    }

    for i in range(3):
        for j in range(3):
            for cube in range(len(TEST_LIST)):
                if TEST_LIST[cube][0][0] == -1:
                    if TEST_LIST[cube][1][0] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(-TEST_LIST[cube][1][0])+'_right.png')), (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT)), 
                                X_COORDINATES[str(-1)+str(i-1)+str(j-1)])
                if TEST_LIST[cube][0][0] == 1:
                    if TEST_LIST[cube][1][0] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(TEST_LIST[cube][1][0])+'_right.png')), (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT)), 
                                X_COORDINATES[str(1)+str(i-1)+str(j-1)]) 
    
    Z_COORDINATES = {
        "-1-1-1": (254, 409), "-10-1": (254, 464), "-11-1": (254, 519), "0-1-1": (300, 435), "00-1": (300, 490), "01-1": (300, 545),
        "1-1-1": (346, 462), "10-1": (346, 517), "11-1": (346, 572), "-1-11": (115, 127), "-101": (115, 182), "-111": (115, 237), 
        "0-11": (160, 153), "001": (160, 208), "011": (160, 263), "1-11": (207, 180), "101": (207, 235), "111": (207, 290)
    }

    for i in range(3):
        for j in range(3):
            for cube in range(len(TEST_LIST)):
                if TEST_LIST[cube][0][2] == -1:
                    if TEST_LIST[cube][1][2] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(-TEST_LIST[cube][1][2])+'_left.png')), (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT)), 
                                Z_COORDINATES[str(i-1)+str(j-1)+str(-1)])
                if TEST_LIST[cube][0][2] == 1:
                    if TEST_LIST[cube][1][2] != 0:
                        WIN.blit(
                            pygame.transform.scale(pygame.image.load(os.path.join('assets', 
                                str(TEST_LIST[cube][1][2])+'_left.png')), (SIDE_FACE_WIDTH, SIDE_FACE_HEIGHT)), 
                                Z_COORDINATES[str(i-1)+str(j-1)+str(1)])                               

    pygame.display.update()