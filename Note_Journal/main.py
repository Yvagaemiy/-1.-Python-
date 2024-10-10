# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку
from datetime import datetime

def create_file():
    with open("Note_titell.csv ", 'a'):
        pass

def date_time():
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return date

def take_user_input():
    date = date_time()
    user_title = input("\nВведите заголовок журнала: ").title()
    user_body = input("\nВведите описание заголовка: ").title()
    return f"Заголовок: {user_title}, Описание: {user_body}. фаил создан:({date})" 
def take_user_create_input():
    date = date_time()
    user_title = input("\nВведите заголовок журнала: ").title()
    user_body = input("\nВведите описание заголовка: ").title()
    return f"Заголовок: {user_title}, Описание: {user_body}. фаил изменен:({date})" 
def writet_note():
    input_user = take_user_input().title()
    with open("Note_titell.csv",'a', encoding="utf-8") as file:
        file.write(f"{input_user}\n\n") 
        print("\nЗапись сделана!\n")

def read_note():
    with open("Note_titell.csv","r",encoding="utf-8") as file:
        reads_note = file.read().rstrip().split("\n\n")
        return reads_note
def print_note():
    print_raed = read_note()
    for nn, i in enumerate(print_raed,1):
        print(f" {nn}. {i} \n") 

def search_note():
    print_raed = read_note()
    for nn, i in enumerate(print_raed,1):
        print(f" {nn}. {i} \n") 
    print("Поиск заметки!:\n")
    with open("Note_titell.csv",'r', encoding='utf - 8') as file:
       note_strs = file.read()
       note_list = note_strs.rstrip().split('\n\n')
    search_input = input('Введите данные для поиска: ').title()
    for nn, note_str in enumerate(note_list, 1):
        if search_input in note_str:
            print()
            print(f"Результат поиска = {nn}: {note_str}")

def copy_note():
    print_raed = read_note()
    for nn, i in enumerate(print_raed,1):
        print(f" {nn}. {i} \n")
    print("Копирование заметки!\n")
    date = date_time()
    note_list = read_note()
    user_num = int(input("\nВыберети номер для копирования: "))
    for nn,_ in enumerate(note_list,1):
        if user_num ==  nn:
            with open("Note_titell.csv",'a', encoding='utf - 8') as file:
                file.write(f"{note_list[nn -1 ]}. фаил скопирован({date}))\n\n")
                print(f"\nЗаметка [{note_list[user_num -1 ]}] cкопирована!\n\n") 

             
def edit_note():
    print_raed = read_note()
    for nn, i in enumerate(print_raed,1):
        print(f" {nn}. {i} \n")
    print("Редоктирование заметки!\n")
    edit_user = int(input("Выберите пункт для изменения: "))
    input_user = take_user_create_input().title()
    
    with open("Note_titell.csv",'r', encoding='utf - 8') as file:
        note_str = file.read().rstrip().split("\n\n")
    
        new_list=[]
        for i in note_str:
            i = i.replace(note_str[edit_user - 1],input_user)
            new_list.append(i)
            
            with open("Note_titell.csv",'w', encoding="utf-8") as file:
                    for j in new_list:
                        file.write(f"{j}\n\n")        
                   

def del_note():
    print_raed = read_note()
    for nn, i in enumerate(print_raed,1):
        print(f" {nn}. {i} \n")
    print("\nУдаление заметки!")
    search_input = int(input('\nВыберети пункт для удаления: '))
    with open("Note_titell.csv",'r', encoding='utf - 8') as file:
        note_str = file.read()
        new_list = note_str.rstrip().split("\n\n")
        for nn, i in enumerate(new_list,1):
            if search_input == nn:
                del new_list[search_input -1]
                with open("Note_titell.csv",'w', encoding='utf - 8') as file:
                    for j in new_list:
                        file.write(f"{j}\n\n")
                print("\nЗапись удалена!\n")
    

def interface():
    print("\n Добрый день!\n Вы находитесь в журнале заметок.")
    user_input = None
    while user_input!=7:
        print ( "1. Создать/дозаписать заметку\n"
                "2. Читать список заметок\n"
                "3. Поиск заметки\n"
                "4. Копировать заметку\n"
                "5. Редактировать заметку\n"
                "6. Удалять заметку\n"
                "7. Выход"
             )
        user_input = input("\n Выберите пункт: ")
        while user_input not in ('1','2','3','4','5','6','7'):
            print("\n Не коректный ввод!\n ")
            user_input = input("\n Выберите коректный пункт: ")   
        match  user_input:
            case '1':
                writet_note()
            case '2':
                print_note()
            case '3':
                search_note()
            case '4':
                copy_note()
            case '5':
                edit_note()
            case '6':
                del_note()
            case '7':
                print("\nДосвидание!\n")


if __name__ =='__main__':
    interface()
  