import pygame
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE
import sys
import json

screen_x = 500
screen_y = 500

city_color = [10,10,200] # blue
city_radius = 3

font_color = [255,255,255] # white

pygame.init() 
window = pygame.display.set_mode((screen_x, screen_y)) 
pygame.display.set_caption('Exemple') 
screen = pygame.display.get_surface() 
font = pygame.font.Font(None,30)

def draw(positions):
    screen.fill(0)
    for pos in positions: 
        pygame.draw.circle(screen,city_color,pos,city_radius)
    text = font.render("Nombre: %i" % len(positions), True, font_color)
    textRect = text.get_rect()
    screen.blit(text, textRect)
    pygame.display.flip()
    
def writeFile(filename, dict):    
    with open("result.txt", 'w') as file:
        for key, value in dict.items():
            file.write(key + ' ' + str(value[0]) + ' ' + str(value[1]) + '\n')

            
def openGui():
    cities = []
    draw(cities)

    points = {}
    inc = 0;

    collecting = True

    while collecting:
        for event in pygame.event.get():
            if event.type == QUIT:
                writeFile("result.txt", points)        
                collecting = False        
            elif event.type == KEYDOWN and event.key == K_RETURN:
                collecting = False
            elif event.type == MOUSEBUTTONDOWN:
                cities.append(pygame.mouse.get_pos())
                inc += 1
                points['v'+str(inc)] = (pygame.mouse.get_pos())
                draw(cities)
                
    pygame.quit()
    return cities
