import re


class Contact:
    def __init__(self, f_name, s_name, phone, fav_contact='', **kwargs):
        self.f_name = f_name
        self.s_name = s_name
        self.phone = phone
        self.kwargs = kwargs
        self.fav_contact = self.get_fav_contact(fav_contact)
        self.info = self.get_user_info()

    def get_fav_contact(self, fav_contact):
        if fav_contact:
            return fav_contact
        else:
            return 'нет'

    def get_user_info(self):
        return {
            'first_name': self.f_name,
            'second_name': self.s_name,
            'phone_number': self.phone,
            'favourite_contact': self.fav_contact,
            'additional_info': self.kwargs
        }

    def __str__(self):
        kwargs_format = re.sub(r"[(){}']", "", str(self.kwargs).replace(", ", "\n    "))
        return f'Имя: {self.f_name}' + '\n' + \
               f'Фамилия: {self.s_name}' + '\n' + \
               f'Телефон: {self.phone}' + '\n' + \
               f'В избранных: {self.fav_contact}' + '\n' + \
               'Дополнительная информация:' + '\n' + \
               f'    {kwargs_format}'
