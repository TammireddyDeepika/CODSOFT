import json
import os

CONTACT_FILE = "contacts.json"


# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return {}


# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# Add new contact
def add_contact(contacts):
    name = input("\nEnter Name        : ")
    phone = input("Enter Phone Number : ")
    email = input("Enter Email        : ")
    address = input("Enter Address      : ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    save_contacts(contacts)
    print("\n✔ Contact added successfully!\n")


# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n------ CONTACT LIST ------")
    for name, info in contacts.items():
        print(f"{name}  -  {info['phone']}")
    print("---------------------------\n")


# Search contact
def search_contact(contacts):
    keyword = input("\nSearch by name/phone: ")

    found = False
    for name, info in contacts.items():
        if keyword.lower() in name.lower() or keyword in info["phone"]:
            print("\n--- Contact Found ---")
            print(f"Name   : {name}")
            print(f"Phone  : {info['phone']}")
            print(f"Email  : {info['email']}")
            print(f"Address: {info['address']}\n")
            found = True
            break

    if not found:
        print("\nContact not found.\n")


# Update contact
def update_contact(contacts):
    name = input("\nEnter contact name to update: ")

    if name not in contacts:
        print("\nContact does not exist.\n")
        return

    print("\nLeave blank to keep old value.")

    phone = input(f"New Phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
    email = input(f"New Email ({contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"New Address ({contacts[name]['address']}): ") or contacts[name]['address']

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    save_contacts(contacts)
    print("\n✔ Contact updated successfully!\n")


# Delete contact
def delete_contact(contacts):
    name = input("\nEnter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("\n✔ Contact deleted successfully!\n")
    else:
        print("\nContact not found.\n")


# -----------------------------
#  Main Program Loop
# -----------------------------
def main():
    contacts = load_contacts()

    while True:
        print("\n====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==========================")

        choice = input("Enter option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("\nThank you for using Contact Book! ✨\n")
            break
        else:
            print("\nInvalid option! Try again.\n")


if __name__ == "__main__":
    main()
