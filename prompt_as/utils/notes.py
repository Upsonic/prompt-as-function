notes = ""


def get_notes():
    global notes
    return notes


def add_note(note: str):
    """
    Noting important things
    """
    global notes
    notes += "\n" + note


def reset_notes():
    global notes
    notes = ""
