# додає новий контакт
# перевіряє на дубль при додаванні
# пропонує створити додатковий номер контакту

from colorama import Fore, Style


def add_contact(data_basa):
    """
    Adds a new contact to the phonebook database.

    The function:
        - Prompts the user to enter first name, last name, phone number, and city.
        - Validates the input (letters only for names/city, digits only for phone number).
        - Checks for duplicate contacts:
            * same phone number;
            * same first + last name.
        - If a duplicate name is found, offers to add the new number
          to the existing contact instead of creating a new one.
        - Adds the validated contact to the in-memory database.

    Args:
        data_basa (dict): The current phonebook data loaded from JSON.

    Returns:
        None
    """

    # вводимо ім’я і перевіряємо, щоб були тільки літери
    while True:
        user_first_name = input(Fore.CYAN + "Enter first name: ").strip().capitalize()
        if not user_first_name.isalpha():
            print(Fore.RED + "First name must contain only letters. Please try again.")
            continue
        break

    # вводимо прізвище і перевіряємо, щоб були тільки літери
    while True:
        user_last_name = input(Fore.CYAN + "Enter last name: ").strip().capitalize()
        if not user_last_name.isalpha():
            print(Fore.RED + "Last name must contain only letters. Please try again.")
            continue
        break

    # вводимо номер телефону і перевіряємо валідність
    while True:
        user_phone = input(Fore.CYAN + "Enter phone number (10 digits): ").strip()
        if not user_phone.isdigit():
            print(Fore.RED + "Phone number must contain digits only. Please try again.")
            continue
        if len(user_phone) != 10:
            print(Fore.RED + "Phone number must be exactly 10 digits long.")
            continue
        break

    # перевіряємо на дублювання
    for contact in data_basa["contacts"]:
        # дубль по номеру
        if contact["phone_number"] == user_phone:
            print(Fore.RED + f"The phone number {user_phone} already exists in the database.")
            return

        # дубль по ім'ю + прізвищу
        if (contact["first_name"] == user_first_name and
                contact["last_name"] == user_last_name):
            print(Fore.YELLOW + f"The contact '{user_first_name} {user_last_name}' already exists.")
            while True:
                choice = input(Fore.YELLOW + "Would you like to add this number to the existing contact? (y/n): ").strip().lower()
                if choice == "y":
                    if "additional_phones" not in contact:
                        contact["additional_phones"] = []
                    contact["additional_phones"].append(user_phone)
                    print(Fore.GREEN + f"Phone number {user_phone} has been added to {user_first_name} {user_last_name}.")
                    return
                elif choice == "n":
                    print(Fore.CYAN + "Creating a new contact...")
                    break
                else:
                    print(Fore.RED + "Please enter 'y' or 'n'.")
            break  # вихід із циклу після перевірки дубля

    # вводимо місто
    while True:
        user_city = input(Fore.CYAN + "Enter city: ").strip().capitalize()
        if not user_city.isalpha():
            print(Fore.RED + "City name must contain only letters. Please try again.")
            continue
        break

    # створюємо новий словник контакту
    contact = {
        "first_name": user_first_name,
        "last_name": user_last_name,
        "phone_number": user_phone,
        "city": user_city
    }

    # додаємо контакт до списку
    data_basa["contacts"].append(contact)

    # повідомляємо користувача
    print(Fore.GREEN + Style.BRIGHT + f" Contact {user_first_name} {user_last_name} was successfully added!")
