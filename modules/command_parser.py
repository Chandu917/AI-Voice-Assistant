from system_control import handle_system_command

def parse_command(command):
    # Return True if command is a system command, else False
    response = handle_system_command(command)
    return response is not None
