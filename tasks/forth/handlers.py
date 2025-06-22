def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict):
    if len(args) != 2:
        print("Invalid input, please enter \'add <name> <phone>\': ")
        return

    name, phone = args
    if name in contacts.keys():
        print(f"Contact with name {name} already exists.")
    else:
        contacts[name] = phone
        print("Contact added.")


def change_contact(args: list, contacts: dict):
    if len(args) != 2:
        print("Invalid input, please enter \'change <name> <phone>\': ")
        return
    name, phone = args
    if name not in contacts.keys():
        print(f"{name} is not in the contacts.")
    else:
        contacts[name] = phone
        print("Contact updated.")


def show_phone(args: list, contacts: dict):
    if len(args) != 1:
        print("Invalid input, please enter \'phone <name>\': ")
        return

    name = args[0]
    if name not in contacts:
        print(f"Contact with name {name} does not exists.")
    else:
        print(f"{name}\'s phone number is: {contacts[name]}")


def show_all(contacts: dict):
    if not contacts:
        print("You do not have contacts yet.")
    else:
        print(f"Here are all your contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
