import math
from datetime import time, timedelta

"""# Задача (решено) 1
x = 42;
print(x)
r = 5
v = (4/3) * math.pi * r**3
print(v)
# Задаем радиус
r1 = 5
# Вычисляем объем
volume = (4/3) * math.pi * r1**3

print(f"Объем сферы с радиусом {r} равен {volume}")"""

"""# Задача 2
# Стоимость одной книги
book = 249.50

# Процент скидки
discount_percentage = 40

# Стоимость книги со скидкой
discounted_price = book * (1 - discount_percentage / 100)

# Стоимость доставки
delivery_one = 100  # за первый экземпляр
delivery_two = 49.50  # за каждый дополнительный экземпляр

# Общая стоимость книг со скидкой
total_books_cost = 60 * discounted_price

# Общая стоимость доставки
total_delivery_cost = delivery_one + (59 * delivery_two)

# Итоговая сумма
total_cost = total_books_cost + total_delivery_cost

print(f"Сумма закупки 60 экземпляров составит: {total_cost:.2f} рублей.")"""

# Задача 3

fixed_time = time(6, 52)

easy_speed = timedelta(minutes=8, seconds=15) * 2
middle_speed = timedelta(minutes=7, seconds=12) * 3

jogging = 5 # км

# Поскольку `fixed_time` является объектом time, его нужно преобразовать в datetime, чтобы складывать с timedelta
fixed_time_datetime = timedelta(hours=fixed_time.hour, minutes=fixed_time.minute)

at_home = fixed_time_datetime + easy_speed + middle_speed

print(f"Ты пробежал {jogging} км.")

# Разберем время на слова
total_seconds = int(at_home.total_seconds())
hours = total_seconds // 3600 # // делим с округлением в меньшую сторону
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Домой ты вернешься в {hours} часов {minutes} минут {seconds} секунд.")

