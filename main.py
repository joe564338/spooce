import sys, pygame
from Level import Level
from Player import Player
from NeutronStar import NeutronStar
from Camera import Camera
from Map import Map
from Asteroid import  Asteroid
import time


pygame.init()

size = width, height = 1024, 760
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
level = Level(4000, 4000)
fps = 1000/60
ball = pygame.image.load("circle.png")
ballRect = ball.get_rect()
nsimg = pygame.image.load("neutronstarcircle.png")
nsRect = nsimg.get_rect()
player = Player(100, 100, ball, ballRect)
neutronStar1 = NeutronStar(512, 380, nsimg, nsRect)
neutronStar2 = NeutronStar(2000, 700, nsimg, nsRect)
asteroid = Asteroid(200,3000)
level.addObj(asteroid)
level.addObj(neutronStar1)
level.addObj(neutronStar2)
level.addObj(player)
camera = Camera(player.posX, player.posY)
map = Map(width, height, player.posX, player.posY, level)
player.imgRect.center = (player.posX, player.posY)
for obj in level.objects:
    print(obj.posX, obj.posY)
lastUpdateTime =  int(round(time.time() * 1000))
mapPlayerColor = 255, 0 , 0
mapNeutronStarColor = 198, 253, 255
mapAsteroidColor = 253, 171, 0
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
    if keys[pygame.K_SPACE]:
        player.brake()

    if pygame.mouse.get_pressed()[0]:
        player.activateLaser()
    else:
        player.deactivateLaser()

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
        camera.adjustCamera(player.posX - width/2, player.posY - height/2)
        level.update(pygame.mouse.get_pos()[0] + camera.posX, pygame.mouse.get_pos()[1] + camera.posY)
        map.updateMap(player.posX, player.posY)


    screen.fill(black)


    for obj in level.objects:
        if obj.id == "player": continue
        if obj.id == "asteroid":
            #print("asteroid")
            #print("{}".format(obj.color))
            pygame.draw.circle(screen, obj.color, (int(obj.posX - camera.posX), int(obj.posY - camera.posY)), int(obj.radius))
            for i in range(len(obj.spotPos)):
                pygame.draw.circle(screen, obj.spotColor[i], (int(obj.spotPos[i][0] +obj.posX - camera.posX), int(obj.spotPos[i][1] + obj.posY - camera.posY)), int(obj.spotRadi[i]))

        if obj.img != None:
            screen.blit(obj.img, (obj.posX- obj.radius - camera.posX, obj.posY- obj.radius - camera.posY))
    if player.laserOn ==True:
        pygame.draw.line(screen, mapPlayerColor, (player.posX - camera.posX, player.posY - camera.posY), pygame.mouse.get_pos(), 3)
    screen.blit(player.img, (player.posX - player.radius - camera.posX, player.posY - player.radius - camera.posY))

    pygame.draw.lines(screen, map.lineColor, False, map.mapBox)

    for i in range(len(map.verticalGridLines)):
        pygame.draw.line(screen, map.lineColor, map.verticalGridLines[i][0], map.verticalGridLines[i][1])
        pygame.draw.line(screen, map.lineColor, map.horizontalGridLines[i][0], map.horizontalGridLines[i][1])
    for obj in map.mapObjects:
        if obj.id == "player":
            pygame.draw.circle(screen, mapPlayerColor,(obj.posX, obj.posY), 4)
        elif obj.id == "neutron star":
            pygame.draw.circle(screen, mapNeutronStarColor, (obj.posX, obj.posY), 3)
        elif obj.id == "asteroid":
            pygame.draw.circle(screen, mapAsteroidColor, (obj.posX, obj.posY), 2)

    pygame.display.flip()