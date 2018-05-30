import sys, pygame
from Level import Level
from Player import Player
import time


pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
level = Level(width, height)
fps = 1000/60
ball = pygame.image.load("circle.png")
ballRect = ball.get_rect()
player = Player(400, 300, ball, ballRect)
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
        print(player)

    elif keys[pygame.K_d]:
        player.goRight()
        print(player)

    else:
        player.updateAccel(0, player.accelY)

    if keys[pygame.K_w]:
        player.goUp()
        print(player)

    elif keys[pygame.K_s]:
        player.goDown()
        print(player)

    else:
        player.updateAccel(player.accelX, 0)


    currentTime = int(round(time.time() * 1000))
    if currentTime - lastUpdateTime > fps:
        lastUpdateTime = currentTime
        level.update()

    screen.fill(black)
    for obj in level.objects:
        screen.blit(obj.img, (player.posX- player.radius, player.posY- player.radius))
    pygame.display.flip()