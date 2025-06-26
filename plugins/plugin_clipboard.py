import pyperclip

def handle(tokens):
    if 'copy' in tokens:
        text_to_copy = ' '.join(tokens[tokens.index('copy')+1:])
        pyperclip.copy(text_to_copy)
        return "Text copied to clipboard."
    elif 'paste' in tokens:
        return f"Clipboard content: {pyperclip.paste()}"
    else:
        return "No clipboard action detected."