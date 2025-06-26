def handle(tokens):
    if "news" in tokens:
        print("News plugin triggered.")
        return "The news plugin is active!"
    return None