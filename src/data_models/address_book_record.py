from typing import List

from src.data_models.record_fields import Name, Phone, Email
from src.data_models.record_fields import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.emails: List[Email] = []
        self.birthday: Birthday|None = None
        self.address: str|None = None

    def add_phone(self, phone_number):
        if Phone(phone_number) not in self.phones:
            self.phones.append(Phone(phone_number))
            return f"Phone {phone_number} added to {self.name}"
        else:
            raise ValueError(f"Phone {phone_number} already exists for {self.name}")
    
    def edit_phone(self, old_phone_number, new_phone_number):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone_number:
                self.phones[index] = Phone(new_phone_number)
                return f"Phone {old_phone_number} changed to {new_phone_number} for {self.name}"
        
        raise ValueError(f"Phone {old_phone_number} not found for {self.name}")
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone.value
        
        raise ValueError(f"Phone {phone_number} not found for {self.name}")
    
    def remove_phone(self, phone: Phone):
        if not phone in self.phones:
            raise ValueError(f"Phone {phone} not found for {self.name}")
        self.phones.remove(phone)
        return f"Phone {phone} removed from {self.name}"

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)
        return f"Birthday {birthday_str} added to {self.name}"

    def add_email(self, email: Email):
        if email in self.emails:
            raise ValueError(f"Email {email} already exists for {self.name}")
        self.emails.append(email)

    def remove_email(self, email: Email):
        if not email in self.emails:
            raise ValueError(f"Email {email} is not set for this contact.")
        self.emails.remove(email)
        return "Email removed."

    def add_address(self, address: str):
        if not address:
            raise ValueError("Address cannot be empty")
        self.address = address

    def __str__(self):
        age = f"(age: {self.birthday.age()})" if self.birthday else ""
        return (f"{self.name}:"
                f"\n\tphones: {'; '.join(p.value for p in self.phones)}"
                f"\n\temails: {'; '.join(e.value for e in self.emails)}"
                f"\n\taddress: {self.address if self.address else 'N/A'}"
                f"\n\tbirthday: {self.birthday if self.birthday else 'N/A'}\t{age}")
