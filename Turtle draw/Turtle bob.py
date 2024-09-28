import math
import turtle


def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r + 50)
    t.pd()


def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        petal(t, r, angle/1.05)
        t.lt(angle)

# Для лепестков
def petal(t, r, angle):
    for _ in range(2):
        t.circle(r, angle)
        t.lt(180 - angle)

# Для равнобедренного угольника
# def isosceles(t, r, angle):
#     y = r * math.sin(angle * math.pi / 180)

#     t.rt(angle)
#     t.fd(r)
#     t.lt(90+angle)
#     t.fd(2*y)
#     t.lt(90+angle)
#     t.fd(r)
#     t.lt(180-angle)


bob = turtle.Turtle()
bob.speed(20)

bob.pu()
bob.bk(130)
bob.pd()

size = 250
# draw_pie(bob, 5, size)
# draw_pie(bob, 6, size)
# draw_pie(bob, 7, size)
draw_pie(bob, 8, size)
draw_pie(bob, 20, size)

bob.hideturtle()
turtle.mainloop()