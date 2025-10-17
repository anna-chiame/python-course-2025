from colorama import Fore, Style

def edit_contact(data_basa):
    """
    Updates an existing contact in the phonebook database.

    The function:
        - Prompts the user to enter a name, last name, or phone number to find a contact.
        - Allows editing of:
            * First name
            * Last name
            * Main phone number (with duplicate check)
            * Additional phone numbers (add/remove)
            * City
        - Validates input for correctness (letters for text fields, digits for numbers).
        - Modifies data in memory without saving directly to file.

    Args:
        data_basa (dict): The current phonebook data loaded from JSON.

    Returns:
        None
    """

    # вибір контакту для редагування
    search_request = input(Fore.CYAN + "Enter the first name, last name, or phone number of the contact to edit: ").strip().lower()

    # пошук контакту
    contact_to_edit = None
    for contact in data_basa["contacts"]:
        full_name = f"{contact['first_name'].lower()} {contact['last_name'].lower()}"
        if (
            search_request == contact["phone_number"]
            or search_request == contact["first_name"].lower()
            or search_request == contact["last_name"].lower()
            or search_request == full_name
        ):
            contact_to_edit = contact
            break

    # якщо не знайдено
    if not contact_to_edit:
        print(Fore.RED + "No contact found matching your search.")
        return

    # меню вибору поля для редагування
    print(Fore.YELLOW + "\nWhat would you like to edit?")
    print(Fore.WHITE + "1. First name")
    print("2. Last name")
    print("3. Main phone number")
    print("4. Additional phone numbers")
    print("5. City")

    choice = input(Fore.CYAN + "Enter the menu number: ").strip()

    # редагування вибраного поля
    if choice == "1":
        new_first_name = input(Fore.CYAN + "Enter new first name: ").strip()
        if new_first_name.isalpha():
            contact_to_edit["first_name"] = new_first_name.capitalize()
            print(Fore.GREEN + "First name successfully updated.")
        else:
            print(Fore.RED + "Invalid input. Only letters are allowed.")

    elif choice == "2":
        new_last_name = input(Fore.CYAN + "Enter new last name: ").strip()
        if new_last_name.isalpha():
            contact_to_edit["last_name"] = new_last_name.capitalize()
            print(Fore.GREEN + "Last name successfully updated.")
        else:
            print(Fore.RED + "Invalid input. Only letters are allowed.")

    elif choice == "3":
        new_phone = input(Fore.CYAN + "Enter new phone number (10 digits): ").strip()
        if new_phone.isdigit() and len(new_phone) == 10:
            duplicate = False
            for contact in data_basa["contacts"]:
                if contact != contact_to_edit:
                    if (
                        contact["phone_number"] == new_phone
                        or ("additional_phones" in contact and new_phone in contact["additional_phones"])
                    ):
                        duplicate = True
                        break
            if not duplicate:
                contact_to_edit["phone_number"] = new_phone
                print(Fore.GREEN + "Main phone number successfully updated.")
            else:
                print(Fore.RED + "This phone number already exists in the database.")
        else:
            print(Fore.RED + "Invalid phone number. It must contain exactly 10 digits.")

    elif choice == "4":
        # редагування додаткових номерів
        if "additional_phones" not in contact_to_edit:
            contact_to_edit["additional_phones"] = []

        print(Fore.CYAN + f"Current additional numbers: {contact_to_edit['additional_phones']}")
        action = input(Fore.YELLOW + "Enter 'add' to add a new number or 'del' to delete one: ").strip().lower()

        if action == "add":
            new_additional = input(Fore.CYAN + "Enter a new additional number (10 digits): ").strip()
            if new_additional.isdigit() and len(new_additional) == 10:
                if new_additional not in contact_to_edit["additional_phones"]:
                    contact_to_edit["additional_phones"].append(new_additional)
                    print(Fore.GREEN + "Additional phone number added.")
                else:
                    print(Fore.YELLOW + "This number is already in the list.")
            else:
                print(Fore.RED + "Invalid number. Must be 10 digits.")
        elif action == "del":
            del_number = input(Fore.CYAN + "Enter the number to delete: ").strip()
            if del_number in contact_to_edit["additional_phones"]:
                contact_to_edit["additional_phones"].remove(del_number)
                print(Fore.GREEN + "Additional phone number removed.")
            else:
                print(Fore.RED + "This number is not in the list of additional numbers.")
        else:
            print(Fore.RED + "Invalid action choice.")

    elif choice == "5":
        new_city = input(Fore.CYAN + "Enter new city name: ").strip()
        if new_city.isalpha():
            contact_to_edit["city"] = new_city.capitalize()
            print(Fore.GREEN + "City successfully updated.")
        else:
            print(Fore.RED + "Invalid city name. Only letters are allowed.")

    else:
        print(Fore.RED + "Invalid menu choice. Please try again.")
