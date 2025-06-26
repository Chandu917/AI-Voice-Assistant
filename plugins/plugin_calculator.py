def handle(tokens):
    try:
        expression = ' '.join(tokens[tokens.index('add')+1:])
        result = eval(expression)
        return f"The result is {result}."
    except Exception as e:
        return "Sorry, I couldn't calculate that."