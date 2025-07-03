from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Повертає список користувачів, у яких день народження в найближчі 7 днів (включно з сьогодні),
    з урахуванням перенесення привітань з вихідних на наступний понеділок.

    :param users: список словників із ключами 'name' та 'birthday' (формат 'рік.місяць.дата')
    :return: список словників із ключами 'name' та 'congratulation_date' (формат 'рік.місяць.дата')
    """
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Парсимо дату народження (тільки місяць і день потрібні для визначення дати в поточному році)
        bday_original = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        # Формуємо дату дня народження у поточному році
        birthday_this_year = bday_original.replace(year=today.year)

        # Якщо день народження вже був цього року раніше за сьогодні - беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо різницю днів між днем народження і сьогодні
        days_diff = (birthday_this_year - today).days

        # Перевіряємо, чи день народження в межах 7 днів включно
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            # Якщо день народження припадає на вихідний (субота=5, неділя=6), переносимо на понеділок
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming
