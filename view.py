from classes import Contact

def main_menu(menu_text, choice_menu, clue_input_menu):
    print(menu_text)
    while True:
        choice = input(choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print(clue_input_menu)


def print_info(message: str):
    print("\n" + "-" * len(message))
    print(message)
    print("-" * len(message) + "\n")

def question_load(change: bool, save: bool, message: str):
    if not save and change:
        answer = input(message + "(y/n) -> ")
        if answer.lower() == "y":
            return True
        else:
            return False
    return True

def question_save(load: bool, message: str):
    if not load:
        answer = input(message + "(y/n) -> ")
        if answer.lower() == "y":
            return True
        else:
            return False
    return True

def print_info_with_condition(save: bool, message: str):
    if save:
        print("\n" + "-" * len(message))
        print(message)
        print("-" * len(message) + "\n")

def show_contact(book: list[int, Contact], message: str):
    if book:
        max_len_comment = max([contact.get_len_comment() for _, contact in book])
        print("\n" + "-" * (47 + max_len_comment))
        for n, contact in book:
            print(f"{n:>3}. {contact}")
        print("-" * (47 + max_len_comment) + "\n")
    else:
        print()
        print(message)
        print()

def new_contact(new_name, new_phone, new_comment):
    print()
    name = input(new_name)
    phone = input(new_phone)
    comment = input(new_comment)
    return Contact(name, phone, comment)

def desired_contact(message):
    desired_element = input(message)
    return desired_element

def change_contact_index(message1, message2):
    index_change_contact = input(message1)
    if index_change_contact.isdigit():
        return int(index_change_contact) - 1
    else:
        print()
        print(message2)
        print()

def check_can_index(can_index, message):
    if not can_index:
        print()
        print(message)
        print()

def replacing_contact(message, new_name, new_phone, new_comment):
    print(message)
    name = input(new_name)
    phone = input(new_phone)
    comment = input(new_comment)
    return Contact(name, phone, comment)

def delete_contact_index(message1, message2):
    delete_index = input(message1)
    if delete_index.isdigit():
        return int(delete_index) - 1
    else:
        print()
        print(message2)
        print()

def confirm(message):
    print()
    answer = input(message + "(y/n) -> ")
    if answer.lower() == "y":
        return True
    else:
        return False
