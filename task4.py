import sys

contacts = {}

def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    arguments = parts[1:]
    return command, arguments

def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."
    
def remove_contact(name):
    if name in contacts:
        del contacts[name]
        return "Contact removed."
    else:
        return "Error: Contact not found."

def show_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ")
        command, arguments = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        
        elif command == "add" and len(arguments) == 2:
            name, phone = arguments
            print(add_contact(name, phone))
        
        elif command == "change" and len(arguments) == 2:
            name, phone = arguments
            print(change_contact(name, phone))

        elif command == "remove" and len(arguments) == 1:
            name = arguments[0]
            print(remove_contact(name))
        
        elif command == "phone" and len(arguments) == 1:
            name = arguments[0]
            print(show_phone(name))
        
        elif command == "all":
            print(show_all())
        
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
