import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((211, 211, 211))

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 2)


circle(screen, red, (250,180), 20)
circle(screen, red, (155, 180),25)
circle(screen, black, (250,180), 20, 2)
circle(screen, black, (155, 180),25, 2)

circle(screen, black, (155, 180), 15)
circle(screen, black, (250,180), 10)

rect(screen, black, (165, 250, 80, 15))

line(screen, black, (220,160), (290,140), 10)
line(screen, black, (190, 160),(105,115),10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

black = (0, 0, 0)
red = (255, 0, 0)
grey = (211,211,211)
sun = (255,250,205)
dark = (105,105,105)
green =(46,139,87)
white = (255,255,255)


screen.fill((64,224,208))

'''Солнце'''
surface = pygame.Surface((300, 300))
surface.set_alpha(150)
surface.set_colorkey((0,0,0,0))
line(surface, sun, (100,80), (280,80), 15)
line(surface, sun, (190, 170),(190,-10),15)
circle(surface, sun, (190, 80), 90, 15)
circle(screen, sun, (290, 80), 10)
circle(screen, sun, (373, 80), 9)
circle(screen, sun, (207, 80), 8)
circle(screen, sun, (290, 166), 7)
screen.blit(surface, (100, 0))

'''Земля'''
line(screen, grey, (0,300), (400,300), 200)
line(screen, black, (0,200), (400,200), 1)

'''Добрый монстр-рыбак'''
ellipse(screen, grey, (65, 115, 90, 50))
ellipse(screen, black, (65, 115, 90, 50),1)

circle(screen, black, (100, 135), 3)
circle(screen, black, (152,135), 3)

ellipse(screen, grey, (5, 150, 120, 180))
ellipse(screen, black, (5, 150, 120, 180),1)

arc(screen, black, (130, 80, 300, 400), 1.6, 3, 3)


ellipse(screen, grey, (100, 175, 65, 35))
ellipse(screen, black, (100, 175, 65, 35),1)

ellipse(screen, grey, (70, 270, 90, 70))
ellipse(screen, black, (70, 270, 90, 70),1)

ellipse(screen, grey, (70, 270, 90, 70))
ellipse(screen, black, (70, 270, 90, 70),1)

ellipse(screen, grey, (110, 320, 70, 25))
ellipse(screen, black, (110, 320, 70, 25),1)

'''Пруд'''
ellipse(screen, dark, (230, 275, 130, 50))
ellipse(screen, green, (240, 295, 110, 30))

''' Удочка'''
line(screen, black, (275,80), (275,308), 1)
arc(screen, black, (75, 55, 100, 100), 4.2, 5.2, 1)

'''Рыба'''
polygon(screen, red, [[260, 330], [240, 350], [280, 350]])
polygon(screen, black, [[260, 330], [240, 350], [280, 350]],1)
polygon(screen, red, [[250, 345], [250, 363], [235, 360]])
polygon(screen, black, [[250, 345], [250, 363], [235, 360]],1)
polygon(screen, red, [[267, 345], [267, 363], [282, 368]])
polygon(screen, black, [[267, 345], [267, 363], [282, 368]],1)
polygon(screen, green, [[235, 348], [210, 358], [210, 338]])
polygon(screen, black, [[235, 348], [210, 358], [210, 338]],1)
ellipse(screen, green, (230, 338, 60, 20))
ellipse(screen, black, (230, 338, 60, 20),1)
ellipse(screen, black, (276, 343, 10, 10))
ellipse(screen, white, (280, 345, 5, 5))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()


