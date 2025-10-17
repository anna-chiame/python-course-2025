import json
import os

# Ім’я бази даних за замовчуванням
DEFAULT_DATABASE_NAME = 'contacts.json'


def ensure_database(database_name=DEFAULT_DATABASE_NAME):
    """
    Checks whether the database file exists.
    If the file is not found, creates a new one with an empty contact list.

    Args:
        database_name (str): Path to the database file.

    Returns:
        None
    """
    if not os.path.exists(database_name):
        print(f"File '{database_name}' not found. Creating a new one...")
        with open(database_name, "w", encoding="utf-8") as file_object:
            # створюємо новий JSON-файл із порожнім списком контактів
            json.dump({"contacts": []}, file_object, ensure_ascii=False, indent=2)
    else:
        print(f"File '{database_name}' found.")


def load_data_basa(database_name=DEFAULT_DATABASE_NAME):
    """
    Loads a JSON file into memory and returns the data as a Python dictionary.

    Args:
        database_name (str): Path to the database file.

    Returns:
        dict: Phonebook data containing the key 'contacts' with a list of contacts.
    """
    with open(database_name, "r", encoding="utf-8") as file_object:
        data_basa = json.load(file_object)
    return data_basa


def save_data_basa(data_basa, database_name=DEFAULT_DATABASE_NAME):
    """
    Writes the updated data back to the JSON file.

    Args:
        data_basa (dict): Dictionary containing contacts.
        database_name (str): Path to the database file.

    Returns:
        None
    """
    with open(database_name, "w", encoding="utf-8") as file_object:
        json.dump(data_basa, file_object, ensure_ascii=False, indent=2)
    print(f"Data saved successfully to file '{database_name}'.")
