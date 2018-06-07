from scipy.spatial import cKDTree
import math



class EfficientWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = list()

    def addObj(self, obj):
        self.objects.append(obj)

    def update(self, mouseX, mouseY):
        collisionTree = cKDTree(self.objects)
        collisionTree.query()
