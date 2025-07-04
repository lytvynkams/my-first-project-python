import pickle
from datetime import datetime, timedelta

# --- Класи поля та записів ---
class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

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

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.today().date()
        next_birthday = self.birthday.value.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones)
        bday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "N/A"
        return f"{self.name.value}: {phones}. Birthday: {bday}"

class AddressBook(dict):
    def add_record(self, record):
        self[record.name.value] = record

    def find(self, name):
        return self.get(name)

    def get_upcoming_birthdays(self):
        result = []
        today = datetime.today().date()
        end = today + timedelta(days=7)

        for rec in self.values():
            if rec.birthday:
                bday = rec.birthday.value.replace(year=today.year)
                if today <= bday <= end:
                    result.append(f"{rec.name.value}: {bday.strftime('%d.%m')}")
        return result

# --- Декоратор обробки помилок ---
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Not enough arguments."
    return wrapper

# --- Команди ---
@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        msg = "Contact added."
    else:
        msg = "Contact updated."
    record.add_phone(phone)
    return msg

@input_error
def change_contact(args, book):
    name, old, new = args
    record = book.find(name)
    record.change_phone(old, new)
    return "Phone changed."

@input_error
def get_phone(args, book):
    name = args[0]
    record = book.find(name)
    return ", ".join(p.value for p in record.phones)

@input_error
def show_all(args, book):
    if not book:
        return "No contacts."
    return "\n".join(str(record) for record in book.values())

@input_error
def add_birthday(args, book):
    name, date = args
    record = book.find(name)
    record.add_birthday(date)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record.birthday:
        return record.birthday.value.strftime("%d.%m.%Y")
    return "Birthday not set."

@input_error
def birthdays(args, book):
    items = book.get_upcoming_birthdays()
    if not items:
        return "No upcoming birthdays."
    return "\n".join(items)

# --- Серіалізація ---
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

# --- Парсер команд ---
def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    return command, parts[1:]

# --- Основна функція ---
def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            save_data(book)
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

if __name__ == "__main__":
    main()
