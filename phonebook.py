# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

import os

phonebook = []

def menu():
    print("Телефонный справочник")
    print("1. Просмотреть справочник")
    print("2. Добавить контакт")
    print("3. Изменить контакт")
    print("4. Удалить контакт")
    print("5. Импорт из файла")
    print("6. Экспорт в файл")
    print("7. Выход")

def view_phonebook():
    if not phonebook:
        print("Телефонный справочник пуст")
    else:
        print("Телефонный справочник:")
        for contact in phonebook:
            print(f"Фамилия: {contact['last_name']}, Имя: {contact['first_name']}, Отчество: {contact['middle_name']}, Телефон: {contact['phone']}")

def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone': phone
    }
    phonebook.append(contact)
    print("Контакт добавлен")

def find_contact(attribute, value):
    found_contacts = []
    for contact in phonebook:
        if contact[attribute] == value:
            found_contacts.append(contact)
    return found_contacts

def edit_contact():
    attribute = input("Введите атрибут для поиска (фамилия, имя, отчество): ").lower()
    value = input(f"Введите {attribute}: ")
    found_contacts = find_contact(attribute, value)
    
    if not found_contacts:
        print("Контакт не найден")
    else:
        view_phonebook(found_contacts)
        choice = input("Выберите номер контакта для изменения: ")
        if choice.isdigit() and 0 <= int(choice) < len(found_contacts):
            contact_to_edit = found_contacts[int(choice)]
            new_value = input("Введите новое значение: ")
            contact_to_edit[attribute] = new_value
            print("Контакт изменен")
        else:
            print("Некорректный выбор")

def delete_contact():
    attribute = input("Введите атрибут для поиска (фамилия, имя, отчество): ").lower()
    value = input(f"Введите {attribute}: ")
    found_contacts = find_contact(attribute, value)
    
    if not found_contacts:
        print("Контакт не найден")
    else:
        view_phonebook(found_contacts)
        choice = input("Выберите номер контакта для удаления: ")
        if choice.isdigit() and 0 <= int(choice) < len(found_contacts):
            contact_to_delete = found_contacts[int(choice)]
            phonebook.remove(contact_to_delete)
            print("Контакт удален")
        else:
            print("Некорректный выбор")

def import_from_file():
    file_name = input("Введите имя файла для импорта: ")
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 4:
                    last_name, first_name, middle_name, phone = data
                    contact = {
                        'last_name': last_name,
                        'first_name': first_name,
                        'middle_name': middle_name,
                        'phone': phone
                    }
                    phonebook.append(contact)
        print("Данные импортированы")
    else:
        print("Файл не найден")

def export_to_file():
    file_name = input("Введите имя файла для экспорта: ")
    with open(file_name, 'w') as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone']}\n")
    print("Данные экспортированы")

while True:
    menu()
    choice = input("Выберите действие (1-7): ")
    
    if choice == '1':
        view_phonebook()
    elif choice == '2':
        add_contact()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        import_from_file()
    elif choice == '6':
        export_to_file()
    elif choice == '7':
        break
    else:
        print("Некорректный выбор")

print("Спасибо, что использовали телефонный справочник!")
