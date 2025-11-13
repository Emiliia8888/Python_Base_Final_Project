from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

import src.command_processing.command_processor as command_processor
from src.command_processing import notes_processor
from src.command_processing.command_parser import parse_input_data
from src.enums.command_enums import CommandEnum
from src.save_load_data.save_load_data import load_all_data, save_all_data

def main():
    user_name = input("Enter your name >>> ")
    print(f"Welcome {user_name} to the assistant bot!")
    book, notes = load_all_data()

    # autocomplete for commands (Task 12)
    base_commands = [
        CommandEnum.HELLO.value,
        CommandEnum.ADD.value,
        CommandEnum.CHANGE.value,
        CommandEnum.SHOW_PHONE.value,
        CommandEnum.ADD_EMAIL.value,
        CommandEnum.SHOW_EMAIL.value,
        CommandEnum.SHOW_ALL.value,
        CommandEnum.ADD_BIRTHDAY.value,
        CommandEnum.SHOW_BIRTHDAY.value,
        CommandEnum.BIRTHDAYS.value,
        CommandEnum.ADD_NOTE.value,
        CommandEnum.DELETE_NOTE.value,
        CommandEnum.LIST_NOTES.value,
        CommandEnum.REMOVE_CONTACT.value,
        CommandEnum.FIND_CONTACT_BY_NAME.value,
        CommandEnum.FIND_CONTACT_BY_EMAIL.value,
        CommandEnum.ADD_ADDRESS.value,
        CommandEnum.REMOVE_ADDRESS.value,
    ]

    exit_commands = list(CommandEnum.EXIT_COMMANDS.value)
    all_commands = base_commands + exit_commands

    command_completer = WordCompleter(all_commands, ignore_case=True)


    while True:
        try:
            user_data = prompt("Enter the command >>> ", completer=command_completer)
            command, *args = parse_input_data(user_data) 
            
            if command in CommandEnum.EXIT_COMMANDS.value:
                save_all_data(book, notes)
                print(f"Good bye {user_name}!")
                break

            match command:
                case CommandEnum.HELLO.value:
                    print(f"How can I help you, {user_name}?")
                case CommandEnum.ADD.value:
                    print(command_processor.add_contact(args, book))
                case CommandEnum.CHANGE.value:
                    print(command_processor.update_contact(args, book))
                case CommandEnum.SHOW_PHONE.value:
                    print(command_processor.show_phones(args, book))
                case CommandEnum.ADD_EMAIL.value:
                    print(command_processor.add_email(args, book))
                case CommandEnum.SHOW_EMAIL.value:
                    print(command_processor.show_emails(args, book))
                case CommandEnum.SHOW_ALL.value:
                    print(command_processor.show_all(book))
                case CommandEnum.ADD_BIRTHDAY.value:
                    print(command_processor.add_birthday(args, book))
                case CommandEnum.SHOW_BIRTHDAY.value:
                    print(command_processor.show_birthday(args, book))
                case CommandEnum.BIRTHDAYS.value:
                    print(command_processor.birthdays(book))
                case CommandEnum.ADD_NOTE.value:
                    print(notes_processor.add_note(args, notes))
                #case CommandEnum.EDIT_NOTE.value:
                    #print(notes_processor.edit_note(args, notes))
                case CommandEnum.DELETE_NOTE.value:
                    print(notes_processor.delete_note(args, notes))
                case CommandEnum.LIST_NOTES.value:
                    print(notes_processor.list_notes(notes))
                case CommandEnum.REMOVE_CONTACT.value:
                    print(command_processor.remove_contact(args, book))
                case CommandEnum.FIND_CONTACT_BY_NAME.value:
                    print(command_processor.find_contact_by_name(args, book))
                case CommandEnum.FIND_CONTACT_BY_EMAIL.value:
                    print(command_processor.find_contact_by_email(args, book))
                case CommandEnum.ADD_ADDRESS.value:
                    print(command_processor.add_address(args, book))
                case CommandEnum.REMOVE_ADDRESS.value:
                    print(command_processor.remove_address(args, book))
                case _:
                    print("Invalid command.")
                    input_command = input("Would you like to see all commands list? Y/N >>> ").strip().lower()
                    if(input_command == 'y'):
                        print(command_processor.show_help_file())
        except Exception as error:
            print("Error happened: ", error)

if __name__ == "__main__":
    main()