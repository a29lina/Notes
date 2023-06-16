from datetime import datetime
current_datetime = datetime.now()


def get_data():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return (data)


def print_data(data):
    data = open('notes.csv')
    for text in data:
        print(text)



def add_data(data):
    print('Введите текст: ')
    note = input()
    if len(data) > 0:
       data.pop()
    a = str(current_datetime)
    data.append(a + ' ' + f'{note}')


def write_data(data):
    file = open('notes.csv', 'a', encoding='utf-8')
    data = str(data)
    file.writelines(data)


def find_note():
    flag = 1
    print('Введите слово: ')
    word = input()
    for line in text:
        if word in line:
            flag = 0
            print(line)
    if flag:
        print('Такого слова нет')


def change_data():
    with open('notes.csv', 'r', encoding='utf-8') as f:
        old_data = f.read()
    print('Введите, что заменить: ')
    old_info = input()
    print('Введите, на что заменить: ')
    new_info = input()
    new_data = old_data.replace(old_info, new_info)
    with open('notes.csv', 'w', encoding='utf-8') as file:
        file.writelines(new_data)


def menu():
    print('МЕНЮ')
    print('Если хотите добавить заметку, нажмите 1')
    print('Если хотите найти заметку, нажмите 2')
    print('Если хотите редактировать зметку, нажмите 3')
    print('Если хотите увидеть весь список, нажмите 4')
    print('Чтобы закончить работу, нажмите 5')
    

    num = int(input())
   
    if num == 1:
        add_data(text)
        write_data(text)
        print('\n')
        menu()
    if num == 2:
        find_note()
        print('\n')
        menu()
    if num == 3:
        change_data()
        print('\n')
        menu()
    if num == 4:
        get_data()
        print_data(text)
        print('\n')
        menu()
    if num == 5:
        quit()       
    else:
        print("Неверный ввод, попробуйте снова")
        menu()


    

text = get_data()
menu()