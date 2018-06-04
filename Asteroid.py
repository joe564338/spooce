from GameObject import GameObject
import random

class Asteroid(GameObject):
    color = 176, 126, 86
    color1 = 253, 171, 0
    color2 = 193, 193, 193
    maxSpeed = 2
    def __init__(self, posX, posY):
        mass = random.randint(30,60)
        radius = mass/2
        spots = random.randint(2, 7)
        GameObject.__init__(self, self.maxSpeed, mass, posX, posY, radius, "asteroid", None, None)
        self.spotRadi = list()
        self.spotPos = list()
        self.spotColor = list()
        self.hp = mass
        for i in range(spots):
            self.spotRadi.append(random.randint(2,9))
            self.spotPos.append([random.randint(0, int(self.radius - self.spotRadi[i])), random.randint(0, int(self.radius - self.spotRadi[i]))])
            if random.random() > .5:
                self.spotColor.append(self.color1)
            else:
                self.spotColor.append(self.color2)



