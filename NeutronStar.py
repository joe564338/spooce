from GameObject import GameObject
import math

class NeutronStar(GameObject):
    mass = 1000
    radius = 20
    maxSpeed = 0

    def __init__(self, posX, posY, img, imgRect):
        GameObject.__init__(self, self.maxSpeed, self.mass, posX, posY, self.radius, "neutron star", img, imgRect)

    def getDist(self, obj):
        return math.sqrt(math.pow(self.posX - obj.posX, 2) + math.pow(self.posY - obj.posY, 2))

    def gravPull(self, obj):
        dist = self.getDist(obj)
        mag = (self.mass/dist)/10
        if dist < 200:
            accDeltaX = mag * (self.posX - obj.posX)/dist
            accDeltaY = mag * (self.posY - obj.posY)/dist
            obj.updateAccel(obj.accelX + accDeltaX, obj.accelY + accDeltaY)

