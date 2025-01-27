print("Welcome to the Contact Management System!")

# Initialize an empty contact list
contacts = []

while True:
    print("\n=== Contact Management Menu ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Add Contact
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully!")

    elif choice == "2":  # View Contacts
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == "3":  # Search Contact
        search_query = input("Enter name or phone number to search: ")
        found = False
        for contact in contacts:
            if search_query in contact['name'] or search_query in contact['phone']:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                found = True
        if not found:
            print("No contact found.")

    elif choice == "4":  # Update Contact
        update_query = input("Enter the name of the contact to update: ")
        for contact in contacts:
            if contact['name'] == update_query:
                print("Leave fields blank to keep current values.")
                contact['name'] = input(f"New name ({contact['name']}): ") or contact['name']
                contact['phone'] = input(f"New phone ({contact['phone']}): ") or contact['phone']
                contact['email'] = input(f"New email ({contact['email']}): ") or contact['email']
                contact['address'] = input(f"New address ({contact['address']}): ") or contact['address']
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == "5":  # Delete Contact
        delete_query = input("Enter the name of the contact to delete: ")
        for contact in contacts:
            if contact['name'] == delete_query:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == "6":  # Exit
        print("Thank you for using the Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")