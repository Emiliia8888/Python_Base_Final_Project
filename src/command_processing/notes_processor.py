from src.data_models.notes_manager import NotesManager, Tag
from src.error_handling.error_handler import input_error

@input_error
def add_note(args, notes: NotesManager):
    title = " ".join(args)
    if len(title) == 0:
        raise ValueError("Title is required.")
    note_id = notes.new(title)
    return f"Created note: {note_id}"

@input_error
def edit_note(args, notes: NotesManager):
    note_id, *_ = args
    return notes.edit_in_editor(int(note_id))

@input_error
def delete_note(args, notes: NotesManager):
    note_id, *_ = args
    return notes.delete(int(note_id))

@input_error
def list_notes(notes: NotesManager):
    return str(notes)

@input_error
def add_tag(args, notes: NotesManager):
    note_id, tag, *_ = args
    note = notes.get(int(note_id))
    if not note:
        raise KeyError("Note not found in the book.")
    note.add_tag(Tag(tag))
    return note

@input_error
def remove_tag(args, notes: NotesManager):
    note_id, tag, *_ = args
    note = notes.get(int(note_id))
    if not note:
        raise KeyError("Note not found in the book.")
    note.remove_tag(Tag(tag))
    return note

@input_error
def search_notes(args, notes: NotesManager):
    tag, *_ = args
    found_notes = list(notes.search(tag))
    if len(found_notes) == 0:
        raise KeyError("Matching notes not found in the book.")
    return "\n".join(found_notes)

