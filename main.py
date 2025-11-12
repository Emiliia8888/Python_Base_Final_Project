import src.command_processing.command_processor as command_processor
from src.command_processing.command_parser import parse_input_data
from src.enums.command_enums import CommandEnum
from src.save_load_data.save_load_data import load_data, save_data

def main():
    user_name = input("Enter your name >>> ")
    print(f"Welcome {user_name} to the assistant bot!")
    book = load_data()

    while True:
        try:
            user_data = input("Enter the command >>> ")
            command, *args = parse_input_data(user_data)
            
            if command in CommandEnum.EXIT_COMMANDS.value:
                print(f"Good bye {user_name}!")
                save_data(book)
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
                case _: 
                    print("Invalid command.")
                    input_command = input("Would you like to see all commands list? Y/N >>> ").strip().lower()
                    if(input_command == 'y'):
                        print(command_processor.show_help_file())
        except Exception as error:
            print("Error happened: ", error)

if __name__ == "__main__":
    main()