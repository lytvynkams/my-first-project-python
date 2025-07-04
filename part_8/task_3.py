import sys
from collections import defaultdict
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    """
    Парсить один рядок логу.
    Повертає словник з ключами: date, time, level, message.
    Якщо рядок не відповідає формату, повертає None.
    """
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return None  # Неправильний формат рядка
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message
    }


def load_logs(file_path: str) -> List[dict]:
    """
    Завантажує всі логи з файлу.
    Повертає список словників з інформацією про кожен рядок.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Фільтрує записи логу за рівнем логування.
    """
    level = level.upper()
    return list(filter(lambda log: log['level'] == level, logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Форматує та виводить таблицю з підрахунком записів за рівнем логування.
    """
    print(f"{'Рівень логування':<17} | {'Кількість'}")
    print(f"{'-'*17}-|{'-'*10}")
    for level in sorted(counts.keys()):
        print(f"{level:<17} | {counts[level]}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_логу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Записів рівня '{filter_level.upper()}' не знайдено.")


if __name__ == "__main__":
    main()
