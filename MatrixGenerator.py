import pygame
import sys
import random
import time
pygame.init()
res = (1300,750)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.list_modes()
color = (255,255,255)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel',16)

datab = '''


'''
names = {}
dloop = 2
brake = 1
screen.fill((255,255,255) )

y = 1020
x =1700
nameslist = []
time.sleep(0.1)
while brake != 0:
    dloop = dloop + 1
    data = datab.split('\n')
    if data[dloop+1] == "":
        brake = 0
    data = data[dloop].split(" <-> ")
    acc1 = data[0]
    data = data[1].split(": ")
    acc2 = data[0]
    score = data[2]

    if acc1 in names:
        ruh111 = names.get(acc1)
    else:
        ruh1 = random.randint((40),x)
        ruh2 = random.randint((40),y)
        names[acc1] = ruh1 , ruh2
        nameslist.append(acc1)
        ruh111 = ruh1 , ruh2

    if acc2 in names:
        ruh222 = names.get(acc2)

    else:

        ruh12 = random.randint((30),x)
        ruh22 = random.randint((30),y)
        names[acc2] = ruh12 , ruh22
        nameslist.append(acc2)
        ruh222 = ruh12 , ruh22
    pygame.draw.line(screen, (0,0,0), ruh111, ruh222, 1)
    for i in range(len(names)):

        nameslist[i]
        pygame.draw.rect(screen,(255,255,255),(    names[nameslist[i]][0], names[nameslist[i]][1]   , (len(nameslist[i]))*10 , 20))
        screen.blit(smallfont.render(nameslist[i] , True , (0,0,0)) , names.get(nameslist[i] ))

    pygame.draw.rect(screen,(255,255,255),(      (ruh111[0] + ruh222[0])/2       ,    (ruh111[1] + ruh222[1])/2      , 20 , 20 ))
    score =  float(score[0:4])
    screen.blit(smallfont.render(str(score) , True , (      ((1-score)*(255))  ,  score*255 ,0      ))         ,  (  (ruh111[0] + ruh222[0])/2   ,  (ruh111[1] + ruh222[1])/2       )   )
    

    pygame.display.update()
    time.sleep(0.1)
pygame.display.update()
time.sleep(6)
pygame.quit()
