import re

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону до формату з кодом країни +38,
    залишаючи лише цифри та символ '+' на початку.

    :param phone_number: Рядок з номером телефону у довільному форматі.
    :return: Нормалізований номер телефону у форматі +380XXXXXXXXX.
    """
    # Видаляємо всі символи, крім цифр та '+'
    phone = re.sub(r'[^\d+]', '', phone_number.strip())

    # Якщо номер починається з '+', залишаємо плюс і цифри після нього
    if phone.startswith('+'):
        # Прибираємо всі плюси, крім першого
        phone = '+' + phone[1:].replace('+', '')
    else:
        # Якщо номер починається з 380 (без +), додаємо +
        if phone.startswith('380'):
            phone = '+' + phone
        else:
            # Якщо немає коду країни, додаємо +38 спереду
            phone = '+38' + phone

    return phone


if __name__ == "__main__":
    phone_input = input("Введіть номер телефону у довільному форматі: ")
    normalized = normalize_phone(phone_input)
    print(f"Нормалізований номер: {normalized}")
