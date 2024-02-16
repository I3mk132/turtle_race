# import library
import turtle
import time

# window size
WIDTH, HEIGHT = 500, 500


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


Racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.shape("turtle")
racer.color("blue")
racer.speed(1)
racer.penup()

racer.forward(100)
racer.right(90)
racer.forward(100)
racer.right(45)
racer.backward(100)
racer.left(90)
racer.forward(100)
time.sleep(5)
