class GameObject:
    def __init__(self, maxSpeed, mass, posX, posY, radius, id, img, imgRect):
        self.maxSpeed = maxSpeed
        self.mass = mass
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.velX = 0
        self.velY = 0
        self.accelX = 0
        self.accelY = 0
        self.id = id
        self.img = img
        self.imgRect = imgRect

    def update(self):
        self.posX += self.velX
        self.posY += self.velY
        self.velX += self.accelX
        self.velY += self.accelY
        if self.imgRect != None:
            self.imgRect.move([self.velX, self.velY])
        if self.velX >= self.maxSpeed:
            self.velX = self.maxSpeed
        elif self.velX <= -self.maxSpeed:
            self.velX = -self.maxSpeed
        if self.velY >= self.maxSpeed:
            self.velY = self.maxSpeed
        elif self.velY <= -self.maxSpeed:
            self.velY = -self.maxSpeed

    def updateAccel(self, accelX, accelY):
        self.accelY = accelY
        self.accelX = accelX

    def updatePosX(self, posX):
        self.posX = posX
        self.imgRect.center = (posX, self.posY)

    def updatePosY(self, posY):
        self.posY = posY
        self.imgRect.center = (self.posX, posY)

    def lrbounce(self):
        self.velX = -self.velX

    def udbounce(self):
        self.velY = -self.velY



    def __str__(self):
        return "Accel: {}, {} Vel: {}, {} Pos: {}, {}".format(self.accelX, self.accelY, self.velX, self.velY, self.posX, self.posY)