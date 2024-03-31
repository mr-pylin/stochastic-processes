# more details about "Brownian motion": https://en.wikipedia.org/wiki/Brownian_motion

# dependencies
import turtle
from random import randint
from math import cos, pi
import matplotlib.pyplot as plt

# width & height of the window
width  = 500
height = 500

# creating a window
screen = turtle.Screen()
screen.setup(width= width, height= height)
screen.title("Brownian motion")

# creating a pen to draw
pen = turtle.Turtle()
pen.color('red')
pen.pencolor('black')
pen.speed(0)

# input from user
default_iteration = 1000
default_move_per_iter = 10

iteration = screen.textinput('iteration', "Number of iterations [e.g. 1000]:")
iteration = int(iteration) if iteration else default_iteration

move_per_iter = screen.textinput('movement', "Move per iteration [e.g. 10]:")
move_per_iter = int(move_per_iter) if move_per_iter else default_move_per_iter

can_pass_borders = screen.textinput('border', "Can pass borders? [yes/no]:").lower()
if can_pass_borders not in ['yes', 'no']:
    raise ValueError("valid inputs for passing borders are : {no | yes}")

interactive_histogram = screen.textinput('interactive histogram', "interactive histogram? [yes/no]:").lower()
if interactive_histogram not in ['yes', 'no']:
    raise ValueError("valid inputs for passing borders are : {no | yes}")

# for writing iteration on the screen
pen2 = turtle.Turtle(visible= False)
pen2.speed(0)
pen2.penup()
pen2.goto(-width / 2 + 5, +height / 2 - 20)
pen2.pendown()
pen2.write(f"iteration:", align= 'left', font=('consolas', 12, 'normal'))
pen2.penup()
pen2.goto(-width / 2 + 100, +height / 2 - 20)
pen2.pendown()
pen2.write('0', align= 'left', font=('consolas', 12, 'normal'))

def write(iteration: str) -> None:
    # move the last written iteration
    pen2.undo()

    # write the text
    pen2.write(iteration, align= 'left', font=('consolas', 12, 'normal'))

# a numpy array to store pen position for creating histogram
width_positions  = []
height_positions = []

# turn on interactive plt
plt.ion()

# create subplots
if interactive_histogram == 'yes':
    fig, axs = plt.subplots(nrows= 1, ncols= 3, figsize=(12, 4), layout= 'compressed')

# function to update and display hist2d plot
def update_hist2d():
    axs[0].clear()
    axs[0].hist(height_positions, bins= 50, color= 'salmon', edgecolor= 'black', range= (-height / 2, height / 2), orientation= 'horizontal')
    axs[0].set_title('Height Histogram')
    axs[0].set(xlabel= 'Frequency', ylabel= 'Height')

    axs[1].clear()
    axs[1].hist2d(width_positions, height_positions, bins= 50, color= 'skyblue', edgecolor= 'black', range= [(-width / 2, width / 2), (-height / 2, height / 2)])
    axs[1].set_title('2D Histogram')
    axs[1].set(xlabel= 'Width', ylabel= 'Height')

    axs[2].clear()
    axs[2].hist(width_positions, bins= 50, color= 'skyblue', edgecolor= 'black', range= (-width / 2, width / 2))
    axs[2].set_title('Width Histogram')
    axs[2].set(xlabel= 'Width', ylabel= 'Frequency')

# loop until iteration is over
for i in range(iteration):

    # get pen position and store them for histogram
    position = pen.pos()
    width_positions.append(position[0])
    height_positions.append(position[1])

    # write iteration to the screen
    write(i + 1)

    # a random angle in range 0 to 359
    angle = randint(0, 359)
    pen.setheading(to_angle= angle)

    # check the pen position to remain inside the screen or not
    if can_pass_borders == 'yes' or abs(position[0] + move_per_iter * cos(angle / 180 * pi)) < width / 2 - 5 and abs(position[1] + move_per_iter * cos(angle / 180 * pi - pi / 2)) < height / 2 - 5:
        pen.forward(distance= move_per_iter)
    
    # update histograms
    if interactive_histogram == 'yes':
        update_hist2d()

# create subplots
if interactive_histogram == 'no':
    fig, axs = plt.subplots(nrows= 1, ncols= 3, figsize=(12, 4), layout= 'compressed')

update_hist2d()

# turn off interactive plt
plt.ioff()
plt.show()

# hold the screen after iterations
screen.mainloop()