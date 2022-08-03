from search_contact import search_contact
from record import record
from delete import delete

def run_phonebook() -> None:
    while True:
        good_action = False
        while not good_action:
            action = input('\nВыберите нужное действие:'
            '\n1 - Добавить контакт в книгу'
            '\n2 - Найти и показать контакт по заданному значению'
            '\n3 - Удалить контакт из книги'
            '\n4 - Выход\n\n')
            if action.isdigit():
                action = int(action)
                if (1 <= action <= 4):
                    good_action = True
                else:
                    print('Для выбора действия ввведите число от 1 до 3-х!')
            else:
                print('Для выбора действия ввведите число от 1 до 3-х!')
        if action == 1:
             record()
        elif action == 2:
             search_contact()
        elif action == 3:
             delete()
        elif action == 4:
             exit()