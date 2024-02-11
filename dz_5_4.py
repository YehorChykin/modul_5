import os

contacts_file_path = r"D:\Projects\start_python\modul_5\contacts.txt"

print("Hi, can I help you?")

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Invalid input. Please provide correct data."
        except IndexError:
            return "Invalid input format. Please try again."

    return inner

@input_error
def add_contact(name, phone_number):
    try:
        with open(contacts_file_path, 'a') as file:
            file.write(f"{name},{phone_number}\n")
        print("Contact added.")
        return "Contact added."
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

@input_error
def change_contact(name, new_phone_number):
    try:
        with open(contacts_file_path, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            contact_name, _ = line.strip().split(',')
            if contact_name == name:
                lines[i] = f"{name},{new_phone_number}\n"
                break
        with open(contacts_file_path, 'w') as file:
            file.writelines(lines)
        print("Contact updated.")
        return "Contact updated."
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

@input_error
def show_phone(name):
    try:
        with open(contacts_file_path, 'r') as file:
            for line in file:
                contact_name, phone_number = line.strip().split(',')
                if contact_name == name:
                    print(f"Name: {name}, Number: {phone_number}")
                    return f"Name: {name}, Number: {phone_number}"
            else:
                print(f"No contact found for {name}")
                return f"No contact found for {name}"
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

@input_error
def show_all():
    try:
        with open(contacts_file_path, 'r') as file:
            contacts = file.readlines()
            for contact in contacts:
                name, phone_number = contact.strip().split(',')
                print(f"Name: {name}, Number: {phone_number}")
            return contacts
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

def parse_input(user_input):
    parts = user_input.lower().split()
    command = parts[0]
    arguments = parts[1:]
    return command, arguments

def main():
    while True:
        user_input = input("Enter a command (hello/close/exit/add/change/show_phone/all): ")
        command, arguments = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif "exit" in command or "close" in command:
            print("Goodbye!")
            break
        elif command == "add":
            name = input("Enter your contact name: ").strip()
            phone_number = input("Enter your contact number: ").strip()
            add_contact(name, phone_number)
        elif command == "change":
            name = input("Enter the contact name: ").strip()
            new_phone_number = input("Enter the new phone number: ").strip()
            change_contact(name, new_phone_number)
        elif command == "show_phone":
            name = input("Enter the contact name: ").strip()
            show_phone(name)
        elif command == "all":
            show_all()
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()