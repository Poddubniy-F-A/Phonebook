PATH = 'phonebook.txt'
PHONE_NUMBER_INDEX = 3


def add_case():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    address = input('Введите адрес: ')

    with open(PATH, 'a', encoding='UTF-8') as file:
        file.write(f'{surname} {name} {patronymic} {phone}\n{address}\n\n')

    print('\nКонтакт добавлен')


def get_contacts_list():
    with open(PATH, 'r', encoding='UTF-8') as file:
        return file.read().rstrip().split('\n\n')


def contact_list_to_str(contact):
    new_contact = ''
    for i in range(len(contact) - 2):
        new_contact += contact[i] + ' '
    new_contact += contact[-2] + '\n' + contact[-1]

    return new_contact


def overwrite_file(contacts_list):
    with open(PATH, 'w') as file:
        for string in contacts_list:
            file.write(string + '\n\n')


def edit_contact(contacts, contact, index):
    print(
        'Возможные действия с контактом:'
        '\n1. Изменить фамилию'
        '\n2. Изменить имя'
        '\n3. Изменить отчество'
        '\n4. Изменить номер телефона'
        '\n5. Изменить адрес'
    )

    edit_var = input('Выберите нужное действие: ')
    while edit_var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        edit_var = input('Выберите нужное действие (1-5): ')

    match edit_var:
        case '1':
            contact[0] = input('Введите новую фамилию: ')
        case '2':
            contact[1] = input('Введите новое имя: ')
        case '3':
            contact[2] = input('Введите новое отчество: ')
        case '4':
            contact[3] = input('Введите новый номер телефона: ')
        case '5':
            contact[4] = input('Введите новый адрес: ')

    contacts[index] = contact_list_to_str(contact)
    overwrite_file(contacts)


def edit_case():
    search = input('Введите номер телефона контакта, который вы хотите изменить: ')
    contacts = get_contacts_list()

    index = 0
    for contact_str in contacts:
        contact_lst = contact_str.replace('\n', ' ').split()
        if contact_lst[PHONE_NUMBER_INDEX] == search:
            edit_contact(contacts, contact_lst, index)
            print('\nКонтакт изменен')
            break
        index += 1
    else:
        print('\nКонтакта с таким телефонным номером не существует')


def delete_contact(contacts, contact):
    contacts.remove(contact_list_to_str(contact))
    overwrite_file(contacts)


def delete_case():
    search = input('Введите номер телефона контакта, который вы хотите удалить: ')
    contacts = get_contacts_list()

    for contact_str in contacts:
        contact_lst = contact_str.replace('\n', ' ').split()
        if contact_lst[PHONE_NUMBER_INDEX] == search:
            delete_contact(contacts, contact_lst)
            print('\nКонтакт удален')
            break
    else:
        print('\nКонтакта с таким телефонным номером не существует')


def show_case():
    with open(PATH, 'r', encoding='UTF-8') as file:
        print(file.read().rstrip())


def search_case():
    print(
        'Возможные способы поиска:'
        '\n1. По фамилии'
        '\n2. По имени'
        '\n3. По отчеству'
        '\n4. По номеру телефона'
        '\n5. По адресу'
    )

    search_var = input('Выберите способ поиска: ')
    while search_var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        search_var = input('Введите способ поиска (1-5): ')

    index_var = int(search_var) - 1
    search = input('Введите поисковый запрос: ')

    search_was_successful = False
    for contact in get_contacts_list():
        if contact.replace('\n', ' ').split()[index_var] == search:
            print('\n' + contact)
            search_was_successful = True
    if not search_was_successful:
        print('\nНичего не найдено')


def copy_case():
    while True:
        try:
            path = input('Введите путь к файлу, куда хотите скопировать контакт: ')
            with open(path, 'a', encoding='UTF-8') as target:
                while True:
                    try:
                        index = input('Введите индекс контакта, который хотите скопировать: ')
                        target.write(get_contacts_list()[int(index) - 1] + '\n\n')
                        break
                    except ValueError:
                        print('Индекс должен быть целым числом')
                    except IndexError:
                        print('Контакта с таким индексом не существует')
            break
        except FileNotFoundError:
            print('Файла по указанному пути не существует')
    print('\nКонтакт скопирован')


print('Приветствуем в нашем телефонном справочнике!')

command = None
while command != '7':
    print('\nДоступные способы взаимодействия:'
          '\n1. Добавить контакт'
          '\n2. Изменить контакт'
          '\n3. Удалить контакт'
          '\n4. Вывести контакты на экран'
          '\n5. Поиск контакта'
          '\n6. Копирование контакта'
          '\n7. Выход из программы')

    command = input('Введите номер действия: ')
    while command not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Некорректный ввод')
        command = input('Введите номер действия (1-7): ')

    print()
    match command:
        case '1':
            add_case()
        case '2':
            edit_case()
        case '3':
            delete_case()
        case '4':
            show_case()
        case '5':
            search_case()
        case '6':
            copy_case()

print('Всего хорошего!')
