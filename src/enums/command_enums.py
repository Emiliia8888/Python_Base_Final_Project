from enum import Enum

class CommandEnum(Enum):
    HELLO = "hello"
    ADD = "add"
    CHANGE = "change"
    SHOW_ALL = "all"
    SHOW_PHONE = "phone"
    ADD_EMAIL = "add-email"
    SHOW_EMAIL = "email"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    BIRTHDAYS = "birthdays"
    EXIT_COMMANDS = ("exit", "close")