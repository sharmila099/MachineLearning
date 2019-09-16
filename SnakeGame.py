
# coding: utf-8

# In[3]:


# Import the required libraries
import turtle
import time
import random

# Define and initiate the variables
score = 0
high_score = 0
delay = 0.5

# Set up the screen
wn = turtle.Screen() 
wn.title("Snake Game")
wn.bgcolor("orange")
wn.setup(width = 600, height = 600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0) # Animation speed
head.shape("square")
head.color("black")
head.penup() 
head.goto(0,0)
head.direction = "up"

# Initialize empty list for body
segments = [] 

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white") # Text colour
pen.penup() # Not going to draw any lines
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 24, "normal")) 

# Functions
def go_up():
    '''Function to move in the upward direction'''
    head.direction = "up"
    
def go_down():
    '''Function to move in the downward direction'''
    head.direction = "down"
    
def go_left():
    '''Function to move in the left direction'''
    head.direction = "left"
    
def go_right():
    '''Function to move in the right direction'''
    head.direction = "right"
    
def move():
    '''Function to move in the direction as required by 20 pixels'''
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) # Move by 20 pixels
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
def fn_clear():
        '''Function to clear the screen'''
        segments.clear()
                
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
                
# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "w") 
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()
    
    # Check for a collision with the border walls
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
        # Hide the segments in case of a collision with the border wall
        for segment in segments:
            segment.goto(1000,1000)
                    
        # Reset the score
        score = 0
        fn_clear() 
        
        # Reset the delay
        delay = 0.5
    
    # Check for collision with the food
    if head.distance(food) < 20: 
        # Each of the basic turtle shape is 20 pixels wide by 20 pixels in length. 
        # If distance between them is less than 20 , it means that they have collided.
        
        # Move the food to a random spot on screen. 
        x = random.randint(-290,290) 
        y = random.randint(-290,290)
        food.goto(x,y)
        # Screen is (-600, 600) with centre as (0,0). Since each shape is (20,20), the center of each shape is at (10,10). 
        # Hence the borders are at (-300,300) and the food center can be placed at (-290,290).
    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # Shorten the delay
        delay -= 0.001
        
        # Increase the score
        score += 10
        
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    # Move the end segments first in reverse order when the len(segments) > 1
    for index in range(len(segments)-1, 0, -1):
        # Step size = 1 in reverse order
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Hide the segments in case of a collision 
            for segment in segments:
                segment.goto(1000,1000)

            # Reset the score
            score = 0
            fn_clear()
            
            # Reset the delay
            delay = 0.5
            
    time.sleep(delay)
      
# Call the main function
wn.mainloop()

