from src.error_handling.error_handler import input_error
from src.data_models.address_book import AddressBook
from src.data_models.address_book_record import Record

COUNT_DAYS_UPCOMING_BIRTHDAYS = 7
HELP_FILE_PATH = "help.txt"

@input_error
def show_help_file():
    with open(HELP_FILE_PATH, mode="r", encoding="UTF-8") as file_object:
        help_text = file_object.read()
    return help_text

@input_error
def add_contact(args, book: AddressBook):
    name = args[0]
    phone = args[1]
    book_record = book.find(name)
    message = "Contact updated."
    if book_record is None:
        book_record = Record(name)
        book.add_record(book_record)
        message = "Contact added."
    if phone:
        book_record.add_phone(phone)
    return message

@input_error
def update_contact(args, book: AddressBook):
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    book_record = book.find(name)
    if book_record is None:
        raise KeyError("Contact not found in the book.")
    else:
        message = book_record.edit_phone(old_phone, new_phone)
    return message

@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    book_record = book.find(name)
    if book_record is None:
        raise KeyError("Contact not found in the book.")
    else:
        phone_numbers = ', '.join(str(phone) for phone in book_record.phones)
    return phone_numbers


@input_error
def add_email(args, book: AddressBook):
    name, email, *_ = args
    book_record = book.find(name)
    if book_record is None:
        raise KeyError("Contact not found in the book.")
    else:
        book_record.add_email(email)
        return "Email added"

@input_error
def show_emails(args, book: AddressBook):
    name = args[0]
    book_record = book.find(name)
    if book_record is None:
        raise KeyError("Contact not found in the book.")
    else:
        emails = ', '.join(str(email) for email in book_record.emails)
    return emails

@input_error
def show_all(book: AddressBook):
    return str(book);

@input_error
def add_birthday(args, book: AddressBook):
    name = args[0]
    birthday_str = args[1]
    book_record = book.find(name)
    if book_record is None:
        raise KeyError("Contact not found in the book.")
    else:
        message = book_record.add_birthday(birthday_str)
    return message

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    book_record = book.find(name)

    if book_record is None:
        raise KeyError("Contact not found in the book.")
    if book_record.birthday is None:
        raise ValueError("Birthday is not set for this contact yet.")
    
    return f"{name}'s birthday is on {book_record.birthday}"

@input_error
def birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays(COUNT_DAYS_UPCOMING_BIRTHDAYS)
    if not upcoming_birthdays:
        return "No upcoming birthdays found."
    
    result_message = ["Upcoming birthdays for next week:"]
    for entry in upcoming_birthdays:
        result_message.append(f"{entry['name']} - {entry['congratulation_date']}")
    return '\n'.join(result_message)
