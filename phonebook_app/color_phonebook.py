"""
PHONEBOOK APPLICATION
=====================
Main control file that connects all modules together.

Functionality:
    - Displays a colorful animated welcome screen.
    - Loads or creates a JSON database.
    - Runs an interactive menu for user actions.
    - Calls modules for Add, Find, Delete, Update, List.
    - Displays a animated  goodbye screen on exit.
"""

import sys
from colorama import Fore, Style, init
from time import sleep
import random

# імпорт власних модулів
from storage_module import ensure_database, load_data_basa, save_data_basa
from user_input import get_user_action
from add_module import add_contact
from find_module import find_contact
from delete_module import delete_contact
from edit_module import edit_contact
from list_module import list_contacts

# ініціалізація кольорової бібліотеки
init(autoreset=True)

#  Допоміжні функції оформлення
def print_separator():
    """Prints a colored line separator for visual clarity."""
    print(Fore.BLUE + Style.BRIGHT + "─" * 60)

def animated_print(text: str, delay: float = 0.03, color: str = Fore.WHITE):
    """
    Prints text gradually (typewriter effect 🖋️).

    Args:
        text (str): Text to display.
        delay (float): Time delay between characters.
        color (str): Text color (Fore.CYAN, Fore.YELLOW, etc.)
    """
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        sleep(delay)
    print()

# Екран привітання
def print_welcome():
    """
    Displays a cheerful welcome screen at program start.
    Uses colors, emojis, and animation to greet the user.
    """

    print_separator()
    animated_print("💖  WELCOME TO YOUR AMAZING PHONEBOOK  💖", color=Fore.MAGENTA, delay=0.04)
    sleep(0.5)
    animated_print("✨ Organize your chaos ✨", color=Fore.CYAN, delay=0.03)
    sleep(0.5)

    print(Fore.YELLOW + "=" * 60)
    sleep(0.3)

    animated_print("📞  1) Add   🔍  2) Find   ❌  3) Delete", color=Fore.GREEN, delay=0.02)
    sleep(0.3)
    animated_print("✏️   4) Update   📋  5) List   🚪  6) Exit", color=Fore.MAGENTA, delay=0.02)
    sleep(0.3)

    print(Fore.YELLOW + "=" * 60)

# Прощання
def print_goodbye():
    """
    Displays a colorful and animated goodbye message on exit.
    Confirms data saving, leaves a friendly farewell,
    and shows a random inspirational quote in English.

    The quote is chosen randomly from a predefined list.
    """

    # список крилатих фраз англійською
    quotes = [
        "Keep smiling — it confuses people. 😄",
        "Dream big, work hard, stay humble. 💪",
        "☕Code, coffee, repeat. 💻",
        "Be the reason someone smiles today. 🌞",
        "Every ending is a new beginning. 🌱",
        "Stay curious and keep learning! 🧠",
        "Make today so awesome that yesterday gets jealous. 😎",
        "Life is short — call your friends often. 📞",
        "You did great today. Now go rest. 🌙",
        "Believe in yourself — you’re the magic. ✨"
    ]

    # вибір однієї випадкової цитати
    random_quote = random.choice(quotes)

    # основний текст завершення
    print_separator()
    animated_print("💾 Saving your changes...", color=Fore.YELLOW, delay=0.04)
    sleep(0.7)
    animated_print("✅ All contacts saved successfully!", color=Fore.GREEN, delay=0.04)
    sleep(0.6)

    # виводимо випадкову цитату на фінальне прощання
    print_separator()
    print(Fore.CYAN + Style.BRIGHT + f"💡 Quote of the day: {random_quote}")
    print_separator()

#  Основна логіка програми

DEFAULT_DATABASE_NAME = 'contacts.json'  # стандартна база даних

def main():
    """
    Main control loop of the phonebook program.

    Steps:
        1. Checks if the database exists (creates one if missing)
        2. Loads all data into memory
        3. Displays a colorful welcome screen
        4. Runs an infinite loop with user menu actions
        5. On exit, saves updated data and displays a goodbye screen
    """

    # визначення імені бази (через аргумент або стандарт)
    if len(sys.argv) > 1:
        data_basa_name = sys.argv[1]
    else:
        data_basa_name = DEFAULT_DATABASE_NAME

    ensure_database(data_basa_name)
    data_basa = load_data_basa(data_basa_name)

    # вітальний екран
    print_welcome()

    # головний цикл
    while True:
        print_separator()
        choice = get_user_action()
        print_separator()

        if choice == "1":
            print(Fore.CYAN + "📥 ADD NEW CONTACT")
            add_contact(data_basa)

        elif choice == "2":
            print(Fore.YELLOW + "🔎 SEARCH CONTACTS")
            find_contact(data_basa)

        elif choice == "3":
            print(Fore.RED + "❌ DELETE CONTACT")
            delete_contact(data_basa)

        elif choice == "4":
            print(Fore.MAGENTA + "✏️ UPDATE CONTACT")
            edit_contact(data_basa)

        elif choice == "5":
            print(Fore.GREEN + "📋 LIST OF CONTACTS")
            list_contacts(data_basa)

        elif choice == "6":
            save_data_basa(data_basa, data_basa_name)
            print_goodbye()
            break

        else:
            print(Fore.RED + "Invalid choice, please try again.")


#  Запуск програми
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram interrupted. Goodbye!")
