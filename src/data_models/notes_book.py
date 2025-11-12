class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def find(self, keyword):
        return [n for n in self.notes if n.match(keyword)]

    def delete(self, title):
        self.notes = [n for n in self.notes if n.title != title]

    def show_all(self):
        return [f"{n.title}: {n.content} (tags: {', '.join(n.tags)})" for n in self.notes]
