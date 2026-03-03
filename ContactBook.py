import json
import os

FILE_NAME = "contacts.json"

# -------- Load Contacts --------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# -------- Save Contacts --------
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# -------- Add Contact --------
def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    # Prevent duplicate phone number
    for contact in contacts:
        if contact["phone"] == phone:
            print("⚠ Contact with this phone number already exists!\n")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

# -------- View Contacts --------
def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.\n")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

# -------- Search Contact --------
def search_contact(contacts):
    key = input("\nEnter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if key in contact["name"].lower() or key in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("❌ Contact not found.")
    print()

# -------- Update Contact --------
def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave blank to keep old value")

            new_phone = input("New Phone: ").strip()
            new_email = input("New Email: ").strip()
            new_address = input("New Address: ").strip()

            if new_phone:
                contacts[index]["phone"] = new_phone
            if new_email:
                contacts[index]["email"] = new_email
            if new_address:
                contacts[index]["address"] = new_address

            save_contacts(contacts)
            print("✅ Contact updated successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# -------- Delete Contact --------
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"🗑 {deleted['name']} deleted successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# -------- Main Program --------
def main():
    contacts = load_contacts()

    while True:
        print("====== CONTACT MANAGER ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

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
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()