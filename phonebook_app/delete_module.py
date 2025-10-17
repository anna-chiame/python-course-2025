from colorama import Fore, Style

def delete_contact(data_basa):
    """
    Deletes a contact from the phonebook database.

    The function:
        - Prompts the user to enter a name, last name, or phone number to find the contact.
        - Searches for exact matches (case-insensitive).
        - If multiple contacts are found, asks the user to choose which one to delete.
        - Asks for confirmation before deletion.
        - Removes the selected contact from memory (does not save to file directly).

    Args:
        data_basa (dict): The current phonebook data loaded from JSON.

    Returns:
        None
    """

    # дані для пошуку контакту
    search_request = input(Fore.CYAN + "Enter the first name, last name, or phone number of the contact to delete: ").strip().lower()

    # шукаємо контакти, які відповідають запиту
    found_contacts = []
    for contact in data_basa["contacts"]:
        if (
            search_request == contact["first_name"].lower()
            or search_request == contact["last_name"].lower()
            or search_request == contact["phone_number"]
            or ("additional_phones" in contact and search_request in contact["additional_phones"])
        ):
            found_contacts.append(contact)

    # якщо нічого не знайдено
    if not found_contacts:
        print(Fore.RED + "No contacts matching your search were found.")
        return

    # якщо знайдено кілька контактів
    if len(found_contacts) > 1:
        print(Fore.YELLOW + "Multiple contacts found:")
        for i, contact in enumerate(found_contacts, start=1):
            print(
                Fore.MAGENTA + f"{i}. {contact['first_name'].title()} {contact['last_name'].title()}"
                + Fore.WHITE + f" | Phone: {contact['phone_number']} | City: {contact['city'].title()}"
            )
        while True:
            choice = input(Fore.CYAN + "Enter the number of the contact you want to delete: ").strip()
            if not choice.isdigit():
                print(Fore.RED + "Please enter a valid number from the list.")
                continue
            choice_num = int(choice)
            if 1 <= choice_num <= len(found_contacts):
                contact_to_delete = found_contacts[choice_num - 1]
                break
            else:
                print(Fore.YELLOW + f"Please enter a number between 1 and {len(found_contacts)}.")
    else:
        contact_to_delete = found_contacts[0]

    # запит на підтвердження видалення
    confirm = input(
        Fore.YELLOW + f"Are you sure you want to delete "
        + Fore.MAGENTA + f"{contact_to_delete['first_name'].title()} {contact_to_delete['last_name'].title()}"
        + Fore.YELLOW + "? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print(Fore.CYAN + "Deletion cancelled.")
        return

    # видаляємо контакт зі списку у пам'яті
    data_basa["contacts"].remove(contact_to_delete)
    print(
        Fore.GREEN + Style.BRIGHT +
        f" Contact {contact_to_delete['first_name'].title()} {contact_to_delete['last_name'].title()} has been successfully deleted."
    )
