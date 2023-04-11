class Contact:
    
    def __init__(self, name: str, phone: str, comment: str = ""):
        self.name = name
        self.phone = phone
        self.comment = comment
    
    def cont_to_str(self):
        return f"{self.name} - {self.phone} - {self.comment}"
    
    def cont_to_list(self):
        return [self.name, self.phone, self.comment]
    
    def get_len_comment(self):
        return len(self.comment)
    
    def __str__(self) -> str:
        return f"{self.name:<25}{self.phone:<15}{self.comment:<20}"
    
    def edit(self, name: str, phone: str, comment: str):
        self.name = name if name else self.name
        self.phone = phone if phone else self.phone
        self.comment = comment if comment else self.comment




class PhoneBook:

    def __init__(self, path: str):
        self.path = path
        self.phone_book: list[Contact] = []
        self.is_changed = False
        self.is_load = False
        self.is_save = False

    def load_file(self, need_load):
        if need_load:
            self.is_load = True
            self.phone_book.clear()
            with open(self.path, "r", encoding= "UTF-8") as file:
                data = file.readlines()
            for contact in data:
                contact = contact.strip() .split(" - ")
                self.phone_book.append(Contact(contact[0], contact[1], contact[2]))
            self.is_changed = False
            self.is_save = False
            return True
        return False
    
    def save_file(self, need_save):
        if need_save:
            self.is_save = True
            data = []
            for contact in self.phone_book:
                data.append(contact.cont_to_str())
            data = "\n".join(data)
            with open(self.path, "w", encoding="UTF-8") as file:
                file.write(data)
            self.is_changed = False
            return True
        return False

    def get_pb(self):
        return self.phone_book
    
    def add_contact(self, contact: Contact):
        self.phone_book.append(contact)
        self.is_changed = True
        self.is_save = False

    def find_contact(self, desired_element):
        found_contacts = []
        for n, contact in enumerate(self.phone_book, 1):
            for element in contact.cont_to_list():
                if element == desired_element:
                    found_contacts.append((n, contact))
        return found_contacts

    def check_index(self, index: int):
        if -1 < index < len(self.phone_book):
            return True
        return False
    
    def change_contact(self, contact: Contact, index: int):
        self.phone_book[index].edit(contact.name, contact.phone, contact.comment)
        self.is_changed = True
        self.is_save = False

    def delete_contact(self, index: int):
        self.phone_book.pop(index)
        self.is_changed = True
        self.is_save = False

    def exit_pb(self):
        if not self.is_save and self.is_changed:
            return True
        else:
            return False