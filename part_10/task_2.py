from datetime import datetime, timedelta
from collections import UserDict


# --- Класи для полів ---
class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must be 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# --- Клас Record ---
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old, new):
        for i, p in enumerate(self.phones):
            if p.value == old:
                self.phones[i] = Phone(new)
                return
        raise ValueError("Old phone not found.")

    def add_birthday(self, bday):
        self.birthday = Birthday(bday)

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones)
        bday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "No birthday"
        return f"{self.name.value}: {phones}; Birthday: {bday}"


# --- Клас AddressBook ---
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end = today + timedelta(days=7)
        result = []

        for record in self.data.values():
            if record.birthday:
                bday = record.birthday.value.replace(year=today.year)
                if today <= bday <= end:
                    result.append(f"{record.name.value}: {bday.strftime('%d.%m.%Y')}")

        return result


# --- Декоратор для обробки помилок ---
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Not enough arguments. Please check your input."
    return wrapper


# --- Командні функції ---
@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError
    record.change_phone(old_phone, new_phone)
    return "Phone number updated."


@input_error
def get_phone(args, book):
    name, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError
    phones = ", ".join(p.value for p in record.phones)
    return f"{name}: {phones}"


@input_error
def show_all(args, book):
    if not book.data:
        return "No contacts yet."
    return "\n".join(str(r) for r in book.data.values())


@input_error
def add_birthday(args, book):
    name, bday, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError
    record.add_birthday(bday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if not record or not record.birthday:
        return "Birthday not found."
    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args, book):
    results = book.get_upcoming_birthdays()
    if not results:
        return "No upcoming birthdays."
    return "\n".join(results)


# --- Парсер вводу ---
def parse_input(user_input):
    parts = user_input.strip().split()
    return parts[0].lower(), parts[1:]


# --- Основна функція ---
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(get_phone(args, book))
        elif command == "all":
            print(show_all(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")


# --- Запуск ---
if __name__ == "__main__":
    main()
