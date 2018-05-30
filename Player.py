from GameObject import GameObject


class Player(GameObject):
    playerMass = 100
    playerMaxSpeed = 16
    playerRadius = 38
    playerAccel = 2
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

