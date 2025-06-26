def handle(tokens):
    note_content = ' '.join(tokens[tokens.index('note')+1:])
    with open('notes.txt', 'a') as file:
        file.write(note_content + '\n')
    return "Note saved."