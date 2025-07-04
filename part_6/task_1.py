def total_salary(path):
    """
    Обчислює загальну та середню заробітну плату розробників, прочитану з файлу.

    :param path: Шлях до текстового файлу із зарплатами (формат рядків: "Прізвище,зарплата").
    :return: Кортеж (загальна сума, середня зарплата).
    """
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                # Розділяємо рядок на ім'я та зарплату
                parts = line.split(',')
                if len(parts) != 2:
                    continue  # ігноруємо рядки з неправильним форматом

                salary_str = parts[1].strip()
                try:
                    salary = float(salary_str)
                except ValueError:
                    continue  # ігноруємо рядки з некоректною зарплатою

                total += salary
                count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
        return (0, 0)
