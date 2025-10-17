"""
PHONEBOOK APPLICATION — MAIN CONTROLLER
Handles:
    - Menu interaction
    - Module coordination
    - Data saving/loading
"""

import sys
from colorama import Fore, Style, init

# ініціалізація кольорів
init(autoreset=True)

# Імпорти модулів
from storage_module import ensure_database, load_data_basa, save_data_basa
from user_input import get_user_action
from add_module import add_contact
from find_module import find_contact
from delete_module import delete_contact
from edit_module import edit_contact
from list_module import list_contacts


DEFAULT_DATABASE_NAME = "contacts.json"


def print_separator():
    """Prints a colored separator line."""
    print(Fore.BLUE + "\n" + "-" * 55 + "\n" + Style.RESET_ALL)


def main():
    """Main control loop of the Phonebook."""
    print_separator()
    print(Fore.CYAN + Style.BRIGHT + "  WELCOME TO THE PHONEBOOK APPLICATION")
    print_separator()

    if len(sys.argv) > 1:
        data_basa_name = sys.argv[1]
    else:
        data_basa_name = DEFAULT_DATABASE_NAME

    ensure_database(data_basa_name)
    data_basa = load_data_basa(data_basa_name)

    while True:
        print_separator()
        choice = get_user_action()
        print_separator()

        if choice == "1":
            print(Fore.CYAN + " ADDING A NEW CONTACT")
            print_separator()
            add_contact(data_basa)

        elif choice == "2":
            print(Fore.YELLOW + " SEARCHING CONTACTS")
            print_separator()
            find_contact(data_basa)

        elif choice == "3":
            print(Fore.RED + " DELETING CONTACT")
            print_separator()
            delete_contact(data_basa)

        elif choice == "4":
            print(Fore.MAGENTA + "  EDITING CONTACT")
            print_separator()
            edit_contact(data_basa)

        elif choice == "5":
            print(Fore.GREEN + " CONTACT LIST")
            print_separator()
            list_contacts(data_basa)

        elif choice == "6":
            print(Fore.YELLOW + " SAVING CHANGES...")
            save_data_basa(data_basa, data_basa_name)
            print_separator()
            print(Fore.CYAN + " THANK YOU FOR USING THE PHONEBOOK. GOODBYE!")
            print_separator()
            break

        else:
            print(Fore.RED + " Invalid choice. Please select from 1 to 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_separator()
        print(Fore.RED + "Program interrupted. Exiting safely...")
        print_separator()
