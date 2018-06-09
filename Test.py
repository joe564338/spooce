from EfficientWorld import EfficientWorld
from Player import Player
import time
from NeutronStar import NeutronStar
import random

time1 = int(round(time.time() * 1000))
player = Player(200, 200, None, None)
ns = NeutronStar(200, 350, None, None)
ns2 = NeutronStar(900, 900, None, None)
ns3 = NeutronStar(400, 250, None, None)
ew = EfficientWorld(100000, 100000, player)
ew.addObj(ns)
ew.addObj(ns2)
ew.addObj(ns3)
for x in range(300):
    ew.addObj(NeutronStar(random.randint(0, ew.width), random.randint(0, ew.height), None, None))
ew.update(100, 100)
print(int(round(time.time() * 1000)) - time1)


