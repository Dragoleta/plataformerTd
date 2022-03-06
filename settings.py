from random import randint



#level generator
mapWidth, mapHeight = 500, 50
def mapNoiseCreator(noiseDensity):
    noiseMap = []
    for y in range(mapHeight):
        innerNoise = []
        for x in range(mapWidth):
            random = randint(0,101)
            if y < mapHeight//2:
                innerNoise.append(' ')
            elif y == mapHeight//2 + 1:
                innerNoise.append('X')
            else:
                if random > noiseDensity:
                    innerNoise.append('X') #floor
                else:
                    innerNoise.append(' ') # wall
        noiseMap.append(innerNoise)
    return noiseMap

def mapAutomaton(runs):
    noiseMap = mapNoiseCreator(40)
    
    for count in range(runs):
        tempMap = noiseMap.copy()
        for y in range(winHeight):
            for x in range(winWidth):
                print(tempMap[[x][y]])                

# game settings
fps = 60
levelMap = mapNoiseCreator(20)
tileSize = 12
winWidth = 1000
print(len(levelMap))
winHeight = len(levelMap) * tileSize