def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me name and phone please."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def get_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return "Contact not found."

@input_error
def get_all_contacts(contacts):
    result = []
    if contacts:
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return "\n".join(result)
    else:
        return "No contacts found."

