from GameObject import GameObject


class Player(GameObject):
    playerMass = 100
    playerMaxSpeed = 16
    playerRadius = 38
    playerAccel = 2
    laserOn = False
    laserDamage = 1
    def __init__(self, posX, posY, img, imgRect):
        GameObject.__init__(self, self.playerMaxSpeed, self.playerMass, posX, posY, self.playerRadius, "player", img, imgRect)


    def goRight(self):
        self.accelX = self.playerAccel

    def goLeft(self):
        self.accelX = -self.playerAccel

    def goUp(self):
        self.accelY = -self.playerAccel

    def goDown(self):
        self.accelY = self.playerAccel

    def activateLaser(self):
        self.laserOn= True

    def deactivateLaser(self):
        self.laserOn = False

    def brake(self):
        if self.velY != 0:
            self.accelY = -self.velY/abs(self.velY) * 2
        else: self.accelY = 0
        if self.velX != 0:
            self.accelX = -self.velX/abs(self.velX) * 2
        else: self.accelX = 0