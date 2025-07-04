import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(path: Path, prefix=""):
    """
    Рекурсивно виводить структуру директорії із кольоровим форматуванням.

    :param path: Path до директорії або файлу
    :param prefix: рядок відступу для візуалізації структури
    """
    if path.is_dir():
        # Колір для директорій
        print(f"{prefix}{Fore.BLUE}{path.name}{Style.RESET_ALL}/")
        entries = sorted(path.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
        for i, entry in enumerate(entries):
            # Формуємо відступи з ┣ або ┗ для гарного вигляду
            connector = "┗" if i == len(entries) - 1 else "┣"
            # Відступ для вкладених елементів (пропорційний глибині)
            new_prefix = prefix + "┃   " if i != len(entries) - 1 else prefix + "    "
            # Виводимо з кольором залежно від типу
            if entry.is_dir():
                print(f"{prefix}{connector} {Fore.BLUE}{entry.name}{Style.RESET_ALL}/")
                print_directory_structure(entry, new_prefix)
            else:
                print(f"{prefix}{connector} {Fore.GREEN}{entry.name}{Style.RESET_ALL}")
    else:
        # Якщо це файл, просто виводимо
        print(f"{prefix}{Fore.GREEN}{path.name}{Style.RESET_ALL}")

def main():
    init(autoreset=True)  # Ініціалізуємо colorama

    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"Помилка: шлях '{dir_path}' не існує.")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"Помилка: шлях '{dir_path}' не є директорією.")
        sys.exit(1)

    print(f"Структура директорії: {dir_path}")
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()
