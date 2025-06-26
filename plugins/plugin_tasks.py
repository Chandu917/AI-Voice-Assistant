def handle(tokens):
    task_content = ' '.join(tokens[tokens.index('task')+1:])
    with open('tasks.txt', 'a') as file:
        file.write(task_content + '\n')
    return "Task added to the list."