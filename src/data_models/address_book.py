from collections import UserDict
from src.data_models.address_book_record import Record
from datetime import datetime
from src.data_models.record_fields import Email

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}
    
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Only Record objects can be added to address book")
        
        self.data[record.name.value] = record
        return f"Record for {record.name} added to address book."
    
    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record for {name} deleted from address book."
        else:
            raise ValueError (f"Record for {name} not found in address book.")
    
    def __str__(self):
        if not self.data:
            raise ValueError("Address book is empty")
        
        result = ["Address Book:"]
        for record in self.data.values():
            result.append(str(record))
        return '\n'.join(result)
    
    def get_upcoming_birthdays(self, days):
        upcoming_birthdays = []
        todays_date = datetime.now().date()
        
        for record in self.data.values():
            if record.birthday is not None:
                next_birthday_date = datetime(year=todays_date.year,
                                              month=record.birthday.value.month,
                                              day=record.birthday.value.day).date()
        
                if next_birthday_date < todays_date:
                    next_birthday_date = datetime(year=todays_date.year + 1,
                                                  month=record.birthday.value.month,
                                                  day=record.birthday.value.day).date()

                difference = next_birthday_date - todays_date
                if difference.days <= days:
                    user_congrats = {"name": record.name.value, "congratulation_date": next_birthday_date.strftime("%d.%m.%Y")}
                    upcoming_birthdays.append(user_congrats)
        
        return upcoming_birthdays

    def find_by_name(self, name) -> Record:
        return self.data.get(name, None)

    def find_by_email(self, email: Email) -> list[Record]:
       return [record for record in self.data.values() if email in record.emails]