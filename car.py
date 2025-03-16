from turtle import *
import random
class Car:
    def __init__(self, speed, color, fname, locate, goal):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)
        self.locate = locate
        self.goal = goal
        
    def drive(self, distance):
        self.turtle.forward(distance)

    def goto(self, x, y):
        self.turtle.goto(x, y)

    def turnleft(self, degree):
        self.turtle.left(degree)

    def write(self, write):
        self.turtle.write(write)

    def hide(self):
        self.turtle.hideturtle()

register_shape("car2.gif")

car_list = []
y=-100
n=0
for i in range(3):
    car_list.append(Car(10, "red", "car2.gif", -400, 0))

for car in car_list:
    car.turtle.penup()
    car.goto(-400, y)
    car.turtle.pendown()
    y+=100

for i in range(400):
    for car in car_list:
        speed = random.randint(2, 20)
        if car.locate < 400:
            if car.locate + speed >= 400:
                speed = 400 - car.locate
                n+=1
                car.goal = 1
                car.hide()
            car.drive(speed)
            if car.goal == 1:
                car.write(str(n)+"등")
        car.locate += speed
