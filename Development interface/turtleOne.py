import turtle
import math
# import tkinter
# print(tkinter.TkVersion)

# bob = turtle.Turtle()
# print(bob)

# bob.fd(100)
# bob.bk(100) # назад
# bob.lt(100) # влево
# bob.rt(100) # вправо
# bob.pu(100) # перо вверх
# bob.pd(100) # перо вниз

"""# вариант 1
bob.fd(100)
bob.lt(90)
bob.fd(100)"""

"""# вариант 2 - звездечка
for i in range(100):
    bob.forward(i * 10)
    bob.right(144)
"""

"""# вариант 3 - мандалы и узоры
for i in range(36):
    bob.circle(100)
    bob.right(10)"""

"""# Анимация игры через клавиатуру
def move_forward():
    bob.forward(58)"""

"""# Рисование с клавиатуры
def move_up():
    bob.setheading(90)
    bob.forward(20)

def move_down():
    bob.setheading(270)
    bob.forward(20)

def move_left():
    bob.setheading(180)
    bob.forward(20)

def move_right():
    bob.setheading(0)
    bob.forward(20)

turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

bob.write("Hello, Turtle!", font=("Arial", 16, "normal"))"""

"""# Рисование при помощи мыши
def set_position(x, y):
    bob.goto(x, y)

turtle.onscreenclick(set_position)"""

"""# рисование звезд и других фигур
for _ in range(100):
    bob.forward(200)
    bob.right(100)"""

"""# Создание пиксельных рисунков
def draw_square(color):
    bob.fillcolor(color)
    bob.begin_fill()
    for _ in range(4):
        bob.forward(20)
        bob.left(90)
    bob.end_fill()

bob.penup()
bob.goto(-100, 100)
bob.pendown()

colors = ["red", "blue", "green", "yellow", "purple"]
for i in range(5):
    draw_square(colors[i])
    bob.forward(22)"""

"""# Квадрат 1
def square(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

bob = turtle.Turtle()
square(bob, 150)"""

"""#  n-сторонний правильный многоугольник
def polygon(t, n, length):
    angle = 360 / n # Угол поворота
    for _ in range(n):
        t.forward(length)
        t.left(angle)

bob = turtle.Turtle()
polygon(bob, 6, 100) #Рисуем шестиугольник со стороной 100"""


"""# Вариант - круг
def polygon(t, n, length):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def circle(t, r):
    circumference = 2 * 3.14159 * r # длина окружности
    n = 100 # количество сторон (чем больше, тем круглее)
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()
circle(bob, 100) # рисуем круг с радиусом 100"""

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

turtle.mainloop()









