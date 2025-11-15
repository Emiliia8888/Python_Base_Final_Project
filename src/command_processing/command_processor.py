from src.data_models.record_fields import Phone
from src.error_handling.error_handler import input_error
from src.data_models.address_book import AddressBook
from src.data_models.address_book_record import Record, Email

COUNT_DAYS_UPCOMING_BIRTHDAYS = 7
HELP_FILE_PATH = "help.txt"

def is_record_found(record: Record) -> bool:
    if record is None:
        raise KeyError("Contact not found in the book.")
    return True

@input_error
def show_help_file():
    with open(HELP_FILE_PATH, mode="r", encoding="UTF-8") as file_object:
        help_text = file_object.read()
    return help_text

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    book_record = book.find_by_name(name)
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
    name, old_phone, new_phone, *_ = args
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    message = book_record.edit_phone(old_phone, new_phone)
    return message

@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    phone_numbers = ', '.join(str(phone) for phone in book_record.phones)
    return phone_numbers

@input_error
def remove_phone(args, book):
    name, phone, *_ = args
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    return book_record.remove_phone(Phone(phone))

@input_error
def add_email(args, book: AddressBook):
    name, email, *_ = args
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    book_record.add_email(Email(email))
    return "Email added"

@input_error
def show_emails(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    emails = ', '.join(str(email) for email in book_record.emails)
    return emails

@input_error
def remove_email(args, book: AddressBook):
    name, email, *_ = args
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    return book_record.remove_email(Email(email))

@input_error
def show_all(book: AddressBook):
    return str(book)

@input_error
def add_birthday(args, book: AddressBook):
    name = args[0]
    birthday_str = args[1]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    message = book_record.add_birthday(birthday_str)
    return message

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
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

@input_error
def remove_contact(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    book.delete_record(name)
    return "Contact removed."

@input_error
def find_contact_by_name(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    return str(book_record)

@input_error
def find_contact_by_email(args, book: AddressBook) -> str:
    email = args[0]
    email_obj = Email(email)
    book_records = book.find_by_email(email_obj)
    if len(book_records) == 0:
        raise KeyError("No contacts found with the provided email.")
    result_messages = [str(record) for record in book_records]
    return '\n'.join(result_messages)

@input_error
def add_address(args, book: AddressBook):
    name = args[0]
    address = args[1::]
    address_str = ' '.join(address)
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    result_message = "Address added." if book_record.address is None else "Address updated."
    book_record.add_address(address_str)
    return result_message

@input_error
def remove_address(args, book: AddressBook):
    name = args[0]
    book_record = book.find_by_name(name)
    is_record_found(book_record)
    if book_record.address is None:
        raise ValueError("Address is not set for this contact.")
    book_record.address = None
    return "Address removed."
