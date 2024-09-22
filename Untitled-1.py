"""example 1
C = 2 + 5
print (C)
C = 2 - 5
print (C)
C = 2 * 5
print (C)
C = 2 / 5
print (C)"""

"""example 2
sample = input("Введите число: ")
sampleTwo = int(sample) + 2
print(f"Ответ: {sampleTwo}")"""

"""# ex 3
print("France is a beautiful country,", end=" Isn't \
it true?")"""

"""# ex 4
def decimal_to_hexadecimal(decimal_number):
    if decimal_number < 0:
        return "-" + hex(decimal_number)[3:].upper()
    return hex(decimal_number)[2:].upper()

# Пример использования
decimal_number = int(input("Введите десятичное число: "))
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(f"Шестнадцатеричное представление: {hexadecimal_number}")"""

"""# ex 5
x = 3
y = 4

result = 2 * x + 3 * y
print(f"Результат равен: {result}")"""

"""# ex 6
def sample():
    example = "This is a trail"
    print(example)

sample()"""

# example = "Today it will rain"
# print(len(example))

"""x = [32, 23, 12, 45, 56, 22, 16]
x.sort()
print(x)

x_two = ['USA', 'China', 'Russia', 'UK', 'Japan']
x_two.sort(reverse=True) # сортировка по убыванию
print(x_two)"""

"""capitals = {'USA': 'Washington', 'Russia': 'Moscow', \
'China': 'Beijing'}
print(capitals)"""


# x = "Sample"
# print(ord(x[1]))


"""y = 0
z = 1
x = int(input("Enter number: "))
while z <= x:
    y = y + z
    z = z + 1
print("The sum of numbers is: ", y)
"""

"""d = [23, 11, 12, 56]
sample = " ~ "
sample = sample.join(map(str, d))
print(sample)"""

"""# ex 7
class Geography:
    attr1 = "country"

    def __init__(self, country_name):
        self.country_name = country_name

    def governance(self):
        print("This country is {}".format(self.country_name))
        
USA = Geography("USA")
UK = Geography("UK")
USA.governance()
UK.governance()"""


"""# ex 8
# Определение класса Polygon
class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def dispsides(self):
        for i in range(self.sides):
            print("side", i+1)

# Определение класса Square на основе Polygon
class Square(Polygon):
    def __init__(self):
        self.sides = int(input("Side of the quare: "))

    def ind_area(self):
        a = self.sides
        # Вычисление площади
        s = a * a
        print("The area of the square is", s)
# Определение многоугольника с 5 сторонами
x = Polygon(5)
x.dispsides()
# Программа определяет квадрат, запрашивает длину
# стороны у польщователя и ычисляет его площадь
x2 = Square()
x2.ind_area()"""

