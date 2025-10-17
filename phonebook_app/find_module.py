from colorama import Fore, Style

def find_contact(data_basa):
    """
    Searches for contacts in the phonebook database.

    The function:
        - Prompts the user to enter a search query (name, last name, phone number, or city).
        - Performs a case-insensitive search.
        - Matches partial entries (e.g., "ann" matches "Anna").
        - Displays all matching results, including additional phone numbers.
        - Allows the user to perform multiple searches.

    Args:
        data_basa (dict): The current phonebook data loaded from JSON.

    Returns:
        None
    """

    while True:
        # отримуємо запит користувача
        search_request = input(Fore.CYAN + "Enter name, last name, phone number, or city to search: ").strip()

        # перевірка, що поле не порожнє
        if not search_request:
            print(Fore.RED + "Search field is empty. Please enter something to search.")
            continue

        # визначаємо тип запиту
        search_request_lower = search_request.lower()
        is_number = search_request.isdigit()  # якщо це цифри
        is_letters = all(ch.isalpha() or ch.isspace() for ch in search_request_lower)

        # перевірка коректності введення
        if not (is_number or is_letters):
            print(Fore.RED + "Invalid characters entered. Please use only letters or digits.")
            continue

        # список результатів пошуку
        results = []

        for contact in data_basa["contacts"]:
            # пошук за номером телефону
            if is_number:
                if search_request in contact["phone_number"]:
                    results.append(contact)
                elif "additional_phones" in contact and any(
                    search_request in phone for phone in contact["additional_phones"]
                ):
                    results.append(contact)

            # пошук за ім'ям, прізвищем або містом (частковий збіг)
            elif is_letters:
                if (
                    search_request_lower in contact["first_name"].lower()
                    or search_request_lower in contact["last_name"].lower()
                    or search_request_lower in f"{contact['first_name'].lower()} {contact['last_name'].lower()}"
                    or search_request_lower in contact["city"].lower()
                ):
                    results.append(contact)

        # виведення результатів
        if results:
            print(Fore.GREEN + Style.BRIGHT + f"\n✅ Found {len(results)} contact(s):")
            for contact in results:
                print(
                    Fore.MAGENTA + f"{contact['first_name'].title()} {contact['last_name'].title()}"
                    + Fore.WHITE + f" | Phone: {contact['phone_number']} | City: {contact['city'].title()}"
                )
                if "additional_phones" in contact:
                    print(Fore.CYAN + f"   Additional phones: {', '.join(contact['additional_phones'])}")
        else:
            print(Fore.RED + "No contacts matching your search were found.")

        # запит чи продовжити пошук
        again = input(Fore.YELLOW + "\nWould you like to search for another contact? (y/n): ").strip().lower()
        if again != "y":
            print(Fore.CYAN + "Returning to the main menu...")
            break
