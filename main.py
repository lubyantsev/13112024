# Задача 1 (просто) "Арифметика":
# 1st program
result1 = (9 ** 0.5) * 5
print(result1)  # Ожидаемый результат: 15.0

# Задача 2 (просто) "Логика":
# 2nd program
result2 = (9.99 > 9.98) and (1000 != 1000.1)
print(result2)  # Ожидаемый результат: True

# Задача 3 (средне) "Школьная загадка":
# 3rd program
result3_1 = 2 * 2 + 2  # Без приоритета
result3_2 = 2 * (2 + 2)  # С приоритетом
print(result3_1)  # Ожидаемый результат: 6
print(result3_2)  # Ожидаемый результат: 8
print(result3_1 == result3_2)  # Ожидаемый результат: False

# Задача 4 (сложно) "Первый после точки":
# 4th program
string_number = '123.456'
float_number = float(string_number)  # Преобразуем строку в дробное число
shifted_number = float_number * 10  # Умножаем на 10
int_number = int(shifted_number)  # Преобразуем в целое число
first_digit_after_decimal = int_number % 10  # Получаем первую цифру после запятой
print(first_digit_after_decimal)  # Ожидаемый результат: 4