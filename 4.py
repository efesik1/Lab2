try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Ошибка: деление на ноль")

except ValueError:
    print("Ошибка: введены нечисловые значения")

finally:
    print("Программа завершена")