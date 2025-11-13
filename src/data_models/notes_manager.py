import datetime
from collections import UserDict
from typing import Set

from src.data_models.record_fields import Field

class Tag(Field):
    def __init__(self, tag):
        super().__init__(tag)

class Note(Field):
    def __init__(self, title):
        super().__init__(title)
        self.content = ""
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        self.tags: Set[Tag] = set()

    def edit(self, new_content):
        self.content = new_content
        self.updated_at = datetime.datetime.now()

    def add_tag(self, tag: Tag):
        self.tags.add(tag)

    def remove_tag(self, tag: Tag):
        self.tags.remove(tag)

    def __str__(self):
        return (f"Title: '{self.value}' "
                f"Tags: {', '.join(t.value for t in self.tags)} "
                f"created at: {self.created_at:%Y-%m-%d %H:%M} "
                f"updated at: {self.updated_at:%Y-%m-%d %H:%M}")


class NotesManager(UserDict):
    def __init__(self):
        super().__init__()
        self.notes = {}
        self.note_counter = 0 if len(self.notes) == 0 else max(self.notes.keys()) + 1

    def new(self, title):
        note_id = self.note_counter
        self.note_counter += 1
        note = Note(title)
        self.notes[note_id] = note
        return note_id

    def get(self, key, default=None) -> Note:
        return self.notes.get(key, default)

    def search(self, tag: str):
        for nid, note in self.notes.items():
            if Tag(tag) in note.tags:
                yield f"{nid}: {note.value} (updated {note.updated_at:%Y-%m-%d %H:%M})"

    def delete(self, note_id: int):
        if note_id in self.notes:
            del self.notes[note_id]
            return f"Deleted note {note_id}"
        else:
            raise ValueError("Note not found")

    #def edit_in_editor(self, note_id):
        #note = self.get(note_id)
        #if not note:
            #return "Note not found."

        #editor = TuiEditor()
        #editor.set_text(note.content or "")
        #print("Press Ctrl-S to exit editor")
        #editor.edit()
        #new_content = editor.get_text()

        #if new_content.strip() != note.content.strip():
            #note.edit(new_content)
            #return f"Updated note '{note.value}' ({note_id})"
        #else:
            #return "No changes made."

    def __str__(self):
        if not self.notes:
            raise ValueError("Notes book is empty")

        result = ["Notes Book:"]
        for id, note in self.notes.items():
            result.append(f"NoteId {int(id)}: {note}")
        return '\n'.join(result)
