def process_input(input_arg):
    try:
        if isinstance(input_arg, list):
            negatives = 0
            sum_after_second_negative = 0
            even_numbers = []

            for num in input_arg:
                if num < 0:
                    negatives += 1
                    if negatives >= 2:
                        sum_after_second_negative += num
                elif num % 2 == 0:
                    even_numbers.append(num)

            print(f"Сумма после второго отрицательного элемента: {sum_after_second_negative}")
            print("Все четные числа:", even_numbers)

        elif isinstance(input_arg, set):
            if input_arg:
                max_element = max(input_arg)
                min_element = min(input_arg)
                print(f"Максимальный элемент: {max_element}")
                print(f"Минимальный элемент: {min_element}")
            else:
                print("Множество пусто")

        elif isinstance(input_arg, int):
            if input_arg >= 2:
                prime_numbers = []

                for num in range(2, input_arg + 1):
                    is_prime = True
                    for i in range(2, int(num ** 0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        prime_numbers.append(num)

                print("Простые числа до", input_arg, ":", prime_numbers)
            else:
                print("Введите число больше или равное 2")

        elif isinstance(input_arg, str):
            digits = [char for char in input_arg if char.isdigit()]
            print("Цифры в строке:", digits)

        else:
            print("Неизвестный тип аргумента")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        print("Завершение выполнения функции")

try:
    user_input = input("Введите данные (список, множество, число или строку): ")
    if user_input.startswith("[") and user_input.endswith("]"):
        input_arg = eval(user_input)
    else:
        input_arg = user_input

    process_input(input_arg)
except Exception as e:
    print(f"Ошибка: {e}")
