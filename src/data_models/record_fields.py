import re
from datetime import datetime

MAX_LEN_PHONE_NUMBER = 10
email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not self.is_phone_number_valid(value):
            raise ValueError(f"Phone number must be {MAX_LEN_PHONE_NUMBER} digits")
        super().__init__(value)
    
    def is_phone_number_valid(self, phone_number):
        return phone_number.isdigit() and len(phone_number) == MAX_LEN_PHONE_NUMBER
        
    def __eq__(self, value):
        return self.value == value

class Email(Field):
    def __init__(self, email: str):
        self.is_email_valid(email)
        super().__init__(email)

    def is_email_valid(self, email: str):
        if re.match(email_regex, email) is None:
            raise Exception("Invalid email address")

    def update(self, email):
        self.is_email_valid(email)
        self.value = email

    def __eq__(self, value):
        return self.value == value

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = self.parse_birthday(value)
        except ValueError:
            raise ValueError("Invalid date format. Date format should be DD.MM.YYYY")
        super().__init__(self.value)
        
    def parse_birthday(self, value):
        if not isinstance(value, str):
            raise ValueError("Birthday date must be a string")
        
        birthday_date = datetime.strptime(value, "%d.%m.%Y").date()

        if birthday_date > datetime.now().date():
            raise ValueError("Birthday date cannot be in the future")

        return birthday_date
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

    def age(self):
        today = datetime.today()
        age = today.year - self.value.year
        if (today.month, today.day) < (self.value.month, self.value.day):
            age -= 1
        return age
