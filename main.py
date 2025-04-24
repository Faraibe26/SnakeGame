from turtle import Turtle, Screen
import random
import time

SIZE = 15

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawself(self, turtle):
        """ creation of black boxes  """

        turtle.goto(self.x - SIZE // 2 - 1, self.y - SIZE // 2 - 1)

        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(SIZE - SIZE // 10)
            turtle.left(90)
        turtle.end_fill()

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_blinking = True

    def changelocation(self):
        self.x = random.randint(0, SIZE) * SIZE - 200
        self.y = random.randint(0, SIZE) * SIZE - 200

    def drawself(self, turtle):
        if self.is_blinking:
            turtle.goto(self.x - SIZE // 2 - 1, self.y - SIZE // 2 - 1)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(SIZE - SIZE // 10)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        # blinking
        self.is_blinking = not self.is_blinking

class Snake:
    def __init__(self):
        self.headposition = [SIZE, 0]  # keeps track of where it needs to go next
        self.body = [Square(-SIZE, 0), Square(0, 0), Square(SIZE, 0)]  # body is a list of squares
        self.nextX = 1  # tells the snake which way it's going next
        self.nextY = 0
        self.crashed = False  # I'll use this when I get around to collision detection
        self.nextposition = [self.headposition[0] + SIZE * self.nextX, self.headposition[1] + SIZE * self.nextY]
        # prepares the next location to add to the snake

    def moveOneStep(self):
        if Square(self.nextposition[0], self.nextposition[1]) not in self.body:
            # attempt (unsuccessful) at collision detection
            self.body.append(Square(self.nextposition[0], self.nextposition[1]))
            # moves the snake head to the next spot, deleting the tail
            del self.body[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
            # resets the head and nextposition
            self.nextposition = [self.headposition[0] + SIZE * self.nextX, self.headposition[1] + SIZE * self.nextY]
        else:
            self.crashed = True  # more unsuccessful collision detection

    def moveup(self):  # pretty obvious what these do
        self.nextX, self.nextY = 0, 1

    def moveleft(self):
        self.nextX, self.nextY = -1, 0

    def moveright(self):
        self.nextX, self.nextY = 1, 0

    def movedown(self):
        self.nextX, self.nextY = 0, -1

    def eatFood(self):
        self.body.append(Square(self.nextposition[0], self.nextposition[1]))
        self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        self.nextposition = [self.headposition[0] + SIZE * self.nextX, self.headposition[1] + SIZE * self.nextY]

    def drawself(self, turtle):
        for segment in self.body:
            segment.drawself(turtle)

class Game:
    def __init__(self):
        self.screen = Screen()
        self.artist = Turtle(visible=False)
        self.artist.up()
        self.artist.speed("fast")

        self.snake = Snake()
        self.food = Food(100, 0)
        self.counter = 0  # this will be used later
        self.commandpending = False  # as will this

        self.screen.tracer(0)  # follow it so far?

        self.screen.listen()
        self.screen.onkey(self.snakedown, "Down")
        self.screen.onkey(self.snakeup, "Up")
        self.screen.onkey(self.snakeleft, "Left")
        self.screen.onkey(self.snakeright, "Right")

    def nextFrame(self):
        self.artist.clear()

        if (self.snake.nextposition[0], self.snake.nextposition[1]) == (self.food.x, self.food.y):
            self.snake.eatFood()
            self.food.changelocation()
        else:
            self.snake.moveOneStep()

        if self.counter == 10:
            self.food.changestate()  # makes the food flash slowly
            self.counter = 0
        else:
            self.counter += 1

        self.food.drawself(self.artist)  # show the food and snake
        self.snake.drawself(self.artist)
        self.screen.update()
        self.screen.ontimer(lambda: self.nextFrame(), 100)

    def snakeup(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.moveup()
            self.commandpending = False

    def snakedown(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.movedown()
            self.commandpending = False

    def snakeleft(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.moveleft()
            self.commandpending = False

    def snakeright(self):
        if not self.commandpending:
            self.commandpending = True
            self.snake.moveright()
            self.commandpending = False

game = Game()

screen = Screen()

screen.ontimer(lambda: game.nextFrame(), 100)

screen.mainloop()
