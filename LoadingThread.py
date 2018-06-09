from EfficientWorld import EfficientWorld
import math

import threading


class LoadingThread(threading.Thread):
    def __init__(self, efficientWorld):
        threading.Thread.__init__(self)
        self.efficientWorld = efficientWorld

    def run(self):
        self.efficientWorld.loadedObjects.clear()
        self.efficientWorld.loadedObjects.append(self.efficientWorld.player)
        for obj in self.efficientWorld.objects:
            dist = math.sqrt(pow(self.efficientWorld.player.posX - obj.posX, 2) + pow(self.efficientWorld.player.posY - obj.posY, 2))
            if dist > 0 and dist < 3000:
                self.efficientWorld.loadedObjects.append(obj)