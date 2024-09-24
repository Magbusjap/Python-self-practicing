from __future__ import print_function, division


"""# Функция, которая ничего не возвращает.
def text_one():
    print("И бескрайние горы")
    print("И бескрайние моря")

def text_two():
    print("Всё это моё")
    print("Моё, родное!")

def total_text():
    text_one()
    text_two()

total_text()"""

"""# Задача-функция 1
def right_justify(s=" " * 70):
    print(f"{s}monty")

right_justify()"""

"""# Задача-функция 2
def do_twice (f):
    f()
    f()

def print_spam():
    print("Спам")

do_twice(print_spam)"""

"""# Вариант 2
def do_twice (f, value):
    f(value * 4) 
    

def print_spam(msg):
    print(msg)

do_twice(print_spam, ' Спам ')"""


"""def square_draw(val1, val2):
    val1 = '+'
    val2 = "-"
    print()"""


# here is a mostly-straightforward solution to the
# two-by-two version of the grid.
"""
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
    

# here is a less-straightforward solution to the
# four-by-four grid

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()


"""

def print_beam():
    print("+ - - - - " * 2 + "+", end="\n")

def print_post():
    print(("|         " * 2 + "|"), end="\n")

def print_row():
    print_beam()
    print_post()
    print_post()
    print_post()
    print_post()

def print_grid():
    print_row()
    print_row()
    print_beam()

print_grid()



