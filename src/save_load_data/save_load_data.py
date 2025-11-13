import pickle
from src.data_models.address_book import AddressBook
from src.data_models.notes_manager import NotesManager
from pathlib import Path
from rich.progress import (
    Progress, 
    SpinnerColumn, 
    TextColumn, 
    BarColumn, 
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn
)
import time
import src.constants.loading_data_consts as consts

def get_full_filepath(filename: str) -> Path:
    user_home = Path.home()
    if not (user_home / consts.SAVE_DATA_FOLDER_PATH).exists():
        (user_home / consts.SAVE_DATA_FOLDER_PATH).mkdir(parents=True)
    filename = user_home / consts.SAVE_DATA_FOLDER_PATH / filename
    return filename

def get_progress_object() -> Progress:
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
        BarColumn(bar_width=None, complete_style="blue", finished_style="green"),
        TextColumn("[white]{task.percentage:>3.1f}%"),
        TextColumn("•", style="yellow"),
        DownloadColumn(),
        TextColumn("•", style="yellow"),
        TransferSpeedColumn(),
        TextColumn("•", style="yellow"),
        TimeRemainingColumn())

def mimic_loading(progress: Progress, message_loading: str, filename: str):
    task = progress.add_task(message_loading, filename = filename, total = consts.TOTAL_STEPS)
    for i in range(consts.TOTAL_STEPS):
        time.sleep(consts.TIME_PER_STEP)
        progress.update(task, advance=1)

def load_addressbook_data() -> AddressBook:
    try:
        with open(get_full_filepath(consts.FILENAME_ADDRESSBOOK_DUMP), 'rb') as dump_file:
            address_book = pickle.load(dump_file)
            return address_book
    except FileNotFoundError:
        return AddressBook()

def load_notes_data() -> NotesManager:
    try:
        with open(get_full_filepath(consts.FILENAME_NOTES_DUMP), 'rb') as dump_file:
            notes = pickle.load(dump_file)
            return notes
    except FileNotFoundError:
        return NotesManager()

def save_data(data, filename):
    with open(get_full_filepath(filename), 'wb') as dump_file:
        pickle.dump(data, dump_file)

def save_all_data(book: AddressBook, notes: NotesManager):
    with get_progress_object() as progress:
        mimic_loading(progress, consts.SAVING_PROGRESS_ADDRESSBOOK, consts.SAVING_PROGRESS_ADDRESSBOOK)
        if len(book.data) > 0:
            save_data(book, consts.FILENAME_ADDRESSBOOK_DUMP)
        mimic_loading(progress, consts.SAVING_PROGRESS_NOTES, consts.SAVING_PROGRESS_NOTES)
        if len(notes.notes) > 0:
            save_data(notes, consts.FILENAME_NOTES_DUMP)

def load_all_data() -> tuple[AddressBook, NotesManager]:
    try:
        with get_progress_object() as progress:
            mimic_loading(progress, consts.LOADING_PROGRESS_ADDRESSBOOK, consts.LOADING_PROGRESS_ADDRESSBOOK)
            book = load_addressbook_data()
            mimic_loading(progress, consts.LOADING_PROGRESS_NOTES, consts.LOADING_PROGRESS_NOTES)
            notes = load_notes_data()
        return book, notes
    except Exception:
        return AddressBook(), NotesManager()