import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    """
    Генерує унікальний відсортований список випадкових чисел для лотерейного квитка.

    :param min_num: Мінімальне можливе число у наборі (не менше 1).
    :param max_num: Максимальне можливе число у наборі (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати (між min_num і max_num).
    :return: Відсортований список унікальних випадкових чисел.
             Порожній список, якщо параметри некоректні.
    """
    # Перевірка вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000):
        return []
    if not (min_num <= quantity <= (max_num - min_num + 1)):
        return []

    # Генеруємо унікальні випадкові числа за допомогою random.sample
    numbers = random.sample(range(min_num, max_num + 1), quantity)

    # Сортуємо та повертаємо список
    return sorted(numbers)

if __name__ == "__main__":
    result = get_numbers_ticket(1, 49, 6)
    print(f"Ваш лотерейний квиток: {result}")
