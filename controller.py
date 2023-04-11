import view
import text_fields as txt
from classes import Contact, PhoneBook


def start_pb():
    phonebook = PhoneBook("phone_book.txt")
    while True:
        choice = view.main_menu(txt.menu_text, txt.choice_menu, txt.clue_input_menu)
        match choice:
            case 1:
                need_load = view.question_load(phonebook.is_changed, phonebook.is_save, txt.need_load)
                load = phonebook.load_file(need_load)
                view.print_info_with_condition(load, txt.load_successful)
            case 2:
                need_save = view.question_save(phonebook.is_load, txt.need_save)
                save = phonebook.save_file(need_save)
                view.print_info_with_condition(save, txt.save_successful)
            case 3:
                pb = list(enumerate(phonebook.get_pb(), 1))
                view.show_contact(pb, txt.no_contact_or_file)
            case 4:
                new_contact = view.new_contact(txt.new_name, txt.new_phone, txt.new_comment)
                phonebook.add_contact(new_contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                desired_element = view.desired_contact(txt.find_element)
                founds_contacts = phonebook.find_contact(desired_element)
                view.show_contact(founds_contacts, txt.no_element)
            case 6:
                index_change_contact = view.change_contact_index(txt.change_contact_number, txt.not_number)
                if index_change_contact != None:
                    can_index = phonebook.check_index(index_change_contact)
                    view.check_can_index(can_index, txt.no_index)
                    if can_index:
                        replacing_contact = view.replacing_contact(txt.new_contact_info, txt.new_name, txt.new_phone, txt.new_comment)
                        phonebook.change_contact(replacing_contact, index_change_contact)
                        view.print_info(txt.change_contact_successful)
            case 7:
                index_delete_contact = view.delete_contact_index(txt.delete_contact_number, txt.not_number)
                if index_delete_contact != None:
                    can_index = phonebook.check_index(index_delete_contact)
                    view.check_can_index(can_index, txt.no_index)
                    if can_index:
                        phonebook.delete_contact(index_delete_contact)
                        view.print_info(txt.delete_contact_successful)
            case 8:
                if phonebook.exit_pb():
                    if view.confirm(txt.is_changed):
                        if view.question_save(phonebook.is_load, txt.need_save):
                            _ = phonebook.save_file(True)
                view.print_info(txt.bye_bye)
                exit()