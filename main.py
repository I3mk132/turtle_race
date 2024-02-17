# import library
import turtle
import time
import random

# window size
WIDTH, HEIGHT = 500, 800
COLORS = [
    'red', 'green', 'blue',
    'cyan', 'yellow', 'pink',
    'purple', 'orange', 'black',
    'gray'
]


# set amount of turtles
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("How many racers would you like to choose(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("please enter a number.")
            continue
        if 10 >= racers >= 2:
            return racers
        else:
            print("inter a number between 2 - 10")


def init_turtle():
    # open window
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")


def race(colors):
    turtles = creating_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2-10 :
                return colors[turtles.index(racer)]



def creating_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


Racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:Racers]

winner = race(colors)
print(f'the winner is {winner} turtle!!!')
