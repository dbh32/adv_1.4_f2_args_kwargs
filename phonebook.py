class PhoneBook:
    def __init__(self, pb_title):
        self.title = pb_title
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def show_contacts(self):
        for contact in self.contact_list:
            print(contact)
            print('')

    def del_contact(self, number):
        for contact in self.contact_list:
            if number in contact.info['phone_number']:
                self.contact_list.remove(contact)
            else:
                pass

    def show_all_favs(self):
        for contact in self.contact_list:
            if contact.fav_contact != 'нет':
                print(f'У {contact.f_name} {contact.s_name}'
                      f' в избранных {contact.fav_contact}')

    def contact_search(self, f_name, s_name):
        for contact in self.contact_list:
            if contact.f_name == f_name and contact.s_name == s_name:
                print(contact)
