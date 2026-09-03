notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]

def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")

def add_note():
    title = input("Gib einen Titel ein: ")
    text = input("Gib einen Text ein: ")
    notes.append({"title" : title, "text": text})

def delete_note(title):
    for note in notes:
        if note["title"] == title:
            notes.remove(note)

def update_note(old_title, new_title=None, new_text=None):
    for note in notes:
        if note["title"] == old_title:

            if new_title is not None:
                note["title"] = new_title

            if new_text is not None:
                note["text"] = new_text

            return

add_note()
delete_note("Einkauf")
update_note("Arbeit", new_title="Job", new_text="Backendcall um 14")
show_notes()