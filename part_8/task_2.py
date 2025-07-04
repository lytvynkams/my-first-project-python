import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, який ітерує по всіх дійсних числах у тексті.
    Числа вважаються відокремленими пробілами з обох боків.
    """
    # Регулярний вираз шукає числа, відокремлені пробілами
    pattern = r'(?<=\s)(\d+\.\d+|\d+)(?=\s)'
    for match in re.finditer(pattern, text):
        yield float(match.group(0))


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Використовує генератор для підсумовування всіх чисел у тексті.
    """
    return sum(func(text))


# Приклад використання
if __name__ == "__main__":
    text = ("Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")
