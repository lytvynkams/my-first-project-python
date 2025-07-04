def parse_input(user_input):
    """
    Розбирає вхідний рядок на команду та аргументи.
    Повертає команду у нижньому регістрі та список аргументів.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    """
    Додає новий контакт у словник contacts.
    Параметри:
      args - список аргументів, очікуються [ім'я, номер]
      contacts - словник контактів
    Повертає рядок з повідомленням про результат.
    """
    if len(args) < 2:
        return "Error: Please provide both name and phone number."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.
    Параметри:
      args - список аргументів, очікуються [ім'я, новий номер]
      contacts - словник контактів
    Повертає рядок з повідомленням про результат.
    """
    if len(args) < 2:
        return "Error: Please provide both name and new phone number."
    name, new_phone = args[0], args[1]
    if name not in contacts:
        return "Error: Contact not found."
    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args, contacts):
    """
    Показує номер телефону для заданого контакту.
    Параметри:
      args - список аргументів, очікується [ім'я]
      contacts - словник контактів
    Повертає рядок з номером або повідомленням про помилку.
    """
    if len(args) < 1:
        return "Error: Please provide a name."
    name = args[0]
    if name not in contacts:
        return "Error: Contact not found."
    return contacts[name]


def show_all(contacts):
    """
    Показує всі контакти з номерами.
    Параметри:
      contacts - словник контактів
    Повертає рядок зі списком контактів або повідомлення, що список пустий.
    """
    if not contacts:
        return "No contacts found."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
