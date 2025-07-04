from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    """
    Обчислює кількість днів від заданої дати до поточної дати.

    :param date_str: Дата у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
    :return: Ціле число днів. Від'ємне, якщо задана дата пізніша за сьогодні.
    :raises ValueError: Якщо формат дати неправильний.
    """
    try:
        # Перетворюємо рядок у дату без часу
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Невірний формат дати: '{date_str}'. Очікується 'РРРР-ММ-ДД'.")

    # Отримуємо поточну дату без часу
    today = datetime.today().date()

    # Рахуємо різницю в днях
    delta = today - input_date

    return delta.days


if __name__ == "__main__":
    date_input = input("Введіть дату у форматі РРРР-ММ-ДД: ")
    try:
        days = get_days_from_today(date_input)
        print(f"Кількість днів від {date_input} до сьогодні: {days}")
    except ValueError as e:
        print(e)
