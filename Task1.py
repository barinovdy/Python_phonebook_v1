# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while (1):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию абонента: ')
            find_by_lastname(phone_book, last_name)
        elif choice == 3:
            number = input('Введите номер телефона абонента: ')
            find_by_number(phone_book, number)
        elif choice == 4:
            user_data = input('Введите информацию о новом абоненте в формате "Фамилия,Имя,Телефон,Описание": ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            last_name = input('Введите фамилию абонента:  ')
            new_number = input('Введите новый номер телефона абонента: ')
            change_number(phone_book, last_name, new_number)
            write_txt('phonebook.txt', phone_book)
        elif choice == 6:
            lastname = input('Введите фамилию удаляемого абонента: ')
            delete_by_lastname(phone_book, lastname)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:
            write_txt('phonebook.txt', phone_book)
            print('Справочник сохранен в файл "phonebook.txt"')
        elif choice == 8:
            new_filename = input('Введите имя нового файла справочника без расширения: ')
            new_line = input('Введите номер копируемой строки справочника: ')
            write_new_file(new_filename, new_line, phone_book)
        elif choice == 9:
            return
        else:
            print('Некорректный ввод')
        choice = show_menu()

def show_menu():
    print(" == Телефонный справочник v1.0 ==\n"
          "  Выберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер абонента\n"
          "6. Удалить абонента\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Скопировать строку справочника в новый файл\n"
          "9. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding = 'utf-8') as phb:
        lines = [line.strip() for line in phb]
        for line in lines:
            if line != '':
                record = dict(zip(fields, line.split(',')))   
                phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename,'w',encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            # for v in phone_book[i].values():
            #     s = s + v + ','
            s = ','.join(phone_book[i].values())
            phout.write(s + '\n')

def print_result(phone_book):
    for i in range(len(phone_book)):
        s = ''
        # for v in phone_book[i].values():
        #     s = s + v + ', '
        s = ', '.join(phone_book[i].values())
        print(s)

def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        record = str(phone_book[i]['Фамилия'])
        record = str(phone_book[i].get('Фамилия', 'Нет фамилии'))
        if str(last_name).lower() in record.lower():
            s = ''
            # for v in phone_book[i].values():
            #     s = s + v + ', '
            s = ', '.join(phone_book[i].values())
            print('Найденный абонент: ' + s)
            return
    print('Абонент с фамилией ' + last_name + ' отсутствует')

def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        # if number == phone_book[i]['Телефон']:
        if number == phone_book[i].get('Телефон', 'Нет телефона'):
            s = ''
            # for v in phone_book[i].values():
            #     s = s  + v + ','
            s = ', '.join(phone_book[i].values())
            print('Найденный абонент: ' + s)
            return
    print('Абонент с номером телефона ' + number + ' отсутствует')

def add_user(phone_book, user_data):
    new_user = user_data.split(',')
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, new_user))
    phone_book.append(record)
    print('Новый абонент добавлен')
    return phone_book

def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        record = str(phone_book[i].values())
        if str(last_name).lower() in record.lower():
            phone_book[i]['Телефон'] = new_number
            print('Номер абонента с фамилией ' + last_name + ' изменен')
        return phone_book
    print('Абонент с фамилией ' + last_name + ' отсутствует')
    return phone_book

def delete_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        record = str(phone_book[i].values())
        if str(last_name).lower() in record.lower():
            phone_book = phone_book.pop(i)
            print('Запись об абоненте с фамилией ' + last_name + ' удалена')
        return phone_book
    print('Абонент с фамилией ' + last_name + ' отсутствует')
    return phone_book

def write_new_file(new_filename, new_line, phone_book):
    filename = str(new_filename) + '.txt'
    with open(filename, 'w', encoding = 'utf-8') as phout:
        s=''
        s = ', '.join(phone_book[int(new_line)].values())
        phout.write(f'{s[:-1]}\n')    
    print('Строка ' + new_line + 'справочника скопирована в файл ' + filename)

work_with_phonebook()