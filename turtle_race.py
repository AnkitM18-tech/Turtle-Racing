#Importing Libraries
import turtle
import tkinter
import time
import random

#Dimensions and Params
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'yellow', 'orange',
          'black', 'purple', 'pink', 'brown', 'cyan']

#Getting number of Turtles
def get_number_of_racers():
    racers = 0 
    while True:
        racers = input('Enter the number of Turtles (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('\n[INVALID INPUT]: Input is not Numeric...')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('\n[INVALID INPUT]: Number not in range (2 - 10). Try again...')

#Turtle Positioning 
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            _,y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

#Turtle Creation
def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

#Initializing Turtles

def init_turtle():
    screen = turtle.Screen()
    screen.bgcolor("White")
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Race")
    icon = tkinter.Image('photo', file = 'icon.png')
    turtle._Screen._root.iconphoto(True, icon)


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f'\nThe winner is {winner}!')
time.sleep(5)