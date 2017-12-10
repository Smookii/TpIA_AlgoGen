import sys
import pygame
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE
import json
import random
import math
import cv2
import time


population = 150

pygame.init()
screen_x = 800
screen_y = 800


line_color = [200,10,10]

city_color = [10,10,200] # blue
city_radius = 3
font_color = [255,255,255] # white
window = pygame.display.set_mode((screen_x, screen_y))
screen = pygame.display.get_surface()
font = pygame.font.Font(None,30)


class Path:
    def __init__(self,hist,length):
        self.hist = hist
        self.length = length


    def p(self):
        print(self.hist)
        print(self.length)


def draw(positions):
    screen.fill(0)
    for pos in positions: 
        pygame.draw.circle(screen,city_color,pos,city_radius)
    text = font.render("Nombre: %i" % len(positions), True, font_color)
    textRect = text.get_rect()
    screen.blit(text, textRect)
    pygame.display.flip()
        
def collectingPoint():
    cities = []
    draw(cities)

    points = {}
    inc = 0;

    collecting = True

    while collecting:
        for event in pygame.event.get():
            if event.type == QUIT:      
                collecting = False        
            elif event.type == KEYDOWN and event.key == K_RETURN:
                collecting = False
            elif event.type == MOUSEBUTTONDOWN:
                cities.append(pygame.mouse.get_pos())
                inc += 1
                points['v'+str(inc)] = (pygame.mouse.get_pos())
                draw(cities)

    return cities

def drawPaths(tab, cities):
    draw(cities)
    pygame.draw.lines(screen,line_color,True,tab,1)
    pygame.display.flip()

def quitDisplay():
    pygame.quit()

def ga_solve(file = None, gui=True, maxtime=0):


    cities = []
    citiesName = []
    if file is None:
        cities = collectingPoint()
    else:
        lines = [line.rstrip('\n') for line in open(file)]
        for line in lines:
            tabLine = line.split(' ')            
            cities.append((int(tabLine[1]),int(tabLine[2])))

    for i in range(0,len(cities)):
        citiesName.append('v'+str(i))

    
    time.clock()
    cCities = cities
    actualCity = cCities.pop(0)
    hist = []
    tabJourney = []
    
    count = 0
    
    while(count < population):
        count += 1

        hist = []
        while len(hist) < len(cities):
            exit = False
            while exit is False:
                val = random.randint(0,len(cities)-1)
                if val not in hist:
                    exit = True
                    hist.append(val)
        
        tabJourney.append(Path(hist,computeDist(cities,hist)))



    pourcentageCross = 0.4
    pourcentageSel = 0.2
    historyBest = []
    exitLoop = False
    while exitLoop is False:   
        tabCross = []
        for i in range(0,int(len(tabJourney)*pourcentageCross)):
            v1 = random.randint(0,len(tabJourney)-1)
            v2 = random.randint(0,len(tabJourney)-1)
            while v1 is v2:
                v2 = random.randint(0,len(tabJourney)-1)
            tabCross.append([v1,v2])

        for values in tabCross:
            cross(tabJourney, values[0],values[1],cities)

        tabJourney.sort(key=lambda x: x.length, reverse=False)
        tabJourney = selection(tabJourney, pourcentageSel)
        tabJourney.sort(key=lambda x: x.length, reverse=False)
            
        if len(historyBest) < 100:
            if tabJourney[0].length in historyBest:          
                historyBest.append(tabJourney[0].length)
            else:
                historyBest = []
                historyBest.append(tabJourney[0].length)
        else:
            exitLoop = True

        travel = []
        for i in tabJourney[0].hist:
            travel.append(citiesName[i])
        if gui is True:
            actualFastest = []
            for i in tabJourney[0].hist:
                actualFastest.append(cities[i])
            
            drawPaths(actualFastest, cities)
        else:
            quitDisplay()
        if time.clock() >= maxtime :
            break
        
    tabJourney.sort(key=lambda x: x.length, reverse=True)
    quitDisplay()
    print(historyBest[0])
    print(travel)
    return (historyBest[0], travel)


def selection(tabJourney, pourcentage):
    nbBest = int(population*pourcentage)
    tabTemp = []
    
    for i in range(0,nbBest):
        tabTemp.append(tabJourney.pop(0))

    nbRand = int(population*(1-pourcentage))

    for i in range(0,nbRand):
        tabTemp.append(tabJourney.pop(random.randint(0,len(tabJourney)-1)))

    tabJourney = []
    return tabTemp
    
    
    


def cross(tabJourney, v1, v2, cities):
    val1 = random.randint(0,int((len(cities)-1)/2))
    val2 = random.randint(int(len(cities)/2),len(cities))
    index = range(val1,val2)
    valCross1 = []
    valCross2 = []
    childHist1 = []
    childHist2 = []
    for i in index:
        valCross1.append(tabJourney[v1].hist[i])
        valCross2.append(tabJourney[v2].hist[i])
    iCpt = 0
    for i in range(0,len(tabJourney[v1].hist)):
        if i in index:
            childHist1.append(valCross2[iCpt])
            iCpt +=1
        else:
            childHist1.append(tabJourney[v1].hist[i])
            
    iCpt = 0      
    for i in range(0,len(tabJourney[v2].hist)):
        if i in index:
            childHist2.append(valCross1[iCpt])
            iCpt +=1
        else:
            childHist2.append(tabJourney[v2].hist[i])

    
    iCpt = 0    
    for i in range(0,len(tabJourney[v1].hist)):
        if i not in index:
            if tabJourney[v1].hist[i] in valCross2:
                while valCross1[iCpt] in valCross2:
                      iCpt += 1
                childHist1[i] = valCross1[iCpt]
                iCpt +=1
    iCpt = 0    
    for i in range(0,len(tabJourney[v2].hist)):
        if i not in index:
            if tabJourney[v2].hist[i] in valCross1:
                while valCross2[iCpt] in valCross1:
                      iCpt += 1
                childHist2[i] = valCross2[iCpt]
                iCpt +=1

    tabJourney.append(Path(childHist1,computeDist(cities,childHist1)))
    tabJourney.append(Path(childHist2,computeDist(cities,childHist2)))
    
    
def printPathTab(tab):
    for p in tab:
        p.p()
    print("-----------------------------------")

def computeDist(cities, hist):
    val = 0
    acutalCity = cities[hist[0]]
    for i in hist:
        if acutalCity is not hist[i]:
            val += fit(acutalCity,cities[i])
            acutalCity = cities[i]
    return val
        

def fit(val1,val2):
    v1 = abs(val1[0]-val2[0])
    v2 = abs(val1[1]-val2[1])
    return v1+v2

def pyta(val1,val2):
    v1 = pow(abs(val1[0]-val1[1]),2)
    v2 = pow(abs(val2[0]-val2[1]),2)
    return math.sqrt(v1+v2)
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ga_solve(file = sys.argv[1],gui = True, maxtime = 90)
    else:
        ga_solve(file = None,gui = True, maxtime = 90)
    
        
    
    
    
