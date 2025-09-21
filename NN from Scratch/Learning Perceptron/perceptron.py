import random
import pygame as pg
import sys

pg.init()

width = 500
height = 500

inner_size = 8
outer_size = 16

pg.display.set_caption("Perceptron")
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

train_mouse = False
train_auto = False
train_point = True


class Perceptron:
    lr = 0.1

    def __init__(self, inputs, weights):
        self.inputs = inputs
        self.weights = weights

    def guess(self):
        sum = 0

        # WTF why did making it a range instead of self.weights make it work.
        # I've been dealing with this for like a whole weekend!!!
        for i in range(0, 2):
            sum += self.inputs[i] * self.weights[i]

        return self.sign(sum)

    def train(self, label, guess):
        error = label - guess

        for i in range(0, 2):
            self.weights[i] += round(int(10 * (error * self.inputs[i] * Perceptron.lr)) / 10)

    # This is the Activation Function
    @staticmethod
    def sign(n):
        if n >= 0:
            return 1
        else:
            return -1


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
            color = (0, 0, 0)
        else:
            color = (100, 100, 100)

        pg.draw.ellipse(screen, color, pg.Rect(self.x, self.y, outer_size, outer_size))


points = [Point() for i in range(100)]

per = Perceptron([1, -1], [-1, 0])

# this is my try at a memory
mem = 0

training_index = 0

while True:
    screen.fill((255, 255, 255))
    pg.draw.aaline(screen, (0, 0, 0), (0, 0), (width, height))

    # Handling input
    for event in pg.event.get():
        # Quit
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    for point in points:
        # Drawing a point
        point.show()

        target = point.label
        per.inputs = [point.x, point.y]

        # Assigning inner colors
        guess = per.guess()
        if guess == target:
            cor_color = (0, 255, 0)
        else:
            cor_color = (255, 0, 0)

        pg.draw.ellipse(screen, cor_color, pg.Rect(point.x + inner_size / 2, point.y + inner_size / 2, inner_size, inner_size))

    for point in points:
        target = point.label
        per.inputs = [point.x, point.y]

        # Auto Learn
        if train_auto:
            per.train(target, per.guess())

    cur = pg.mouse.get_pressed()[0]

    # Training all the points at once if True
    if train_mouse:
        if cur == 1 and mem == 0:
            for point in points:
                target = point.label
                per.inputs = [point.x, point.y]

                per.train(target, per.guess())

    if train_point:
        training = points[training_index]
        target = training.label
        per.inputs = [training.x, training.y]

        per.train(target, per.guess())
        training_index += 1
        if training_index == len(points):
            training_index = 0

    print(per.weights)

    # Updating the window
    pg.display.update()
    clock.tick(10)

    # Updating memory
    cur = mem
