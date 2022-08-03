from fileinput import filename
from write import write as csvl
from pathlib import Path

def delete()->None:
    result_search = list()
    contact_search = input("\nВведите значение для удаление контакта из телефонной книги: ")
    phonebook = csvl(path = "phonebook",filename = "phonebook.csv")
    for contact_line in phonebook:
        if contact_search in contact_line:
            result_search.append(contact_line)
    if result_search == []:
        print("\nНенайдено")
    else:
        for result in result_search:
            final_list = result.split(";")
            print(f"\nФамилия: {final_list[0]}"f"Имя:{final_list[1]}"f"Очество:{final_list[2]}"f"телефон:{final_list[3]}")
    flag = bool(input("\nДля отмены нажмите Enter""\nДля подтверждения введите любое значение и Enter\n"))
    if flag:
        new_phonebook = list()
        for contact in phonebook:
            contact_math = False
            for contact_delete in result_search:
                if contact == contact_delete:
                    contact_match = True
            if not contact_match:
                new_phonebook.append(contact)
        filepath = Path("phonebook","phonebook.csv")
        with open(filepath,"w") as file:
            file.wrirelines(new_phonebook)