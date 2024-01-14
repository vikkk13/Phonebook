
import os


def export_data():
    with open("phone.txt", "r") as source_file:
        lines = source_file.readlines()
        line_number = int(input("Введите номер строки для копирования: "))
   
        with open("file_output.txt", "a") as target_file:
        
            if line_number > 0 and line_number <= len(lines):
                target_file.write(lines[line_number-1])
                print("Строка скопирована успешно!")
            else:
                print("Указан недопустимый номер строки. Введите корректные данные!")


def input_data(data):
    while True:
        user_input = input('введите номер телефона: ')
        if not user_input or not user_input.isdigit():
            return data
        if user_input in data:
            print('Такой номер уже есть!')
        else:
            temp = input("ФИО через пробел: ").split()
            if len(temp) != 3:
                print('Ошибка')
            else:
                data[user_input] = temp
                with open('phone.txt', 'a') as f:
                    print(f"{user_input}\t{temp[0]}\t{temp[1]}\t{temp[2]}", file=f)
                return data
            

def show_data(data):
    for key, value in data.items():
        print(key, *value)


def search_data(data):
    user_input = input("Поиск 1: номер телефона или 2: иное")
    if user_input not in {'1', '2'}:
        return
    if user_input == '1':
        phone = input("введите номер телефона: ")
        print(data.get(phone, 'Нет номера'))
        return
    other = input("Имя или Фамилия или Отчество")
    if ' ' in other or not other:
        print('Ошибка')
        return
    for key, values in data.items():
        for value in values:
            if other in value:
                print(key, *values)
                break


def main():
    if os.path.exists('phone.txt'):
        with open('phone.txt', 'r+') as file:
            data = {}
            for sentence in file:
                phone, second_name, first_name, third_name = sentence.split('\t')
                data[phone] = [second_name, first_name, third_name]
    else:
        with open('phone.txt', 'w') as f:
            data ={}

    print("Добро пожаловать в телефонный справочник!")
    while True:
            while True:
                user_input = input("""1:Ввести новые данные \n2:Просмотреть данные \n3:Поиск \n4:Выход\n5:Выгрузить строку в файл file_output.txt\n""")
                if user_input not in {'1', '2', '3', '4', '5'}:
                     print ('Неверное значение!')
                else:
                     break
            if user_input == '1':
                data = input_data(data)
            elif user_input == '2':
                show_data(data)     
            elif user_input == '3':
                search_data(data)
            elif user_input == '5':
                export_data()    
            else: 
                print('До свидания!')
                break    

if __name__ == '__main__':
    main()  





