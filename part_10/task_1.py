from datetime import datetime, timedelta
from collections import UserDict

# --- Класи Field, Name, Phone, Birthday ---

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) < 10:
            raise ValueError("Invalid phone number. It must be at least 10 digits.")
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
        for idx, p in enumerate(self.phones):
            if p.value == old:
                self.phones[idx] = Phone(new)
                return True
        raise ValueError("Phone number not found.")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.today().date()
        bday = self.birthday.value.replace(year=today.year)
        if bday < today:
            bday = bday.replace(year=today.year + 1)
        return (bday - today).days

# --- Клас AddressBook ---

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        birthdays = []

        for record in self.data.values():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year)
                if today <= bday_this_year <= next_week:
                    birthdays.append({
                        "name": record.name.value,
                        "congrats_date": bday_this_year.strftime("%d.%m.%Y")
                    })

        return birthdays

# --- Приклад використання ---

if __name__ == "__main__":
    book = AddressBook()

    # Контакт 1
    r1 = Record("Alice")
    r1.add_phone("0501234567")
    r1.add_birthday("08.07.1990")
    book.add_record(r1)

    # Контакт 2
    r2 = Record("Bob")
    r2.add_phone("0677654321")
    r2.add_birthday("10.07.1995")
    book.add_record(r2)

    # Контакт 3 без дня народження
    r3 = Record("Charlie")
    r3.add_phone("0931112233")
    book.add_record(r3)

    # Виведення привітань на тиждень
    print("\nUpcoming birthdays in the next 7 days:")
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        for entry in upcoming:
            print(f"{entry['name']} - {entry['congrats_date']}")
    else:
        print("No upcoming birthdays.")
