from colorama import Fore, Style, init

# ініціалізація colorama
init(autoreset=True)

# кольорове меню з emoji
AVAILABLE_FUNCTIONAL_MENU = f"""

{Fore.YELLOW + Style.BRIGHT}Available options:
{Fore.GREEN}   1️⃣  Add — add a new contact 📥
{Fore.CYAN}   2️⃣  Find — search for a contact 🔍
{Fore.RED}   3️⃣  Delete — remove a contact ❌
{Fore.MAGENTA}   4️⃣  Update — modify a contact ✏️
{Fore.BLUE}   5️⃣  List — show all contacts 📋
{Fore.YELLOW}   6️⃣  Exit — save and quit 🚪
"""

def get_user_action():
    """
    Displays the colorful functional menu with emojis,
    prompts the user to select an action,
    validates input, and returns the correct choice.

    Returns:
        str: The selected option number as a string ("1"–"6").
    """
    while True:
        print(AVAILABLE_FUNCTIONAL_MENU)
        valid_actions = ["1", "2", "3", "4", "5", "6"]
        user_action = input(Fore.CYAN + "👉 Enter your choice (1–6): ").strip()

        # перевіряємо правильність вводу
        if not user_action.isnumeric() or user_action not in valid_actions:
            print(Fore.RED + "❗ Invalid choice. Please enter a number between 1 and 6.\n")
            continue

        # якщо все добре — повертаємо вибір
        return user_action
