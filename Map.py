class Map:
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

    def updateMap(self, playerPosX, playerPosY):
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        scaleX = playerPosX/8
        scaleY = playerPosY/8
        print("Scales" + str(scaleX) +", " + str(scaleY))
        for i in range(len(self.horizontalGridLines)):
            for j in range(len(self.horizontalGridLines[i])):
                self.horizontalGridLines[i][j][1] = self.windowSizeY - ((self.horizontalGridLinesConst[i][j][1] + scaleY) % 200)
                self.verticalGridLines[i][j][0] = self.windowSizeX - ((self.verticalGridLinesConst[i][j][0] + scaleX) % 200)
                


