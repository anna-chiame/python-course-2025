from colorama import Fore, Style

def list_contacts(data_basa):
    """
    Displays all contacts stored in the phonebook database.

    The function:
        - Retrieves all contacts from the in-memory data dictionary.
        - Displays them in a formatted, color-coded list.
        - Shows main and additional phone numbers.
        - Handles the case when the contact list is empty.

    Args:
        data_basa (dict): The current phonebook data loaded from JSON.

    Returns:
        None
    """

    contacts = data_basa.get("contacts", [])

    # перевірка на порожню базу
    if not contacts:
        print(Fore.RED + "The contact list is empty.")
        return

    print(Fore.YELLOW + Style.BRIGHT + "\n=== CONTACT LIST ===\n")

    for index, contact in enumerate(contacts, start=1):
        first_name = contact.get("first_name", "").title()
        last_name = contact.get("last_name", "").title()
        phone = contact.get("phone_number", "")
        city = contact.get("city", "").title()

        # основна інформація про контакт
        print(
            Fore.CYAN + f"{index}. "
            + Fore.MAGENTA + f"{first_name} {last_name}"
            + Fore.WHITE + " | "
            + Fore.GREEN + f"Phone: {phone}"
            + Fore.WHITE + " | "
            + Fore.BLUE + f"City: {city}"
        )

        # додаткові телефони
        additional_phones = contact.get("additional_phones", [])
        if additional_phones:
            print(Fore.CYAN + "   Additional phones: " + Fore.GREEN + ", ".join(additional_phones))

        # роздільник між контактами
        print(Fore.WHITE + "-" * 60)

    print(Fore.YELLOW + Style.BRIGHT + "\nEnd of contact list.\n")
