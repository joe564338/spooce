from scipy.spatial import cKDTree
import math




class EfficientWorld:
    def __init__(self, width, height, player):
        self.width = width
        self.height = height
        self.objects = list()
        self.player = player
        self.objects.append(player)
        self.loadedObjects = list()

    def addObj(self, obj):
        self.objects.append(obj)

    def update(self, mouseX, mouseY):
        objCoords = list()
        for obj in self.objects:
            objCoords.append((obj.posX, obj.posY))
        objTree = cKDTree(objCoords)

        for obj in self.objects:
            objVel = math.sqrt(pow(obj.velX, 2) + pow(obj.velY, 2))
            possibleCollisions = objTree.query((obj.posX, obj.posY), 15, 0, 2, obj.radius * 10 + objVel)

            for x in range(len(possibleCollisions[1])):
                if possibleCollisions[1][x] >= len(self.objects) or possibleCollisions[0][x] == 0.0:
                    continue
                #print(possibleCollisions[0][x])
