from GameObject import GameObject

class Map:
    mapCoverage = 2000
    mapScale = 10
    def __init__(self, windowSizeX, windowSizeY, playerPosX, playerPosY, level):
        self.mapBox = ((windowSizeX -200, windowSizeY), (windowSizeX - 200, windowSizeY -200), (windowSizeX, windowSizeY - 200))
        self.lineColor = 255, 255, 255
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.level = level
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.mapWidth = 200
        self.mapHeight = 200
        self.horizontalGridLinesConst = (((windowSizeX - 200,windowSizeY), (windowSizeX, windowSizeY)),((windowSizeX - 200, windowSizeY - 150), (windowSizeX, windowSizeY - 150)), ((windowSizeX - 200, windowSizeY - 100), (windowSizeX, windowSizeY - 100)), ((windowSizeX - 200, windowSizeY - 50), (windowSizeX, windowSizeY - 50)))
        self.verticalGridLinesConst = (((windowSizeX - 200,windowSizeY), (windowSizeX - 200, windowSizeY - 200)),((windowSizeX -150, windowSizeY), (windowSizeX - 150, windowSizeY - 200)), ((windowSizeX -100, windowSizeY),(windowSizeX - 100, windowSizeY -200)), ((windowSizeX - 50, windowSizeY), (windowSizeX - 50, windowSizeY - 200)))
        self.verticalGridLines = [[[windowSizeX - 200,windowSizeY], [windowSizeX - 200, windowSizeY - 200]],[[windowSizeX -150, windowSizeY], [windowSizeX - 150, windowSizeY - 200]], [[windowSizeX -100, windowSizeY],[windowSizeX - 100, windowSizeY -200]], [[windowSizeX - 50, windowSizeY], [windowSizeX - 50, windowSizeY - 200]]]
        self.horizontalGridLines = [[[windowSizeX - 200,windowSizeY], [windowSizeX, windowSizeY]],[[windowSizeX - 200, windowSizeY - 150], [windowSizeX, windowSizeY - 150]], [[windowSizeX - 200, windowSizeY - 100], [windowSizeX, windowSizeY - 100]], [[windowSizeX - 200, windowSizeY - 50], [windowSizeX, windowSizeY - 50]]]
        self.mapObjects = list()


    def updateMap(self, playerPosX, playerPosY):
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        scaleX = playerPosX/10
        scaleY = playerPosY/10
        self.mapObjects.clear()
        for obj in self.level.objects:
            if obj.id == "player":
                self.mapObjects.append(GameObject(0,0, self.windowSizeX - 100, self.windowSizeY - 100, 0, "player", None, None))
            elif obj.id == "neutron star":
                distX = obj.posX - playerPosX
                distY = obj.posY - playerPosY
                if abs(distX) < self.mapCoverage/2 and abs(distY) < self.mapCoverage/2:
                    mapObjPosX = int(self.windowSizeX - (100 - distX/self.mapScale))
                    mapObjPosY = int(self.windowSizeY - (100 - distY/self.mapScale))
                    self.mapObjects.append(GameObject(0, 0, mapObjPosX, mapObjPosY,0, "neutron star", None, None))
            elif obj.id == "asteroid":
                distX = obj.posX - playerPosX
                distY = obj.posY - playerPosY
                if abs(distX) < self.mapCoverage / 2 and abs(distY) < self.mapCoverage / 2:
                    mapObjPosX = int(self.windowSizeX - (100 - distX / self.mapScale))
                    mapObjPosY = int(self.windowSizeY - (100 - distY / self.mapScale))
                    self.mapObjects.append(GameObject(0, 0, mapObjPosX, mapObjPosY, 0, "asteroid", None, None))

        for i in range(len(self.horizontalGridLines)):
            for j in range(len(self.horizontalGridLines[i])):
                self.horizontalGridLines[i][j][1] = self.windowSizeY - ((self.horizontalGridLinesConst[i][j][1] + scaleY) % 200)
                self.verticalGridLines[i][j][0] = self.windowSizeX - ((self.verticalGridLinesConst[i][j][0] + scaleX) % 200)



