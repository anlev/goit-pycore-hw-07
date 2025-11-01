from address_book import AddressBook
from handlers import (
    add_contact,
    show_phone,
    edit_phone,
    remove_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays, edit_phone, remove_phone,
)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        command, *args = input("Enter a command: ").split()
        command = command.strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "show-phone":
            print(show_phone(args, book))

        elif command == "edit-phone":
            print(edit_phone(args, book))

        elif command == "remove-phone":
            print(remove_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()