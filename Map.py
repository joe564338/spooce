class Map:
    def __init__(self, windowSizeX, windowSizeY):
        self.mapBox = ((windowSizeX -200, windowSizeY), (windowSizeX - 200, windowSizeY -200), (windowSizeX, windowSizeY - 200))
        self.lineColor = 255, 255, 255
