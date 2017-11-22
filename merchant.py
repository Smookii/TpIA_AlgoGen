import sys

import random
import math
import point

def ga_solve(file = None, gui=True, maxtime=0):
    
    cities = []
    if file is None:
        cities = point.openGui()
    else:
        lines = [line.rstrip('\n') for line in open(file)]
        for line in lines:
            tabLine = line.split(' ')
            cities.append((int(tabLine[1]),int(tabLine[2])))
    
    
    cCities = cities
    actualCity = cCities.pop(0)
    hist = []
    
    count = 0
    
    record = 99999999999
    while(count < 1000):
        count += 1

        hist = []
        while len(hist) < len(cities):
            exit = False
            while exit is False:
                val = random.randint(0,len(cities)-1)
                if val not in hist:
                    exit = True
                    hist.append(val)
        
        newVal = computeDist(cities,hist)
        if newVal < record:
            record = newVal
    print(record)
    
    

    
def fRandom():
    actualDist = 90000000
    newcity = None
    for c in cCities:
        newDist = pyta(actualCity, c)
        if newDist < actualDist:
            actualDist = newDist
            newcity = c
    
    

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
        ga_solve(file = sys.argv[1],gui = False, maxtime = 2)
    else:
        ga_solve(file = None,gui = False, maxtime = 2)
    
        
    
    
    