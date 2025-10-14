
import json
# displays all contacts from the database
def list_contact(db_name):
    try:
        # Open the JSON database(db_name)
        with open(db_name, 'r', encoding='utf-8') as file:
            db = json.load(file)
        # If no info in db
        contacts = db.get('contacts', [])
        if not contacts:
            print("List of contacts is empty.")
            return
        # print a numerated list of contacts
        print("List of contacts:")
        for ind_contact, contact in enumerate(contacts, start=1):
            print(f"{ind_contact}. Name: {contact.get('name', '')} | "
                  f"Phone: {contact.get('phone_number', '')} | "
                  f"City: {contact.get('city', '')}")
    # if database is not found
    except FileNotFoundError:
        print(f"File {db_name} is not founded!")
    # if database file is damaged or it's not in json's format
    except json.JSONDecodeError:
        print(f"File {db_name} is damaged or mistake in file's format (not JSON)!")