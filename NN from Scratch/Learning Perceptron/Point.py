class Point:
    def __init__(self, x=None, y=None):
        if not x and not y:
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)
        else:
            self.x = x
            self.y = y

        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    def show(self):
        if self.label == 1:
            color = (0, 0, 0)
        elif self.label == -1:
            color = (0, 0, 255)
        else:
            color = (100, 100, 100)

        pg.draw.ellipse(screen, color, pg.Rect(self.x, self.y, 8, 8))

