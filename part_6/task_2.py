def get_cats_info(path):
    """
    Зчитує інформацію про котів із файлу і повертає список словників з ключами 'id', 'name', 'age'.

    :param path: Шлях до текстового файлу з даними про котів.
    :return: Список словників, кожен з яких містить інформацію про одного кота.
    """
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                parts = line.split(',')
                if len(parts) != 3:
                    continue  # ігноруємо рядки з неправильним форматом

                cat_id, name, age = parts
                cat_dict = {
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                }
                cats.append(cat_dict)

        return cats

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
        return []



if __name__ == "__main__":
    path = input("Введіть шлях до файлу з інформацією про котів: ").strip()
    cats = get_cats_info(path)
    if cats:
        print("Інформація про котів:")
        for cat in cats:
            print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")
    else:
        print("Немає даних або файл не знайдено.")
