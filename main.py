import sys, pygame
from Level import Level
from Player import Player
from NeutronStar import NeutronStar
import time


pygame.init()

size = width, height = 1024, 760
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
level = Level(width, height)
fps = 1000/60
ball = pygame.image.load("circle.png")
ballRect = ball.get_rect()
nsimg = pygame.image.load("neutronstarcircle.png")
nsRect = nsimg.get_rect()
player = Player(100, 100, ball, ballRect)
neutronStar1 = NeutronStar(512, 380, nsimg, nsRect)
neutronStar2 = NeutronStar(200, 700, nsimg, nsRect)
level.addObj(neutronStar1)
level.addObj(neutronStar2)
level.addObj(player)
player.imgRect.center = (player.posX, player.posY)
for obj in level.objects:
    print(obj.posX, obj.posY)
lastUpdateTime =  int(round(time.time() * 1000))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #events = pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.goLeft()


    elif keys[pygame.K_d]:
        player.goRight()


    else:
        player.updateAccel(0, player.accelY)

    if keys[pygame.K_w]:
        player.goUp()


    elif keys[pygame.K_s]:
        player.goDown()


    else:
        player.updateAccel(player.accelX, 0)

    if keys[pygame.K_r]:
        player.posX = 100
        player.posY = 100
        player.velX = 0
        player.velY = 0
        player.accelX = 0
        player.accelY = 0
    currentTime = int(round(time.time() * 1000))
    if currentTime - lastUpdateTime > fps:
        lastUpdateTime = currentTime
        level.update()

    screen.fill(black)
    for obj in level.objects:
        screen.blit(obj.img, (obj.posX- obj.radius, obj.posY- obj.radius))
    pygame.display.flip()