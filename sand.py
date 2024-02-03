# import the pygame module, so you can use it
import pygame
import math
import random
def gridi():
    global rez
    linia = 0
    while linia < width:
        linia += rez
        pygame.draw.line(screen, (20, 20, 20), (linia, 0), (linia, height), width=1)
    linia = 0
    while linia < height:
        linia += rez
        pygame.draw.line(screen, (20, 20, 20), (0, linia), (width, linia), width=1)


def calc_pozycja(x,y):
    global rez
    x = math.floor(x/rez)
    y = math.floor(y/rez)
    return x,y
def piasek_draw(pias):
    global rez
    global R
    global G
    global B
    for x,i in enumerate(pias):
        if 1 in i:
            for y,z in enumerate(i):
                pygame.draw.rect(screen, (R*z, G*z, B*z),(x*rez,y*rez,rez,rez),)
                #if z == 1:
                    #R, G, B = colorchange(R, G, B)

def colorchange(r,g,b):
    r += 5
    if r > 255:
        r = 10
        g += 5
        if g > 255:
            g = 0
            b += 5
            if b > 255:
                b = 0
    return r,g,b
def grawitacja(piasgw):
    for level,i in enumerate(piasgw):
        if 1 in i:
            for row,j in enumerate(i[::-1]):
                gdzie = []
                row = len(i) - row -1
                if j == 1:
                    if row + 1 < len(i):
                        if piasgw[level][row + 1] == 0:
                            piasgw[level][row + 1] = 1
                            piasgw[level][row] = 0
                        else:
                            if level - 1 > -1:
                                if piasgw[level-1][row + 1] == 0:
                                    gdzie.append(-1)
                            if level + 1 < len(piasgw):
                                if piasgw[level + 1][row + 1] == 0:
                                    gdzie.append(1)
                            if len(gdzie) > 0:
                                piasgw[level + random.choice(gdzie)][row + 1] = 1
                                piasgw[level][row] = 0

    return piasgw


if __name__ == "__main__":

    piasek = []
    R,G,B = 214, 178, 128
    pygame.init()
    width, height = 1920,1080
    rez = 10
    screen = pygame.display.set_mode((width,height))
    for i in range(int(width/rez)):
        tempo = []
        for j in range(int(height/rez)):
            tempo.append(0)
        piasek.append(tempo)
    print(piasek)

    running = True
    while running:
        #dodaj = random.randint(0, width/rez-1)

        if pygame.mouse.get_pressed()[0]:
            pozycjax,pozycjay = pygame.mouse.get_pos()
            pozycjax,pozycjay = calc_pozycja(pozycjax,pozycjay)
            if pozycjax < width-rez and pozycjay < height and pozycjax > -rez and pozycjay > -rez:
                piasek[pozycjax][pozycjay] = 1

        if pygame.mouse.get_pressed()[2]:
            pozycjax, pozycjay = pygame.mouse.get_pos()
            pozycjax, pozycjay = calc_pozycja(pozycjax, pozycjay)
            if pozycjax < width - rez and pozycjay < height and pozycjax > -rez and pozycjay > -rez:
                piasek[pozycjax][pozycjay] = 0

        #pozycjax, pozycjay = dodaj,0
        #if pozycjax < width - rez and pozycjay < height and pozycjax > -rez and pozycjay > -rez:
            #piasek[pozycjax][pozycjay] = 1
        piasek = grawitacja(piasek)
        piasek_draw(piasek)
        gridi()
        pygame.display.flip()
        #pygame.time.wait(20)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
