import os
from icecream import ic
# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных
FILE_NAME = 'telephone_directory.txt'


def get_data(file_name):
    try:
        with open(file_name, 'r') as f:
            contacts = f.readlines()
        return contacts    
    except FileNotFoundError as err:
        print(err.strerror)

def show_contacts(file_name):
    data = get_data(file_name)
    for ind, contact in enumerate(data, start=1):
        print(f'{ind}. {contact}', end='')
    input('Нажмите любую клавишу')


def inner_data():
    while True:
        contact = ' '.join(input('Введите контакт в формате "Фамили Имя телефон": ').split())
        if not contact:
            print('Вы не ввели никаких данных!')
            continue
        confirmation = input(
            f'Введеные данные:\n{contact}\nПодтверждаете сохранение сонтакта(да/нет): '                
            )
        if confirmation == 'да':
            return contact + '\n'
            


def add_contact(file_name):
    new_contact = inner_data()
    ic(new_contact)
    with open(file_name, 'a') as f:        
        f.write(new_contact)
        print(f'Контакт {new_contact} добавлен!')
    
    input('Нажмите любую клавишу')


def search_contact(file_name):
    target = ' '.join(input('Введите контакт для поиска: ').split())
    if not target:
        input('Вы ничего не ввели')
        return
    data = get_data(file_name)
    for ind, contact in enumerate(data):
        if target in contact:
            print(contact)
            is_target = input('Это нужный контакт? да/нет: ')
            if is_target == 'да':
                return data, ind
    else:
        print('Ни одного совпадения не найдено.')
    input('Нажмите любую клавишу')
    return None, None

def change_contact(file_name):
    data, ind = search_contact(file_name)
    if not data:
        return
    contant_for_change = data.pop(ind)
    confirmation = input(f'Изменить {contant_for_change}?: да/нет: ')
    if confirmation == 'да':
        new_contact_data = inner_data()
        data.insert(ind, new_contact_data)
        ic(data)
        with open(file_name, 'w') as f:
            f.write(''.join(data))
            print('Изменения внесены.')
    else:
        print('Изменения отменены.')
    input('Нажмите любую клавишу')

def delete_contact(file_name):
    data, ind = search_contact(file_name)
    contant_for_del = data.pop(ind)
    confirmation = input(f'Удалить {contant_for_del}?: да/нет: ')
    if confirmation == 'да':        
        with open(file_name, 'w') as f:
            f.write(''.join(data))
            print(f'Контакт удален.')
    else:
        print('Удаление отменено.')
    input('Нажмите любую клавишу')


def drawing():
    print(
        ' 1 - показать все контакты\n',
        '2 - добавить контакт\n',
        '3 - найти контакт\n',
        '4 - изменить контакт\n',
        '5 - удалить контакт\n',
        '6 - выход'
    )

def main(file_name):
    while True:
        os.system('clear')
        drawing()
        try:
            user_choice = int(input('Введите число от 1 до 6: '))
            if user_choice == 1:
                show_contacts(file_name)
            elif user_choice == 2:
                add_contact(file_name)
            elif user_choice == 3:
                search_contact(file_name)
            elif user_choice == 4:
                change_contact(file_name)
            elif user_choice == 5:
                delete_contact(file_name)
            elif user_choice == 6:
                print('Удачного дня!')
                break
        except ValueError:
            next
    
            

main(FILE_NAME)

