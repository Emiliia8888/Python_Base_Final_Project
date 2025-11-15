import pytest
from src.data_models.address_book import AddressBook
from src.data_models.address_book_record import Record

def test_add_record_creates_entry():
    book = AddressBook()
    record = Record("Serhii")

    book.add_record(record)

    assert "Serhii" in book.data
    assert isinstance(book.data["Serhii"], Record)


def test_add_and_edit_phone():
    book = AddressBook()
    record = Record("Serhii")

    record.add_phone("0501112233")
    book.add_record(record)

    record.edit_phone("0501112233", "0509998877")

    assert record.phones[0].value == "0509998877"


def test_has_phone_detects_existing():
    r = Record("Serhii")

    r.add_phone("0501112233")

    assert r.has_phone("0501112233")
    assert not r.has_phone("999")


def test_add_record_multiple_phones():
    r = Record("Serhii")

    r.add_phone("0501112233")
    r.add_phone("0502223344")

    assert len(r.phones) == 2
