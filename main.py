import contact
import phonebook

if __name__ == '__main__':
    anton = contact.Contact('Anton', 'Vasilyev', '+7123', telegram='telega', email='address@milo.wow',
                            work_phone='+7456')
    vasya = contact.Contact('Vasya', 'Pupkin', '+7697', fav_contact='Anton Vasilyev', email='myaddress@mail.py')
    pb = phonebook.PhoneBook('Телефонная книга')

    # print(anton)
    # print(vasya)
    # Карточка контакта

    pb.add_contact(anton)
    pb.add_contact(vasya)
    # Добавляем контакты

    pb.show_contacts()
    # Показать добавленные контакты

    pb.del_contact('+7123')
    # Удаление контакта

    pb.show_all_favs()
    # Показать все избранные контакты

    pb.contact_search('Vasya', 'Pupkin')
    # Поиск контакта
