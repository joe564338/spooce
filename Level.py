import math


class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = list()

    def addObj(self, obj):
        self.objects.append(obj)

    def update(self):
        movingObjs = list()
        for obj in self.objects:
            if obj.velX != 0 or obj.velY != 0 or obj.accelX != 0 or obj.accelY != 0:
                movingObjs.append(obj)
        for obj in movingObjs:
            inbounds = True
            collision = False
            for obj2 in self.objects:
                dist = math.sqrt(math.pow(obj2.posX - obj.posX, 2) + math.pow(obj2.posY - obj.posY, 2))
                if dist != 0:
                    if dist < obj.radius + obj2.radius:
                        obj.posX += obj.posX - obj2.posX
                        obj.posY += obj.posY - obj2.posY
                        collision = True
                    else:
                        if (obj2.id == "neutron star"):
                            obj2.gravPull(obj)

            if obj.velX + obj.posX + obj.radius -3 > self.width:
                #print("colliding right wall")
                inbounds = False
                obj.updatePosX(self.width - obj.radius - 4)
                obj.updateAccel(0, 0)
                obj.lrbounce()
            if obj.velX + obj.posX - obj.radius -3  < 0:
                #print(obj.velX + obj.posX - obj.radius -3)
                #print("colliding left wall")
                inbounds = False
                obj.updatePosX(0 + obj.radius +4)
                obj.updateAccel(0, 0)
                obj.lrbounce()
            if obj.velY + obj.posY + obj.radius -3 > self.height:
                #print("colliding bottom wall")
                inbounds = False
                obj.updatePosY(self.height - obj.radius -4)
                obj.updateAccel(0, 0)
                obj.udbounce()
            if obj.velY + obj.posY - obj.radius -3 < 0:
                #print("colliding top wall")
                inbounds = False
                obj.updatePosY(0 + obj.radius + 4)
                obj.updateAccel(0, 0)
                obj.udbounce()
            if inbounds and not collision:
                #print("no wall collision")
                obj.update()

    def updateObjAccel(self, id, accelX, accelY):
        for obj in self.objects:
            if obj.id == id:
                obj.accelX = accelX
                obj.accelY = accelY
