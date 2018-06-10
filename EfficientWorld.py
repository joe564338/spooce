from scipy.spatial import cKDTree
import math




class EfficientWorld:
    def __init__(self, width, height, player, screenWidth, screenHeight):
        self.width = width
        self.height = height
        self.objects = list()
        self.player = player
        self.objects.append(player)
        self.loadedObjects = list()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def addObj(self, obj):
        self.objects.append(obj)

    def update(self, mouseX, mouseY):
        objCoords = list()
        movingObj = list()
        for obj in self.objects:
            objCoords.append((obj.posX, obj.posY))
            if obj.velX != 0 or obj.velY != 0:
                movingObj.append(obj)
        objTree = cKDTree(objCoords)

        for obj in movingObj:
            objVel = math.sqrt(pow(obj.velX, 2) + pow(obj.velY, 2))
            possibleCollisions = objTree.query((obj.posX, obj.posY), 50, 0, 2, self.screenWidth + self.screenHeight)
            inbounds = True
            collision = False
            for x in range(len(possibleCollisions[1])):

                if possibleCollisions[0][x] == 0.0:
                    continue
                elif possibleCollisions[1][x] >= len(self.objects):
                    break
                print(possibleCollisions[0][x])

