def parse_input(user_input: str) -> tuple[str]:
    """Get command from user input and parse it"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]):
    """Add contact to the list"""
    correct_command = is_input_correct(args)
    if correct_command:
        name, phone = args
        if name in contacts.keys():
            print(f"Contact with name {name} already exists.")
        else:
            contacts[name] = phone
            print("Contact added.")
    else:
        print("Invalid input, please enter \'add <name> <phone>\': ")


def change_contact(args: list[str], contacts: dict[str, str]):
    """Update phone number of the exist contact"""
    correct_command = is_input_correct(args)
    if correct_command:
        name, phone = args
        if name not in contacts.keys():
            print(f"{name} is not in the contacts.")
        else:
            contacts[name] = phone
            print("Contact updated.")
    else:
        print("Invalid input, please enter \'change <name> <phone>\': ")


def is_input_correct(args: list[str]) -> bool:
    """Basic validation of input data for 'add' and 'change' commands"""
    if len(args) == 2:
        is_name = args[0].isalpha()
        is_phone = args[1].isdigit()
        if is_name and is_phone:
            return True
    return False


def show_phone(args: list[str], contacts: dict[str, str]):
    """Show contact's phone based on contact's name"""
    if len(args) != 1:
        print("Invalid input, please enter \'phone <name>\': ")
        return

    name = args[0]
    if name not in contacts:
        print(f"Contact with name {name} does not exists.")
    else:
        print(f"{name}\'s phone number is: {contacts[name]}")


def show_all(contacts: dict[str, str]):
    """Show all contacts"""
    if not contacts:
        print("You do not have contacts yet.")
    else:
        print(f"Here are all your contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
