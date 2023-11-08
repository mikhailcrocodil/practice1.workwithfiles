import psutil
import os
import json
import xml.etree.ElementTree as xml
import zipfile

def create_file(exstention):
    try:
        bl = False
        while bl != True:
            filename = input("Введите имя файла: ")
            filename = filename+exstention
            if os.path.exists(filename):
                bl = False
                print('Файл существует введите имя снова')
            else:
                bl = True
        return filename
    except BaseException as err:
        raise BaseException(f'Не удалось создать файл - ERR:{str(err)}')

def create_archive():
    try:
        bl = False
        while bl != True:
            filename = input("Введите имя архива: ")
            filename = filename + ".zip"
            if os.path.exists(filename):
                bl = False
                print('Архив существует. Введите имя снова')
            else:
                bl = True
        return filename
    except BaseException as err:
        raise BaseException(f'Не удалось создать архив - ERR:{str(err)}')


def info_disk():
    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"Диск: {partition.device}")
            print(f"Тип файловой системы: {partition.fstype}")
            print(f"Метка тома: {partition.mountpoint}")
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"Общий размер: {partition_usage.total / (1024 ** 3):.2f} ГБ\n")
    except BaseException as err:
        raise BaseException(f'Получение информации недоступно: info_disk - ERR: {str(err)}')


def work_file():
    try:
        filename = create_file(".txt")
        with open(filename, "w") as file:
            user_input = input("Введите строку для записи в файл: ")
            file.write(user_input)

        with open(filename, "r") as file:
            file_content = file.read()
            print(f"Информация из файла: {file_content}")

        choice = input("Удалить файл(y/n): ")
        if choice == "y":
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Файл {filename} удален")
            else:
                print("Файл не найден")
    except BaseException as err:
        raise BaseException(f'work_file - ERR: {str(err)}')

def work_json():
    try:
        filename = create_file(".json")
        user_surname = input("Введите фамилию: ")
        user_name = input("Введите имя: ")
        user_age = input("Введите возраст: ")
        user_university = input("Введите вуз: ")
        object = {
            "surname": user_surname,
            "name": user_name,
            "age": user_age,
            "university": user_university
        }

        with open(filename, "w") as file:
            json.dump(object, file)

        with open(filename, "r") as file:
            file_content = json.load(file)
            print(file_content)

        choice = input("Удалить файл(y/n): ")
        if choice == "y":
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Файл {filename} удален")
            else:
                print("Файл не найден")
    except BaseException as err:
        raise BaseException(f'work_json - ERR: {str(err)}')

def work_xml():
    try:
        filename = create_file(".xml")

        root = xml.Element("object")
        surname = xml.SubElement(root, "surname")
        name = xml.SubElement(root, "name")
        age = xml.SubElement(root, "age")
        university = xml.SubElement(root, "university")

        user_surname = input("Введите фамилию: ")
        user_name = input("Введите имя: ")
        user_age = input("Введите возраст: ")
        user_university = input("Введите вуз: ")

        surname.text = user_surname
        name.text = user_name
        age.text = user_age
        university.text = user_university

        tree = xml.ElementTree(root)
        tree.write(filename)

        tree = xml.parse(filename)
        root = tree.getroot()

        print("Информация из файла:")
        print(f"Фамилия: {root.find('surname').text}")
        print(f"Имя: {root.find('name').text}")
        print(f"Возраст: {root.find('age').text}")
        print(f"Вуз: {root.find('university').text}")

        choice = input("Удалить файл(y/n): ")
        if choice == "y":
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Файл {filename} удален")
            else:
                print("Файл не найден")
    except BaseException as err:
        raise BaseException(f'work_xml - ERR: {str(err)}')

def work_zip():
    try:
        filename = create_archive()
        file_name = input("Введите имя файла для добавления в архив (не забудьте указать формат файла): ")

        with zipfile.ZipFile(filename, 'w') as archive:
            archive.write(file_name)

        extract_dir = "Разархивированное"
        with zipfile.ZipFile(filename, 'r') as archive:
            archive.extractall(extract_dir)

        file_path = os.path.join(extract_dir, file_name)
        if os.path.isfile(file_path):
            print(f"Файл разархивирован: {file_path}")
            file_size = os.path.getsize(filename)
            print(f"Размер архива: {file_size} байт")

        choice = input("Удалить файл и архив(y/n): ")
        if choice == "y":
            if os.path.isfile(file_path):
                if os.path.exists(filename):
                    os.remove(file_path)
                else:
                    print("Файл не найден")
            if os.path.isfile(filename):
                if os.path.exists(filename):
                    os.remove(filename)
                else:
                    print("Файл не найден")
    except BaseException as err:
        raise BaseException(f'work_zip - ERR: {str(err)}')

try:
    print("1. Вывести информацию о диске")
    print("2. Работа с файлом")
    print("3. Работа с json")
    print("4. Работа с xml")
    print("5. Работа с zip")
    print("6. Выход")

    while True:
        choice = input("Введите номер нужного пункта: ")
        if choice == "1":
            info_disk()
        elif choice == "2":
            work_file()
        elif choice == "3":
            work_json()
        elif choice == "4":
            work_xml()
        elif choice == "5":
            work_zip()
        elif choice == "6":
            break
        else:
            continue
except BaseException as err:
    raise BaseException(f'Ошибка выполнения - ERR: {str(err)}')

